from openai import OpenAI
import os
from dotenv import load_dotenv

# Load .env file BEFORE reading key
load_dotenv()

print("start")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_ai(question: str):
    try:
        prompt = f"""
You are a Lancaster University study assistant.
Answer the question clearly and simply.
Then provide one useful study tip.

Question:
{question}
"""

        response = client.responses.create(
            model="gpt-5-nano",
            input=prompt,
        )
        answer = response.output_text  # NEW way to extract text

        return {
            "question": question,
            "answer": answer
        }

    except Exception as e:
        return {
            "error": "AI service failed",
            "details": str(e)
        }

