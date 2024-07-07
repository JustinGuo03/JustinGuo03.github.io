"""Definition of SQLAlchemy table-backed object mapping entity for Articles in Newsfeed."""

from sqlalchemy import Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .entity_base import EntityBase

from typing import Self
from backend.models import wordle

class WordleEntity(EntityBase):
    __tablename__ = "Wordles"

    # unique ID for word
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    # unique word
    word: Mapped[String] = mapped_column(String, nullable=False, default="")

    # first letter
    letter1: Mapped[String] = mapped_column(String, nullable=False, default="")

    # second letter
    letter2: Mapped[String] = mapped_column(String, nullable=False, default="")

    # third letter
    letter3: Mapped[String] = mapped_column(String, nullable=False, default="")

    # fourth letter
    letter4: Mapped[String] = mapped_column(String, nullable=False, default="")

    # fifth letter
    letter5: Mapped[String] = mapped_column(String, nullable=False, default="")

    score: Mapped[int] = mapped_column(int, nullable=False, default="")

 
    @classmethod
    def from_model(cls, wordle: wordle.Word) -> Self:
        """
        Class method that converts n `Word` model into a `WordleEntity`

        Parameters:
            - model (Article): Model to convert into an entity
        Returns:
            ArticleEntity: Entity created from model (not yet persisted)
        """
        return cls(
            id=wordle.id,
            letter1=wordle.letter1,
            letter2=wordle.letter2,
            letter3=wordle.letter3,
            letter4=wordle.letter4,
            letter5=wordle.letter5,
            score=wordle.score
        )

    def to_model(self) -> wordle.Word:
        """
        Converts a `WordleENtity` object into a 'Word` model object

        Returns:
            Article: `Article` object from the entity
        """
        return wordle.Word(
            id=self.id,
            letter1=self.letter1,
            letter2=self.letter2,
            letter3=self.letter3,
            letter4=self.letter4,
            letter5=self.letter5,
            score=self.score,
        )
