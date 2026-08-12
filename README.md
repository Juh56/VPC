# VPC

Projeto inicial de visão computacional para detecção e análise de rostos.

## MVP

- Captura de imagens por câmera.
- Detecção de rostos.
- Visualização das detecções.
- Base preparada para testes automatizados.

## Estrutura

```text
VPC/
├── README.md
├── .gitignore
├── requirements.txt
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── camera.py
│   └── vision.py
├── tests/
│   └── test_vision.py
├── data/
│   └── .gitkeep
└── docs/
    └── arquitetura.md
```

## Instalação

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate
pip install -r requirements.txt
```

## Execução

```bash
python -m app.main
```

> Este MVP faz detecção de rosto. Identificação de pessoas e armazenamento de dados biométricos serão tratados em etapas posteriores, com atenção a consentimento, privacidade e segurança.
