

import cv2
import zmq
import base64
import time

# PYNQ will connect to this port
PORT = "5555"

def stream_builtin_camera():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind(f"tcp://*:{PORT}") 

    # '0' targets the default built-in laptop webcam
    cap = cv2.VideoCapture(0)
    print(f"Laptop: Streaming built-in camera on port {PORT}...")
    print("Press Ctrl+C in this terminal to stop.")

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
                
            # Compress to JPEG to ensure it fits through the network smoothly
            params = [int(cv2.IMWRITE_JPEG_QUALITY), 80]
            _, buffer = cv2.imencode('.jpg', frame, params)
            
            # Encode as Base64 string and send
            socket.send(base64.b64encode(buffer))

            # Tiny sleep to prevent network buffer overflow
            time.sleep(0.01)

    except KeyboardInterrupt:
        print("\nStopping laptop stream.")
    finally:
        cap.release()
        socket.close()

if __name__ == "__main__":
    stream_builtin_camera()