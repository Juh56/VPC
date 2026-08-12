import numpy as np

from app.vision import detect_faces, load_face_detector


def test_face_detector_loads():
    detector = load_face_detector()
    assert not detector.empty()


def test_detect_faces_on_blank_frame():
    frame = np.zeros((240, 320, 3), dtype=np.uint8)
    faces = detect_faces(frame)
    assert len(faces) == 0
