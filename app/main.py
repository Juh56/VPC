"""Process static images for the VPC MVP."""

import argparse
from pathlib import Path

import cv2

from .vision import detect_faces, load_face_detector


def process_image(input_path: Path, output_path: Path) -> int:
    """Detect faces in one image and save an annotated copy."""
    image = cv2.imread(str(input_path))
    if image is None:
        raise ValueError(f"Não foi possível ler a imagem: {input_path}")

    faces = detect_faces(image, load_face_detector())
    for x, y, width, height in faces:
        cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    if not cv2.imwrite(str(output_path), image):
        raise RuntimeError(f"Não foi possível salvar o resultado: {output_path}")

    return len(faces)


def main() -> None:
    parser = argparse.ArgumentParser(description="VPC - detecção de rostos em imagens")
    parser.add_argument("input", type=Path, help="caminho da imagem de entrada")
    parser.add_argument("-o", "--output", type=Path, default=None, help="caminho da imagem de saída")
    args = parser.parse_args()

    output = args.output or Path("data/output") / f"{args.input.stem}_detectada{args.input.suffix}"
    count = process_image(args.input, output)
    print(f"Rostos detectados: {count}")
    print(f"Resultado salvo em: {output}")


if __name__ == "__main__":
    main()
