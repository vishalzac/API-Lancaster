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

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are a helpful university assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5
        )

        answer = response.choices[0].message.content

        return {
            "question": question,
            "answer": answer
        }

    except Exception as e:
        return {
            "error": "AI service failed",
            "details": str(e)
        }
