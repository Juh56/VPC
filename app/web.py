"""Web interface for running the VPC MVP inside GitHub Codespaces."""

from pathlib import Path

import cv2
from flask import Flask, Response, render_template_string

from .vision import detect_faces, load_face_detector

app = Flask(__name__)
_detector = load_face_detector()

HTML = """<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>VPC — Visão Computacional</title>
  <style>
    body { font-family: system-ui, sans-serif; max-width: 900px; margin: 40px auto; padding: 0 20px; }
    video { width: 100%; max-width: 720px; border-radius: 12px; background: #111; }
    button { padding: 10px 16px; margin: 8px 4px 8px 0; cursor: pointer; }
    #status { margin: 12px 0; }
  </style>
</head>
<body>
  <h1>VPC — Detecção de Rostos</h1>
  <p>O navegador fornece a câmera e o Codespace executa o processamento.</p>
  <video id="video" autoplay playsinline></video>
  <div>
    <button onclick="startCamera()">Iniciar câmera</button>
    <button onclick="stopCamera()">Parar</button>
  </div>
  <p id="status">Câmera parada.</p>
  <canvas id="canvas" hidden></canvas>
<script>
let stream;
let timer;
const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const status = document.getElementById('status');

async function startCamera() {
  try {
    stream = await navigator.mediaDevices.getUserMedia({video: true, audio: false});
    video.srcObject = stream;
    status.textContent = 'Câmera ativa.';
    clearInterval(timer);
    timer = setInterval(sendFrame, 500);
  } catch (error) {
    status.textContent = 'Não foi possível acessar a câmera: ' + error.message;
  }
}

function stopCamera() {
  clearInterval(timer);
  if (stream) stream.getTracks().forEach(track => track.stop());
  video.srcObject = null;
  status.textContent = 'Câmera parada.';
}

async function sendFrame() {
  if (!video.videoWidth) return;
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  canvas.getContext('2d').drawImage(video, 0, 0);
  const blob = await new Promise(resolve => canvas.toBlob(resolve, 'image/jpeg', 0.75));
  const response = await fetch('/detect', {method: 'POST', body: blob});
  const data = await response.json();
  status.textContent = `Rostos detectados: ${data.faces}`;
}
</script>
</body>
</html>"""


@app.get("/")
def index():
    return render_template_string(HTML)


@app.post("/detect")
def detect():
    # Flask receives the current browser frame; no image is persisted to disk.
    import numpy as np

    data = request.get_data()
    image = cv2.imdecode(np.frombuffer(data, dtype=np.uint8), cv2.IMREAD_COLOR)
    if image is None:
        return {"error": "Imagem inválida"}, 400

    faces = detect_faces(image, _detector)
    return {"faces": len(faces)}


def run() -> None:
    app.run(host="0.0.0.0", port=8000, debug=False)


if __name__ == "__main__":
    run()
