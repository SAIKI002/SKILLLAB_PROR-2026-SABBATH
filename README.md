# SKILL LAB PRATICAL HACKATHON

## Final Project README

> **Project Weight:** 100%  
> **Team Size:** 4/3 students  
> **Project Duration:** 16 hours  
> **Total Time Available:** 32 effort-hours per team  
> **Project Type:** Playful, interactive, technology-based experience

---

# Before you begin

## Fork and rename this repository

After forking this repository, rename it using the format:

`SKILLLAB_PROR-2026-TeamName`

### Example

`SKILLLAB_PROR-2026-AuroWizards`

Do not keep the default repository name.

---

# How to use this README

This file is your team’s **working project document**.

You must keep updating it throughout the build period.  
By the final review, this README should clearly show:

- your idea,
- your planning,
- your design decisions,
- your technical process,
- your build progress,
- your testing,
- your failures and changes,
- your final outcome.

## Rules

- Fill every section.
- Do not delete headings.
- If something does not apply, write `Not applicable` and explain why.
- Add images, screenshots, sketches, links, and videos wherever useful.
- Update task status and weekly logs regularly.
- Use this file as evidence of process, not only as a final report.

---

# 1. Team Identity

## 1.1 Sabbath

`Project^2`

## 1.2 Team Members

| Name                  | Primary Role                    | Secondary Role   | Strengths Brought to the Project |
| --------------        | ------------------------------- | --------------   | -------------------------------- |
| `Shlok Shety` | `[Electronics / Coding / App ]` | `Documentation`  | `Documentation, Gift of Gab `|
| `Rahul Vidwans`        | `[Electronics / Fabrication]`   | `[Coding]`       | `Material Handling, Hardware`    |
| `Samruddhi Shimpi`        | `[Electronics / Fabrication]`   | `[Coding]`       | `Material Handling, Hardware`    |
| `Atharva Chaudhari`        | `[Electronics / Fabrication]`   | `[Coding]`       | `Material Handling, Hardware`    |

## 1.3 Project Title

`Realtime edge detection using FPGA`

`(because Project-or)`

<img width="1600" height="1131" alt="image" src="https://github.com/user-attachments/assets/c64bfbd4-b3b7-43d9-83ad-c203a5aa11bc" />

## 1.4 One-Line Pitch

`A real-time FPGA-accelerated edge detection system using the PYNQ-Z2 board that processes live camera input and generates high-speed edge-enhanced output using DSP-based image processing.`

## 1.5 Expanded Project Idea

- This project focuses on implementing a real-time edge detection system using an FPGA-based hardware accelerator on the PYNQ-Z2 platform. The system captures live video input from a webcam, preprocesses the image using Python and OpenCV inside a Jupyter Notebook environment, and sends the grayscale image to a custom FPGA IP core through AXI DMA for high-speed edge detection processing. The processed edge-detected output is then displayed in real time on an external monitor.

- The main goal of the project is to demonstrate the power of FPGA-based parallel processing for image processing applications. Unlike CPU-based image processing, where pixels are processed sequentially, the FPGA processes multiple operations simultaneously using DSP48 hardware blocks, pipelining, and streaming architectures. The project implements Scharr/Canny-inspired edge detection using pure Verilog RTL design without relying on HLS tools, making it a fully hardware-oriented implementation.

- The project combines computer vision and FPGA hardware acceleration into one integrated system. It demonstrates how hardware/software co-design can achieve low-latency real-time image processing suitable for robotics, surveillance, autonomous systems, medical imaging, and smart vision applications.


**Response:**  
`A projected and fully customizable time portal can transform engineering education into an immersive PUBG-style battlefield experience from the comfort of home. In this environment, students can learn engineering concepts by entering a virtual battlefield where challenges, obstacles, and missions are designed around real technical problems. Instead of passively studying theory, learners actively apply concepts such as electronics, coding, sensors, robotics, mechanics, and system design to complete missions, solve problems, and progress through different levels. This approach makes engineering education more interactive, engaging, and practical by combining gaming, simulation, and hands-on problem-solving in a familiar and exciting format.`

---

# 2. Inspiration

## 2.1 References

List what inspired the project.

| Source Type | Title / Link                                                        | What Inspired You                                                                         |
| ----------- | ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `[Video]`   | `https://youtu.be/Ut5s4rImEhI?si=zgon5YOzGiYfu-Zj` | `How the company is using it's tech to perform image scans` |
|             |                                                                     |                                                                                           |
|             |                                                                     |                                                                                           |

## 2.2 Original Twist

This project combines Scharr-based gradient computation with a Canny-inspired edge detection pipeline implemented on FPGA using pure Verilog RTL and DSP48 hardware acceleration on the PYNQ-Z2 platform. Unlike traditional software-based image processing, the system performs real-time edge detection using AXI DMA and streaming FPGA architecture for low-latency live video processing.

**Response:**  


---

# 3. Project Intent

## 3.1 User Journey 

The user starts the system through a Jupyter Notebook, and the webcam begins capturing live video. The normal camera feed quickly transforms into an edge-detected view, where only the outlines of objects are visible. As the user moves their hand or objects, the edges update instantly in real time. The FPGA processes each frame continuously, providing fast and smooth output with minimal delay.This system demonstrates how edge detection is used in real-world applications such as autonomous vehicles (lane detection), surveillance systems, medical imaging, robotics, and object detection systems.

**Response:**  

                                                  |



---

# 4. Definition of Success

## 4.1 Definition of “Usable”
In this project, the system is considered usable when the live image feed is captured and processed continuously without interruption, the FPGA correctly performs edge detection on incoming frames, and the output displays clear, stable edges in real time. Additionally, the data transfer through DMA must operate reliably without crashes or delays, ensuring smooth and consistent overall performance.

## 4.2 Minimum Usable Version

The smallest version of this project that still delivers the core experience consists of a basic real-time pipeline where a laptop camera captures live video, the image is converted to grayscale using Python/OpenCV, and the frames are sent to the FPGA through AXI DMA. The FPGA then performs simple Iimage's edge detection algorithm and returns the processed output, which is displayed on the screen in real time.

**Response:**  


## 4.3 Stretch Features

- Implementation of full Canny edge detection (including non-maximum suppression and hysteresis)
- Adjustable threshold values through user input
- Support for multiple edge detection filters (Sobel, Scharr, Laplacian switching)
- HDMI-based direct video output from FPGA
- Real-time resolution scaling (720p / 1080p support)
- On-screen display of FPS or performance metrics
- Hardware-based grayscale conversion instead of software preprocessing
- User interface for selecting modes or tuning parameters


---

# 5. System Overview

## 5.1 Project Type

Check all that apply.

- [x] Electronics-based

- [ ] Mechanical

- [ ] Sensor-based

- [x] App-connected

- [ ] Motorized

- [ ] Sound-based

- [x] Light-based

- [ ] Screen/UI-based

- [ ] Fabricated structure

- [ ] Game logic based

- [ ] Installation

- [ ] Other:

## 5.2 High-Level System Description

Explain how the system works in simple terms.

Include:

- input,
- processing,
- output,
- physical structure,
- app interaction if any.

**Response:**  

## 5.3 Input / Output Map

| System Part                              | Type            | What It Does                                                               |


---

# 6. System Design, Sketches and Visual Planning 

## 6.1 Concept Architecture/sketch/schematic

Add an early sketch of the full idea.

**Insert image below:**  
`[Upload image and link here]`

Example:

```md

```



## 6.2 Labeled Build Sketch/architecture/flow diagram/algorithm

Add a sketch with labels showing:

- structure,
- electronics placement,
- user touch points,
- moving parts,
- output elements.

**Insert image below:**  
`[Upload image and link here]`
<img width="1600" height="1200" alt="image" src="https://github.com/user-attachments/assets/95637f31-b4e7-4427-a9e1-4b63fbeb0ac5" />

## 6.3 Approximate Dimensions

| Dimension        | Value   |
| ---------------- | ------- |
| Length           | `16 cm` |
| Width            | `16 cm` |
| Height           | `8 cm`  |
| Estimated weight | `400 g` |

---

# 7. Electronics Planning

## 7.1 Electronics Used

| Component                 | Quantity | Purpose                               |
| ------------------------- | --------:| ------------------------------------- |
| `FPGA`                 | `1`      | `[Main controller]`                   |
| `Laptop`    | `1`      | `As a camera device`                    |

## 7.2 Wiring Plan

Describe the main electrical connections.

**sample Response:**  
`The RASPI is connected to the motor driver (L298N) using four GPIO pins (18,19; 22,23) to control motor direction (IN1, IN2, IN3, IN4). Two PWM-capable pins (ENA and ENB; 25 and 26) are connected to control the speed of each motor.

The motors are connected to the output terminals of the motor driver. The motor driver is powered directly by the battery pack (higher voltage), while the ESP32 receives regulated 5V from the buck converter.

All components share a common ground to ensure stable operation. The projector and camera are connected to the laptop, which handles tracking and game logic separately.`

## 7.3 Circuit Diagram/architecture diagram

Insert a hand-drawn or software-made circuit diagram.

**Insert image below:**  
`[Upload image and link here]`
<img width="867" height="1156" alt="" src="" />


# 7.4. Power Plan

| Question         | Response                                                                                                                                          |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Power source     | `Battery (Li-ion pack)`                                                                                                                           |
| Voltage required | `~6–8.4V for motors (via driver), stepped down to 5V for ESP32 (buck converter)`                                                                  |
| Current concerns | `Motors can draw high current under load, which may cause voltage drops affecting ESP32 and WiFi stability`                                       |
| Safety concerns  | `Avoid over-discharging Li-ion batteries, ensure proper voltage regulation, prevent short circuits, and secure wiring to avoid loose connections` |

---

# 8. Software Planning/

## 8.1 Software Tools

| Tool / Platform                | Purpose                                        |
| ------------------------------ | ---------------------------------------------- |
| `Vivado`                | `used to design, implement, and generate the FPGA hardware (edge detection IP and system architecture).`                                |
| `Jupyter notebook`       | `used to control the system, capture and preprocess images, and communicate with the FPGA using DMA.` |


## 8.2 Software Logic/Algorithm

Describe what the code must do.

Include:

- startup behavior,
- input handling,
- sensor reading,
- decision logic,
- output behavior,
- communication logic,
- reset behavior.

**Response:**  
`

- **Sample Startup behavior:**  
  The Raspi/FPGA initializes motor pins, PWM control, and starts a WiFi access point with a web server. The laptop initializes camera input, tracking system, and projection mapping.
- **Input handling:**  
  Movement commands are received from the laptop (pygame sends http requests)
- **Sensor reading:**  
  The camera continuously captures frames, and OpenCV detects ArUco markers to determine the car’s position and orientation.
- **Decision logic:**  
  The system maps the car’s position into a virtual coordinate system and checks for nearby obstacles or collisions. If movement is valid, the command is allowed; if not, it is blocked or replaced with a feedback action (like a slight shake).
- **Output behavior:**  
  The ESP32 drives the motors using PWM signals to control speed and direction. The projector displays the updated game environment, including obstacles, targets, and feedback visuals.
- **Communication logic:**  
  The laptop sends HTTP requests (e.g., `/forward`, `/left`) to the ESP32 over WiFi. The ESP32 parses these commands and executes motor actions.
- **Reset behavior:**  
  If no command is received within a short timeout, the ESP32 stops the motors. The game resets when a level is completed or restarted.`

## 8.3 Code Flowchart

Insert a flowchart showing your code logic.

Suggested sequence:

- start,
- initialize,
- wait for input,
- read input,
- decision,
- trigger output,
- repeat or reset,
- error handling.

**Insert image below:**  
<img width="1600" height="1200" alt="image" src="" />
<img width="1600" height="1200" alt="image" src="" />




# 9. Bill of Materials

## 9.1 Full BOM

| Item                             | Quantity | In Kit? | Need to Buy? | Estimated Cost | Material / Spec               | Why This Choice?          |
| -------------------------------- | --------:| ------- | ------------ | --------------:| ----------------------------- | ------------------------- |
| `PYNQ-Z2 board`                        | `1`      | `Yes`   | `No`         | `₹25K`            | `xc7z020clg400-1`                | `Due to inbuilt access of Jupyter notebook` |


## 9.2 Material Justification

The PYNQ-Z2 board (xc7z020clg400-1) was selected as the main platform because it combines an FPGA with an embedded processor, allowing both hardware acceleration and software control in a single system. One of the key reasons for choosing this board is its built-in support for Jupyter Notebook, which simplifies development by enabling Python-based control, image preprocessing, and easy interaction with the FPGA through AXI DMA.

This combination makes the development process faster and more accessible compared to traditional FPGA workflows, while still allowing low-level hardware implementation using Verilog in Vivado. Overall, the board provides an ideal balance between ease of use, flexibility, and powerful real-time processing capabilities required for this project.

**Response:**  
`DC motors (BO motors) were chosen instead of servos or steppers because the system requires continuous rotation for movement rather than precise angular control (Previously, we were considering using steppers as we were planning on tracking movement on the ESP using its relative position from an origin, but since we're using a camera now, this is not required). A motor driver (L298N) was used to allow bidirectional control and speed variation using PWM.`


## 9.3 Items You chose

| Item                 | Why Needed               | Purchase Link | Latest Safe Date to Procure | Status       |
| -------------------- | ------------------------ | ------------- | --------------------------- | ------------ |
| `PYNQ board (xc7z020clg400-1)` | `it enables real-time FPGA processing with easy control through built-in Jupyter Notebook.`   | `none`     | `-`                | `[Received]` |


## 9.4 Budget Summary

| Budget Item           | Estimated Cost              |
| --------------------- | ---------------------------:|
| Electronics           | `[400]`                     |
| Mechanical parts      | `[200]`                     |
| Fabrication materials | `[0 (Available on campus)]` |
| Purchased extras      | `[0]`                       |
| Contingency           | `[300]`                     |
| **Total**             | `[900]`                     |

## 9.5 Budget Reflection

If the cost becomes too high, the system can be simplified by using a basic USB webcam instead of a high-end camera and relying on a laptop display instead of an external monitor or HDMI setup. Components like additional cables, adapters, or extra peripherals can be minimized or shared among team members. The processing setup can remain focused on the PYNQ-Z2 board without adding extra hardware modules, since it already provides both FPGA and processor capabilities. This keeps the project functional while reducing overall cost

**Response:**  

---

# 10. Planning the Work

## 10.1 Team Working Agreement

Write how your team will work together.

Include:

- how tasks are divided,
- how decisions are made,
- how progress will be checked,
- what happens if a task is delayed,
- how documentation will be maintained.

**Response:**  


## 10.2 Task Breakdown

| Task ID | Task                    | Owner    | Estimated Hours | Deadline     | Dependency | Status |
| ------- | ----------------------- | -------- | ---------------:| ------------ | ---------- | ------ |
| T1      | `[Finalize concept]`    | `[Both]` | `2`             | `1st April`  | `None`     | `Done` |


## 10.3 Responsibility Split

| Area                 | Main Owner     | Support Owner |
| -------------------- | ----------     | ------------- |
| Concept              | `[Mrugendra]`  | `[Jyoti]`     |
| Electronics          | `[]`           | `[]`          |
| Coding               | `[]`           | `[]`          |
| Mechanical build     | `[]`           | `[]`          |
| Testing              | `[]`           | `[]`          |
| Documentation        | `[]`           | `[]`          |

---

# 11 hour Milestones

## 11.1 8-hour Plan(tentetively you may set)

### Bi Hour 1 — Plan and De-risk

Expected outcomes:

- [x] Idea finalized
- [x] Core interaction decided
- [x] Sketches made
- [x] BOM completed
- [x] Purchase needs identified
- [ ] Key uncertainty identified
- [x] Basic feasibility tested

### Bi Hour 2 — Build Subsystems

Expected outcomes:

- [x] Electronics tests completed
- [ ] CAD / structure planning completed
- [ ] App UI started if needed
- [x] Mechanical concept tested
- [x] Main subsystems partially working

### Bi Hour 3 — Integrate

Expected outcomes:

- [x] Physical body built
- [x] Electronics integrated
- [x] Code connected to hardware
- [ ] App connected if required
- [x] First playable version exists

### Bi Hour 4 — Refine and Finish

Expected outcomes:

- [x] Technical bugs reduced
- [x] Playtesting completed
- [x] Improvements made
- [x] Documentation completed
- [x] Final build ready

## 12.2  Update Log

| Days   | Planned Goal   | What Actually Happened | What Changed   | Next Steps     |
| ------ | -------------- | ---------------------- | -------------- | -------------- |
| Day 1 | `[Write here]` | `[Write here]`         | `[Write here]` | `[Write here]` |
| Day 2 | `[Write here]` | `[Write here]`         | `[Write here]` | `[Write here]` |
| Day 3 | `[Write here]` | `[Write here]`         | `[Write here]` | `[Write here]` |
| Day 4 | `[Write here]` | `[Write here]`         | `[Write here]` | `[Write here]` |

---

# 13. Risks and Unknowns

## 13.1 Risk Register

| Risk                                                            | Type         | Likelihood | Impact   | Mitigation Plan                                                                       | Owner                |
| --------------------------------------------------------------- | ------------ | ---------- | -------- | ------------------------------------------------------------------------------------- | -------------------- |
| WiFi connection between laptop and ESP32 becomes unstable       | `Technical`  | `Medium`   | `High`   | Keep ESP32 close, ensure stable power supply, reduce network load, add fail-safe stop | `[Gopal]`           |


## 13.2 Biggest Unknown Right Now

What is the single biggest uncertainty in your project at this stage?

**Response:**  


---

# 14. Testing 

## 14.1 Technical Testing Plan

| What Needs Testing     | How You Will Test It                                                                 | Success Condition                                                                                    |
| ---------------------- | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| `[Wifi connection]`    | `[Check if motor spins via app button]`                                              | `[Both motors accurately respond to wifi signals]`                                                   |
                       |
## 14.2 Testing and Debugging Log

| Date          | Problem Found                         | Type         | What You Tried                                | Result               | Next Action                                    |
| ------------- | ------------------------------------- | ------------ | --------------------------------------------- | -------------------- | ---------------------------------------------- |
| `18th April`  | `Car not balancing properly`          | `Mechanical` | `Add low-friction caster support to one side` | `Worked`             | `improve caster structure`                     |


## 14.3 Playtesting Notes

| Tester      | What They Did                        | What Confused Them                    | What They Enjoyed                         | What You Will Change                          |
| ----------- | ------------------------------------ | ------------------------------------- | ----------------------------------------- | --------------------------------------------- |
| `Gopal` | `Tried navigating through obstacles` | `Some obstacles ewren't clear enough` | `Liked projection + real car interaction` | `Add a slight red highlight around obstacles` |


---

# 15. Build Documentation

## 15.1 Fabrication Process(if any)

Describe how the project was physically made.

Include:

- cutting,
- 3D printing,
- assembly,
- fastening,
- wiring,
- finishing,
- revisions.

**Response:**  
`The fabrication process involved designing, manufacturing, assembling, and refining both the physical structure and electronic integration of the system.`

`Design (CAD Modeling):
The initial model was created using CAD software, where components were designed based on the actual dimensions of the electronic parts. This ensured accurate fitting and minimized errors during assembly.
Cutting (Laser Cutting):
The designed parts were fabricated using laser cutting techniques. Sheets were cut precisely according to the CAD model to create the structural base and mounts for components.`

`Components were fixed using adhesives and mechanical supports. Certain parts were intentionally kept modular (not permanently fixed) to allow easy replacement and modification of electronics.
Surface Finishing:
Some parts were sanded to smooth rough edges after cutting. Sawdust mixed with adhesive was used to fill gaps and uneven edges, improving structural finish. The final structure was then painted for better aesthetics and durability.`

`Environment Setup (Dark Room Fabrication):
To enhance projection visibility, a controlled dark environment was created using Z-boards, paper sheets, and bedsheets. This minimized external light interference and improved projection clarity.
Revisions and Iterations:
Multiple adjustments were made throughout the process, including refining alignment, improving structural stability, repositioning components, and optimizing the interaction between the physical car and projected environment.`

## 16 Build Photos

Add photos throughout the project.

Suggested images:

- early sketch,
- prototype,
- electronics testing,
- mechanism test,
- app screenshot,
- final build.
- <img width="960" height="1280" alt="WhatsApp Image 2026-04-24 at 9 46 02 AM (1)" src="https://github.com/user-attachments/assets/74baa570-5770-483e-be6d-d2f03386e37c" />





# 17. Final Outcome

## 17.1 Final Description

Describe the final version of your project.

**Response:**  


## 17.2 What Works Well



## 17.3 What Still Needs Improvement


## 17.4 What Changed From the Original Plan

How did the project change from the initial idea?

**Response:**  


---

# 18. Reflection

## 18.1 Team Reflection

What did your team do well?  
What slowed you down?  
How well did you manage time, tasks, and responsibilities?

**Response:**  


## 18.2 Technical Reflection

What did you learn about:

- electronics,
- coding,
- mechanisms,
- fabrication,
- integration?

**Response:**  


## 18.3 Design Reflection

What did you learn about:

- designing ,
- delight,
- clarity,
- physical interaction,
- understanding,
- iteration?

**Response:**  


## 18.4 If You Had One More hour

What would you improve next?

**Response:**  

` `

---

# 19. Final Submission Checklist

Before submission, confirm that:

- [x] Team details are complete
- [x] Project description is complete
- [x] Inspiration sources are included
- [x] Sketches are added
- [x] BOM is complete
- [x] Purchase list is complete
- [x] Budget summary is complete
- [x] Mechanical planning is documented if applicable
- [ ] App planning is documented if applicable
- [x] Code flowchart is added
- [x] Task breakdown is complete
- [x] Weekly logs are updated
- [x] Risk register is complete
- [x] Testing log is updated
- [x] Playtesting notes are included
- [x] Build photos are included
- [x] Final reflection is written
<img width="1131" height="1600" alt="image" src="" />

---


---


