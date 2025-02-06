import re
from pydantic import BaseModel

class ClearText:

    async def clean_coursera(self, text: str) -> str:
        pattern = r"Play video starting at \d{0,2}:\d{0,2}:\d{0,2} and follow transcript\d{0,2}:\d{0,2}"
        return re.sub(pattern, "", text).strip().replace("\n", " ")
    async def clean_youtube(self, text: str) -> str:
        pattern = r"[\d{0,2}:|]\d{0,2}:\d{0,2}"  # Ví dụ: Loại bỏ timestamp dạng [00:12]
        return re.sub(pattern, "", text).strip().replace("\n", " ")
    
clear_text = ClearText()