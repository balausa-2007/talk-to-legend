import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
from rag import retrieve_context, build_vectorstore
from personas import get_persona_prompt, get_all_characters

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class ChatRequest(BaseModel):
    message: str
    character: str

@app.on_event("startup")
async def startup_event():
    build_vectorstore()

@app.get("/characters")
def get_characters():
    return JSONResponse(content=get_all_characters(), media_type="application/json; charset=utf-8")
@app.post("/chat")
def chat(request: ChatRequest):
    
    context = retrieve_context(request.message, request.character, k=5)
    
    persona_prompt = get_persona_prompt(request.character)
    
    
    system_prompt = f"""{persona_prompt}

CRITICAL: The following is your knowledge base. Use ONLY this information to answer factual questions about yourself (children, family, dates, events). NEVER invent facts.
If the answer is not in the knowledge base, say "I don't recall the details clearly."

YOUR KNOWLEDGE BASE:
{context}

Remember: respond in the same language as the user's message.""" 
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": request.message}
        ],
        max_tokens=1024,
        temperature=0.7
    )

    return JSONResponse(
        content={
            "response": response.choices[0].message.content,
            "character": request.character
        },
        media_type="application/json; charset=utf-8"
    )

@app.get("/")
def root():
    return {"message": "Talk to a Legend API is running!"}