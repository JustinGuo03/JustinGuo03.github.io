from pydantic import BaseModel

class Word(BaseModel):
    id: int
    word: str
    letter1: str
    letter2: str
    letter3: str
    letter4: str
    letter5: str
    score: int
