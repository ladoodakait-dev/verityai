from fastapi import FastAPI
from pydantic import BaseModel
import train

app = FastAPI(title="Verity AI")

# This is what the user sends us
class Question(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Verity AI is running! Send math questions to /solve"}

@app.post("/solve")
def solve(question: Question):
    result = train.solve_math(question.text)
    return {"question": question.text, "answer": result}
