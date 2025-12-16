import logging
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from app.models.category import Category


class CategoryRepository:
    def __init__(self, session):
        self.session = session
        self.logger = logging.getLogger(__name__)

    def add_category(self, category):
        try:
            self.session.add(category)
            self.session.commit()
            self.session.refresh(category)

            self.logger.info(
                "Category added successfully",
                extra={"category_id": category.id}
            )

            return category

        except IntegrityError:
            self.session.rollback()
            self.logger.exception("Integrity error while adding category")
            raise

        except SQLAlchemyError:
            self.session.rollback()
            self.logger.exception("Database error while adding category")
            raise

    def get_by_id(self, cat_id):
        self.logger.debug("Fetching category by id", extra={"cat_id": cat_id})
        return (
            self.session
            .query(Category)
            .filter(Category.id == cat_id)
            .first()
        )
