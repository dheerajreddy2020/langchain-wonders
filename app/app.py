import os
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from fastapi.middleware.cors import CORSMiddleware


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI with GPT-4O Mini
openai_model = ChatOpenAI(model="gpt-4o-mini")
conversation = ConversationChain(llm=openai_model)

app = FastAPI()

# Add CORS middleware
origins = [
    "http://localhost:3000",
    "http://localhost:8001",  # Adjust as necessary
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

if __name__ == "__main__":
    uvicorn.run("app:app", proxy_headers=True, host='0.0.0.0', port=8000, reload=False)


class ChatRequest(BaseModel):
    user_input: str

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        user_input = request.user_input
        response = conversation.predict(input=user_input)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
