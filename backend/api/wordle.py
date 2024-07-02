"""Newsfeed API

Newsfeed routes are used to create, retrieve, and update articles."""

from fastapi import APIRouter, Depends

from ..services.wordle import WordleService
from ..models.wordle import Word


api = APIRouter(prefix="/api/wordle")
openapi_tags = {
    "name": "Wordle Solver",
    "description": "Create, delete, and retrieve Wordle solutions.",
}


# GET api/words
# Gets all words
# Expected return type: list[Word]
@api.get("", response_model=list[Word], tags=["Wordles"])
def get_words(
    wordle_service: WordleService = Depends(),
) -> list[Word]:
    """
    Get all words

    Parameters:
        wordle_service: a valid WordleService

    Returns:
        list[Word]: All `Word`s in the `Words` database table
    """
    return wordle_service.get_words()


@api.get("", response_model=list[Word], tags=["Wordle"])
def get_word(
    word: str,
    wordle_service: WordleService = Depends(),
) -> list[Word]:
    return wordle_service.get_word(word)


@api.post("", response_model=Word, tags=["Wordle"])
def create_word(
    word: Word,
    wordle_service: WordleService = Depends(),
) -> list[Word]:

    return wordle_service.create_word(word)


@api.delete("", response_model=None, tags=["Wordle"])
def delete_word(
    word: str,
    wordle_service: WordleService = Depends(),
) -> None:

    wordle_service.delete(word)
