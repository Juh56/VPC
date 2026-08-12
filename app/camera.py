"""Camera capture helpers for the VPC MVP."""

import cv2


def open_camera(index: int = 0):
    """Open a local camera and raise a clear error if unavailable."""
    camera = cv2.VideoCapture(index)
    if not camera.isOpened():
        camera.release()
        raise RuntimeError(f"Could not open camera index {index}")
    return camera
