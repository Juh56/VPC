# VPC

MVP de visão computacional para **detecção de rostos em imagens estáticas**.

## Como funciona

```text
Imagem → OpenCV → Detecção de rosto → Imagem marcada + contagem
```

O MVP atual não usa câmera e não faz identificação de pessoas. A câmera fica reservada para uma etapa futura.

## Rodar no Codespace

Instale as dependências:

```bash
pip install -r requirements.txt
```

### Opção 1 — linha de comando

Coloque uma imagem em `data/input/`, por exemplo `data/input/foto.jpg`, e execute:

```bash
python -m app.main data/input/foto.jpg
```

O resultado será salvo em:

```text
data/output/foto_detectada.jpg
```

Também é possível escolher o arquivo de saída:

```bash
python -m app.main data/input/foto.jpg --output data/output/resultado.jpg
```

### Opção 2 — interface web no Codespace

Execute:

```bash
python -m app.web
```

Abra a porta **8000** na aba **PORTS** do Codespace e escolha **Open in Browser**. Envie uma imagem pelo formulário e o VPC mostrará a quantidade de rostos detectados e a imagem marcada.

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
│   ├── vision.py
│   └── web.py
├── data/
│   ├── input/
│   └── output/
├── tests/
└── docs/
```

## Próxima evolução

Depois de validar a detecção em imagens estáticas, podemos evoluir o projeto por etapas, mantendo a identificação de pessoas separada da simples detecção facial e tratando dados biométricos com os cuidados de privacidade e segurança necessários.
