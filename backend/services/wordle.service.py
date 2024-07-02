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

    def get_article_slug(self, slug: str) -> Article:
        """Gets an article by slug"""
        article = (
            self._session.query(ArticleEntity)
            .filter(ArticleEntity.slug == slug)
            .one_or_none()
        )

        # Check if result is null
        if article is None:
            raise ResourceNotFoundException(
                f"No article found with matching slug: {slug}"
            )

        return article.to_model()

    def create_article(self, subject: User, article: Article) -> Article:
        if article.id is not None:
            article.id = None

        article_entity: ArticleEntity = ArticleEntity.from_model(subject, article)

        self._session.add(article_entity)
        self._session.commit()

        return article_entity.to_model()

    def create_no_user(
        self, article: Article
    ) -> Article:  # debug only method, will be removed later
        if article.id:
            article.id = None

        article_entity: ArticleEntity = ArticleEntity.from_model_no_user(article)

        self._session.add(article_entity)
        self._session.commit()

        return article_entity.to_model()

    def update(self, article: Article) -> Article:
        obj = self._session.get(ArticleEntity, article.id)

        if obj is None:
            raise ResourceNotFoundException(
                f"No article found with matching ID: {article.id}"
            )

        # update article
        obj.slug = article.slug
        obj.title = article.title
        obj.image = article.image
        obj.body = article.body
        obj.publish_datetime = article.publish_datetime
        obj.published = article.published

        # Save changes
        self._session.commit()

        # return updated object
        return obj.to_model()

    def delete(self, slug: str) -> None:
        obj = (
            self._session.query(ArticleEntity)
            .filter(ArticleEntity.slug == slug)
            .one_or_none()
        )

        # Ensure object exists
        if obj is None:
            raise ResourceNotFoundException(
                f"No article found with matching slug: {slug}"
            )

        # Delete object and commit
        self._session.delete(obj)
        # Save changes
        self._session.commit()
