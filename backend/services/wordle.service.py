from typing import Counter
from fastapi import Depends

# from pytest import Session

from sqlalchemy import select
from sqlalchemy import desc
from sqlalchemy.orm import Session
from backend.database import db_session
from backend.entities.wordle_entity import WordleEntity
import re
import pandas as pd
import numpy as np

from ..models.wordle import Word


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
    
    def delete_word(self, word: str) -> None:
        obj = (
            self._session.query(WordleEntity)
            .filter(WordleEntity.word == word)
            .one_or_none()
        )
        # Delete object and commit
        self._session.delete(obj)
        # Save changes
        self._session.commit()

    def create_default_table(self) -> list[Word]:
        with open('answers.txt') as file:
            possible_answers = file.readlines()

        list_possible_answers = sorted([re.sub(r'[^A-Z]', '', t.upper()) for t in possible_answers[0].split(',')])
        
        arr_words = np.array([list(w) for w in list_possible_answers])
        df_words = pd.DataFrame(data=arr_words,
                                columns=[f'letter_{i+1}' for i in range(5)])
        df_words['word'] = list_possible_answers

        #count letter frequency by index
        letter_frequency = []
        for i in range(5):
            letter_frequency.append(Counter(df_words[f'letter_{i+1}']))

        def findWordFrequency(word):
                total = 0
                for i, v in enumerate(word):
                    total += letter_frequency[i][v.upper()]
                return total

        word_frequency = {}
        for word in list_possible_answers:
            word_frequency[word] = findWordFrequency(word)
        
        allwords = []

        for i, v in enumerate(word_frequency):
            wordle_entity: WordleEntity = WordleEntity()
            wordle_entity.word = v
            wordle_entity.id = i
            wordle_entity.letter1 = v[0]
            wordle_entity.letter2 = v[1]
            wordle_entity.letter3 = v[2]
            wordle_entity.letter4 = v[3]
            wordle_entity.letter5 = v[4]
            wordle_entity.score = word_frequency[v]

            self._session.add(wordle_entity)
            self._session.commit()

            allwords.append(wordle_entity)
        
        return allwords
        
        
