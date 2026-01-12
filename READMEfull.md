---
title: AI Log Analysis Agent
emoji: 🧠
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: "4.44.0"
app_file: app.py
pinned: false
---

# AI Log Analysis Agent (RAG + MCP-style Architecture)

## 🚀 Overview
This project demonstrates an **AI-powered log analysis system** that identifies the **root cause and resolution** of system failures using **Retrieval-Augmented Generation (RAG)**.

The key idea is that the **LLM never answers directly**.  
Instead, it retrieves relevant historical incidents from a **vector database** and generates responses **only using injected context**.  
This mirrors **MCP-style tool calling** and helps **prevent hallucinations**.

A live, interactive demo is deployed on **Hugging Face Spaces**.

---

## 🧩 Problem Statement
In distributed systems, failure logs are often:
- Large and unstructured
- Time-consuming to analyze manually
- Repetitive across services and regions

Engineers frequently debug the same classes of issues (DB timeouts, certificate expiry, API failures), but this knowledge is rarely reused efficiently.

---

## ✅ Solution
This system automates log analysis by:
1. Storing historical failure incidents in a **vector database**
2. Performing **semantic similarity search** for new failures
3. Injecting only relevant historical context into the LLM prompt
4. Generating a concise explanation of:
   - Root cause
   - Resolution

If no similar incident exists, the system explicitly reports that no context was found.

---

## 🏗️ Architecture (High Level)
User Log Input
↓
Vector Similarity Search (ChromaDB)
↓
Context Injection (RAG)
↓
LLM Inference (Instruction-tuned model)
↓
Root Cause & Resolutio

---

## 🧠 Why This Is Not a Simple Chatbot
- The LLM **does not rely on its internal knowledge**
- All answers are constrained by retrieved context
- Prevents hallucination
- Stateless and reproducible
- Easily extensible to MCP servers or tool-based agents

This design reflects **real-world AI system architecture**, not prompt-only chatbots.

---

## 🛠️ Tech Stack
- **Python**
- **Gradio** – UI
- **ChromaDB** – Vector database
- **Sentence Transformers** – Embeddings
- **Transformers (FLAN-T5)** – Instruction-tuned LLM
- **LangChain (Community)** – Vector store integration
- **Hugging Face Spaces** – Deployment

---

## 📂 Project Structure

├── app.py # Gradio UI + inference
├── ingest.py # Vector DB ingestion
├── data/
│ └── sample_logs.csv # Synthetic historical logs
├── requirements.txt # Strict dependency pinning
├── pyproject.toml # Project metadata
├── .gitignore
└── README.md


---

## ▶️ How It Works

### 1️⃣ Log Ingestion
- Synthetic historical logs are embedded using a sentence transformer
- Embeddings are stored in ChromaDB
- This step runs automatically on first startup

### 2️⃣ Log Analysis
- User pastes a failed log
- Vector similarity search retrieves closest incidents
- Retrieved context is injected into the prompt
- LLM generates a response based **only on this context**

---

## 🧪 Example Input
Service payment-service failed due to SSL handshake error

### Example Output
Root Cause: Expired SSL certificate
Resolution: Renew the certificate and restart the service

---

## 🌐 Live Demo
👉 **Hugging Face Space:**  
https://huggingface.co/spaces/kaustubhp/ai-log-analysis-agent

Interviewers can test the system directly using the live UI.

---

## ⚠️ Notes on Warnings
- Some LangChain components are marked deprecated but remain functional
- Telemetry warnings from ChromaDB are non-blocking
- These are expected in managed runtimes like Hugging Face Spaces

---

## 🎯 Interview Talking Points
- Why RAG over fine-tuning
- How hallucinations are avoided
- Difference between chatbot vs MCP-style system
- Dependency pinning and cloud runtime debugging
- Stateless AI system design

---

## 📌 Resume Snippet
AI Log Analysis Agent (Live Demo)
• Built a RAG-based AI system for automated failure log analysis
• Prevented hallucinations via vector-based context injection
• Deployed live on Hugging Face Spaces
• Tech: Python, Gradio, ChromaDB, Transformers, LangChain

---

## 📄 License
MIT License
