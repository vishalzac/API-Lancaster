# Lancaster AI Student Assistant API

## Overview

This project is a lightweight backend service built using FastAPI that uses Artificial Intelligence to enhance the student learning journey at Lancaster University. The service provides a simple API that allows students to ask academic questions and receive AI-generated explanations along with helpful study advice.

The application is designed as a clean backend-only service with a focus on maintainability, clarity, and simplicity. It demonstrates how AI can be integrated into a backend system using a real large language model API while maintaining good API design and error handling practices.

---

## How AI is Used

The service integrates with the OpenAI API to process student questions. When a request is sent to the `/feature` endpoint, the API constructs a prompt and sends it to the AI model. The model is instructed to act as a university study assistant and return a clear explanation along with one study tip.

The AI is not used as a chatbot, but as a backend capability that enhances responses programmatically. This demonstrates a realistic enterprise use of AI as part of backend business logic rather than just a UI feature.

---

## How This Improves the Student Journey

Students often struggle with:
- Understanding complex concepts
- Knowing how to study effectively
- Identifying what to learn next

This service helps by:
- Providing clear, simplified explanations
- Offering concise study advice
- Encouraging structured independent learning
- Supporting students outside classroom hours

It could easily be extended into support tools such as:
- Assignment helpers  
- Lecture summaries  
- Academic advising systems  
- Revision planning tools  

---

## API Endpoints

### 1. Health Check

```
GET /health
```

Response:
```json
{
  "status": "ok",
  "service": "Lancaster AI Student Assistant"
}
```

---

### 2. AI Feature

```
POST /feature
```

Request example:

```json
{
  "question": "Explain machine learning simply"
}
```

Response example:

```json
{
  "question": "Explain machine learning simply",
  "answer": "Machine learning is when a computer learns patterns from data..."
}
```

---

## Running the Project Locally

### Requirements
- Python 3.9+
- An OpenAI API key

---

### Installation

1. Clone or extract the project
2. Install dependencies:

```
pip install -r requirements.txt
```

---

### Environment Setup

Create a `.env` file in the project root and add:

```
OPENAI_API_KEY=your_api_key_here
```

---

### Run the API

```
uvicorn app:app --reload
```

---

### Open Swagger UI

Visit:

```
http://127.0.0.1:8000/docs
```

---

## Running Unit Tests

Run:

```
pytest
```

---

## Project Structure

```
lancaster-ai-student-backend
├── app.py
├── ai_service.py
├── test_ai.py
├── requirements.txt
├── README.md
└── .env
```

---

## Future Enhancements

- Authentication
- Rate limiting
- Database persistence
- Personalised study suggestions
- Course-specific assistants
- Deployment to cloud infrastructure (Azure / AWS)

---

## Notes

This project is intentionally designed to be small, clear, and testable within a short timeframe. The focus is on backend quality, API cleanliness, and practical AI usage rather than creating a production system.
