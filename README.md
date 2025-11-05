# 🤖 Twitter AI Bot

Este proyecto automatiza la **creación y publicación de hilos de Twitter** utilizando **OpenAI** y la **API de Twitter**.

## 🚀 Características
- Lee temas desde `data/topics.csv`
- Genera hilos con GPT (ChatGPT API)
- Publica los hilos automáticamente en Twitter
- Configurable mediante variables de entorno `.env`

## 🛠 Instalación

```bash
git clone https://github.com/tuusuario/twitter_ai_bot.git
cd twitter_ai_bot
pip install -r requirements.txt
cp .env.example .env
```
Edita `.env` con tus claves de OpenAI y Twitter.

## ▶️ Ejecución

```bash
python -m src.main
```

## 🧠 Estructura

```
twitter_ai_bot/
│
├── src/
│   ├── main.py
│   ├── services/
│   ├── utils/
│
├── data/topics.csv
├── .env.example
├── requirements.txt
└── README.md
```

## ⚡ Credenciales requeridas

- OpenAI API Key → [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)
- Twitter Developer Portal → [https://developer.twitter.com/](https://developer.twitter.com/)

## 💡 Nota
Nunca subas tu archivo `.env` al repositorio público.
