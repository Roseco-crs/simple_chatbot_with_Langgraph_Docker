# Simple Langgraph project with Docker: Containerized LangGraph Agent

A simple, robust chatbot built with **LangGraph** and **LangChain**, fully containerized with **Docker** for seamless deployment.

## 🚀 Features
- **Stateful Logic:** Uses LangGraph to manage conversation flow and agent states.
- **Fast Inference:** Powered by Groq LPU for near-instant responses.
- **Modern Tooling:** Uses `uv` for lightning-fast Python dependency management.
- **Dockerized:** Build once, run anywhere. No "works on my machine" excuses.

## 🛠️ Prerequisites
- Docker installed.
- A Groq API Key.

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Roseco-crs/simple_chatbot_with_Langgraph_Docker.git](https://github.com/Roseco-crs/simple_chatbot_with_Langgraph_Docker)
   cd imple_chatbot_with_Langgraph_Docker
   docker build -t app.py .
   docker run --env-file .env -p 8501:7860 app.py
