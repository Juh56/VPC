"""Run the VPC face-detection MVP with a local camera."""

import cv2

from .camera import open_camera
from .vision import detect_faces


def main() -> None:
    camera = open_camera()
    detector = None

    try:
        while True:
            ok, frame = camera.read()
            if not ok:
                print("Could not read frame from camera.")
                break

            faces = detect_faces(frame, detector)
            for x, y, width, height in faces:
                cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)

            cv2.imshow("VPC - Face Detection", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        camera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
