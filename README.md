---
title: AI Log Analysis Agent
emoji: 🧠
sdk: gradio
app_file: app.py
---

# AI Log Analysis Agent

**Live Demo:** https://huggingface.co/spaces/kaustubhp/ai-log-analysis-agent

## What It Is
An **AI-powered log analysis system** that identifies the **root cause and resolution** of failures using **Retrieval-Augmented Generation (RAG)**.

The LLM never answers directly — it retrieves relevant historical incidents from a **vector database** first, preventing hallucinations and enabling reliable reasoning.

---

## Why It Matters
- Automates repetitive log analysis
- Prevents LLM hallucination
- Demonstrates MCP-style, tool-driven AI systems
- Designed as a real-world, deployable AI service

---

## How It Works
1. Historical logs are embedded and stored in a vector database  
2. New logs trigger semantic similarity search  
3. Retrieved context is injected into the LLM prompt  
4. The LLM outputs root cause and resolution  

---

## Tech Stack
- Python
- Gradio
- ChromaDB (Vector DB)
- Sentence Transformers
- Transformers (FLAN-T5)
- LangChain (Community)
- Hugging Face Spaces

---

## Example
**Input**
Service payment-service failed due to SSL handshake error
**Output**
Root Cause: Expired SSL certificate
Resolution: Renew the certificate and restart the service

---

## Resume Snippet
AI Log Analysis Agent (Live Demo)
• Built a RAG-based AI system for automated failure analysis
• Prevented hallucinations using vector-based context injection
• Deployed live on Hugging Face Spaces