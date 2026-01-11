
import gradio as gr
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from transformers import pipeline

DB_PATH = "chroma_db"

# Load embeddings + vector DB
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = Chroma(
    persist_directory=DB_PATH,
    embedding_function=embeddings
)

# Lightweight local model (good for demo)
llm = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_new_tokens=200
)

def analyze_log(log_text):
    if not log_text.strip():
        return "❌ Please provide a log message."

    # Step 1: Retrieve similar incidents
    results = vector_db.similarity_search(log_text, k=2)

    if not results:
        return "⚠️ No similar historical incidents found."

    context = "\n\n".join([doc.page_content for doc in results])

    # Step 2: Construct prompt
    prompt = f"""
Task: Analyze the log and identify the root cause and resolution.

Context:
{context}

Log:
{log_text}

Answer concisely:
- Root Cause:
- Resolution:
"""


    # Step 3: Generate response
    response = llm(prompt)[0]["generated_text"]

    return response


# Gradio UI
demo = gr.Interface(
    fn=analyze_log,
    inputs=gr.Textbox(lines=6, label="Paste Failed Log"),
    outputs=gr.Textbox(label="AI Analysis",lines=20),
    title="AI Log Analysis Agent",
    description="RAG-based log analysis using Vector DB + LLM"
)

if __name__ == "__main__":
    demo.launch()
