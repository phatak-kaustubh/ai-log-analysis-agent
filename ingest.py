
import csv
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

DATA_PATH = "data/sample_logs.csv"
DB_PATH = "chroma_db"

def ingest_logs():
    documents = []

    with open(DATA_PATH, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            content = (
                f"Service: {row['service']}\n"
                f"Region: {row['region']}\n"
                f"Error: {row['error_message']}\n"
                f"Root Cause: {row['root_cause']}\n"
                f"Resolution: {row['resolution']}"
            )
            documents.append(content)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    Chroma.from_texts(
        texts=documents,
        embedding=embeddings,
        persist_directory=DB_PATH
    )

    print("✅ Logs ingested into vector database")

if __name__ == "__main__":
    ingest_logs()
