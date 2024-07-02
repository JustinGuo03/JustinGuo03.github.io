from fastapi import Depends

# from pytest import Session

from sqlalchemy import select
from sqlalchemy import desc
from sqlalchemy.orm import Session
from backend.database import db_session
from backend.entities.wordle_entity import WordleEntity

from ..models.wordle import Word

from sqlalchemy import select


class WordleService:
    def __init__(self, session: Session = Depends(db_session)):
        self._session = session

    def get_words(self) -> list[Word]:
        """
        Retrieves all currently published Articles for newsfeed display

        Returns:
            list[Article]: All published articles in the database.
        """
        entities = (
            self._session.query(WordleEntity)
            .order_by(desc(Word.score))
            .all()
        )

        return [entity.to_model() for entity in entities]

    def get_word(self) -> Word:

        entities = (
            self._session.query(WordleEntity)
            .order_by(desc(Word.score))
            .first()
        )

        return [entity.to_model() for entity in entities]

    def create_word(self, word: Word) -> Word:
        wordle_entity: WordleEntity = WordleEntity.from_model(word)

        self._session.add(wordle_entity)
        self._session.commit()

        return wordle_entity.to_model()
    
    def delete_word(self, word: Word) -> None:
        obj = (
            self._session.query(WordleEntity)
            .filter(WordleEntity.word == word)
            .one_or_none()
        )
        # Delete object and commit
        self._session.delete(obj)
        # Save changes
        self._session.commit()