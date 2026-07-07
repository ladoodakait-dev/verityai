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

# This lets Render tell our app which port to use
if __name__ == "__main__":
    import os
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
