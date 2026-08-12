"""Computer-vision primitives used by the VPC MVP."""

from pathlib import Path

import cv2


CASCADE_PATH = Path(cv2.data.haarcascades) / "haarcascade_frontalface_default.xml"


def load_face_detector() -> cv2.CascadeClassifier:
    """Load the OpenCV Haar cascade used for face detection."""
    detector = cv2.CascadeClassifier(str(CASCADE_PATH))
    if detector.empty():
        raise RuntimeError(f"Could not load face detector: {CASCADE_PATH}")
    return detector


def detect_faces(frame, detector=None):
    """Return face bounding boxes detected in a BGR OpenCV frame."""
    if frame is None:
        raise ValueError("frame cannot be None")

    detector = detector or load_face_detector()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return detector.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(40, 40),
    )
