from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import logging
from ai_service import ask_ai

# Load environment variables
load_dotenv()

# Logging setup
logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title="Lancaster AI Student Assistant",
    description="AI backend to enhance student learning journey",
    version="1.0"
)

# Request model
class StudentRequest(BaseModel):
    question: str

# Health check endpoint
@app.get("/health")
def health():
    return {"status": "ok", "service": "Lancaster AI Student Assistant"}

# AI Feature endpoint
@app.post("/feature")
def feature(request: StudentRequest):
    logging.info("Received question")
    response = ask_ai(request.question)
    return response
