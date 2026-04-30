from pynq import Overlay, allocate
import numpy as np
import cv2, zmq, base64

# ===============================
# LOAD BITSTREAM
# ===============================
ol = Overlay("final.bit")
dma = ol.axi_dma_0

WIDTH, HEIGHT = 640, 480

# Buffers
in_buf  = allocate((HEIGHT, WIDTH), dtype=np.uint8)
out_buf = allocate((HEIGHT, WIDTH), dtype=np.uint8)

# ===============================
# ZMQ SETUP
# ===============================
context = zmq.Context()

recv_socket = context.socket(zmq.SUB)
recv_socket.connect("tcp://192.168.2.15:5555")
recv_socket.setsockopt_string(zmq.SUBSCRIBE, '')

send_socket = context.socket(zmq.PUB)
send_socket.bind("tcp://*:5556")

print("PYNQ: Clean + Crisp FPGA output running...")

# ===============================
# MAIN LOOP
# ===============================
while True:
    msg = recv_socket.recv()

    # Decode
    jpg = base64.b64decode(msg)
    frame = cv2.imdecode(np.frombuffer(jpg, np.uint8), cv2.IMREAD_COLOR)

    if frame is None:
        continue

    frame = cv2.resize(frame, (WIDTH, HEIGHT))

    # ===============================
    # 🔥 PREPROCESS (VERY IMPORTANT)
    # ===============================
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Strong blur → removes noise
    gray = cv2.GaussianBlur(gray, (7, 7), 1.5)

    # Contrast boost → better edges
    gray = cv2.equalizeHist(gray)

    # ===============================
    # FPGA CANNY
    # ===============================
    in_buf[:] = gray
    dma.sendchannel.transfer(in_buf)
    dma.recvchannel.transfer(out_buf)
    dma.sendchannel.wait()
    dma.recvchannel.wait()

    # ===============================
    # 🔥 POSTPROCESS (KEY FIX)
    # ===============================

    # 1. Remove noise (small dots)
    kernel = np.ones((3,3), np.uint8)
    clean = cv2.morphologyEx(out_buf, cv2.MORPH_OPEN, kernel)

    # 2. Thin edges slightly
    clean = cv2.medianBlur(clean, 3)

    # 3. Controlled sharpening (no noise boost)
    blur = cv2.GaussianBlur(clean, (3,3), 0)
    sharp = cv2.addWeighted(clean, 1.6, blur, -0.6, 0)

    # ===============================
    # SEND BACK
    # ===============================
    _, buffer = cv2.imencode('.jpg', sharp,
                             [int(cv2.IMWRITE_JPEG_QUALITY), 85])

    send_socket.send(base64.b64encode(buffer))