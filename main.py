from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai

app = FastAPI()

# OpenAI API key (замени на свой)
OPENAI_API_KEY = "your-api-key"
openai.api_key = OPENAI_API_KEY

class DecisionRequest(BaseModel):
    problem_description: str

@app.post("/analyze")
async def analyze_decision(request: DecisionRequest):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "Ты помощник для принятия сложных решений."},
                {"role": "user", "content": request.problem_description}
            ]
        )
        return {"response": response["choices"][0]["message"]["content"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Запуск сервера: uvicorn filename:app --reload