import cv2
import mediapipe as mp
import numpy as np
from flask import Flask, Response

# Replace with your DroidCam IP
DROIDCAM_URL = "http://192.168.31.180:4747/video"

app = Flask(__name__)

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(
    static_image_mode=False,
    model_complexity=1,
    enable_segmentation=False,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

mp_drawing = mp.solutions.drawing_utils

# Open DroidCam stream
cap = cv2.VideoCapture(DROIDCAM_URL)


def generate_frames():
    while True:
        success, frame = cap.read()
        if not success:
            continue

        # Convert to RGB for MediaPipe
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(frame_rgb)

        # Create black background
        black_frame = np.zeros_like(frame)

        # Draw pose landmarks only
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                black_frame,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=3, circle_radius=4),
                mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=3)
            )

        # Encode frame for streaming
        ret, buffer = cv2.imencode('.jpg', black_frame)
        frame_bytes = buffer.tobytes()

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n'
        )


@app.route('/')
def video_feed():
    return Response(
        generate_frames(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
