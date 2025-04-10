from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Ticket(BaseModel):
    description: str

@app.post("/analyze")
async def analyze_ticket(ticket: Ticket):
    # Placeholder for Azure AI response (to be integrated)
    command_suggestion = f"Example command for: {ticket.description}"
    return {
        "original_ticket": ticket.description,
        "suggested_command": command_suggestion
    }