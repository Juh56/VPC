"""Static-image web interface for the VPC MVP."""

from pathlib import Path

import cv2
from flask import Flask, render_template_string, request, send_from_directory

from .vision import detect_faces, load_face_detector

app = Flask(__name__)
_detector = load_face_detector()
OUTPUT_DIR = Path("data/output")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

HTML = """<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>VPC — Imagem estática</title>
</head>
<body>
  <h1>VPC — Detecção de Rostos</h1>
  <p>Envie uma imagem para detectar e marcar os rostos encontrados.</p>
  <form method="post" enctype="multipart/form-data">
    <input type="file" name="image" accept="image/*" required>
    <button type="submit">Processar imagem</button>
  </form>
  {% if message %}<p>{{ message }}</p>{% endif %}
  {% if result %}<p>Rostos detectados: <strong>{{ count }}</strong></p><img src="{{ result }}" alt="Resultado da detecção" style="max-width:100%;height:auto">{% endif %}
</body>
</html>"""


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template_string(HTML, message=None, result=None)

    uploaded = request.files.get("image")
    if uploaded is None or not uploaded.filename:
        return render_template_string(HTML, message="Selecione uma imagem.", result=None)

    data = uploaded.read()
    image = cv2.imdecode(__import__("numpy").frombuffer(data, dtype="uint8"), cv2.IMREAD_COLOR)
    if image is None:
        return render_template_string(HTML, message="Arquivo de imagem inválido.", result=None)

    faces = detect_faces(image, _detector)
    for x, y, width, height in faces:
        cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)

    output_name = "resultado.jpg"
    cv2.imwrite(str(OUTPUT_DIR / output_name), image)
    return render_template_string(HTML, message="Imagem processada.", count=len(faces), result=f"/result/{output_name}")


@app.get("/result/<path:filename>")
def result(filename):
    return send_from_directory(OUTPUT_DIR, filename)


def run() -> None:
    app.run(host="0.0.0.0", port=8000, debug=False)


if __name__ == "__main__":
    run()
