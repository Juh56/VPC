# Arquitetura inicial

O MVP do VPC é dividido em três responsabilidades:

- `app/camera.py`: acesso à câmera local.
- `app/vision.py`: detecção de rostos usando OpenCV.
- `app/main.py`: laço principal, visualização e integração dos módulos.

## Fluxo

```text
Câmera
   ↓
Captura de frame
   ↓
Conversão para escala de cinza
   ↓
Detector Haar Cascade
   ↓
Coordenadas dos rostos
   ↓
Visualização na janela
```

A primeira etapa deliberadamente separa **detecção** de **identificação**. O reconhecimento de identidade, caso seja adicionado futuramente, deverá ter controles de acesso, consentimento e tratamento adequado de dados biométricos.
