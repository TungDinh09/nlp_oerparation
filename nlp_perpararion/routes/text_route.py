
from nlp_perpararion.schemas.text_base import TextData
from nlp_perpararion.clean_text.clear_text import clear_text
from fastapi import APIRouter

text_route = APIRouter()

@text_route.post("/clean")
async def clean_text(data: TextData):
    if data.source.lower() == "coursera":
        cleaned_text = await clear_text.clean_coursera(data.text)
    elif data.source.lower() == "youtube":
        cleaned_text = await clear_text.clean_youtube(data.text)
    else:
        return {"error": "Invalid source. Choose 'coursera' or 'youtube'."}
    
    return {"cleaned_text": cleaned_text}