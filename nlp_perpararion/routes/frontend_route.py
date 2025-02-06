
from nlp_perpararion.schemas.text_base import TextData
from fastapi.responses import HTMLResponse
from nlp_perpararion.clean_text.clear_text import clear_text
from fastapi import APIRouter

frontend_route = APIRouter()

@frontend_route.get("/", response_class=HTMLResponse)
async def serve_frontend():
    with open("nlp_perparation_fe/index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())