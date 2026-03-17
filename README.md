# Motion Mate – Real-Time Human Pose Estimation System

## Overview
Motion Mate is an embedded vision project designed to perform real-time human pose estimation and motion analysis on edge hardware. The system captures live video, detects human skeletal keypoints, and visualizes body posture efficiently with minimal latency.

The project is implemented using Python, OpenCV, and MediaPipe Pose, and deployed on a Raspberry Pi 4 Model B. It uses DroidCam for wireless video streaming, enabling flexible camera input without additional hardware dependencies.

---

## Features
- Real-time single-person pose detection
- Skeletal keypoint extraction and visualization
- Low-latency processing optimized for edge devices
- Modular pipeline: capture → inference → visualization
- Wireless video input using DroidCam

---

## System Architecture
1. Video Capture  
   - Frames are captured via DroidCam over Wi-Fi

2. Pose Estimation  
   - MediaPipe Pose processes each frame to extract keypoints

3. Visualization  
   - Detected landmarks are drawn using OpenCV

4. Output  
   - Processed video stream is displayed in real time

---

## Tech Stack
- Python
- OpenCV
- MediaPipe Pose
- Raspberry Pi 4 Model B

---

## Installation

### Prerequisites
- Python 3.x
- Raspberry Pi OS (or any Linux-based system)
- DroidCam (mobile app + client)

### Install dependencies
```bash
pip install opencv-python mediapipe numpy
