import logging
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from app.models.category import Category


class CategoryRepository:
    logger = logging.getLogger(__name__)

    def __init__(self, session):
        self.session = session    

    def get_all_categories(self):
        try:
            categories = self.session.query(Category).all()
            CategoryRepository.logger.info(f"Fetched {len(categories)} categories")

            return categories
        except SQLAlchemyError:
            self.session.rollback()
            CategoryRepository.logger.exception("Database error while fetching categories")
            raise       

    def add_category(self, category: Category) -> Category:
        try:
            self.session.add(category)
            self.session.commit()
            self.session.refresh(category)

            CategoryRepository.logger.info(
                "Category added successfully",
                extra={"category_id": category.id}
            )

            return category

        except IntegrityError:
            self.session.rollback()
            CategoryRepository.logger.exception("Integrity error while adding category")
            raise

        except SQLAlchemyError:
            self.session.rollback()
            CategoryRepository.logger.exception("Database error while adding category")
            raise

    def update_category(self, updated_category: Category) -> Category:  
        try:
            category = self.session.merge(updated_category)
            self.session.commit()

            CategoryRepository.logger.info(
                "Category updated successfully",
                extra={"category_id": category.id}
            )

            return category
        except IntegrityError:
            self.session.rollback()
            CategoryRepository.logger.exception("Integrity error while updating category")
            raise
        except SQLAlchemyError:
            self.session.rollback()
            CategoryRepository.logger.exception("Database error while updating category")
            raise

    def delete_category(self, category_id: int):
        try:
            category = self.session.get(Category, category_id)
            if not category:
                raise ValueError("Category not found")

            self.session.delete(category)
            self.session.commit()

            CategoryRepository.logger.info(
                "Category deleted successfully",
                extra={"category_id": category_id}
            )

        except ValueError:
            self.session.rollback()
            CategoryRepository.logger.exception("Value error while deleting category")
            raise
        except IntegrityError:
            self.session.rollback()
            CategoryRepository.logger.exception("Integrity error while deleting category")
            raise
        except SQLAlchemyError:
            self.session.rollback()
            CategoryRepository.logger.exception("Database error while deleting category")
            raise
    

    def get_category_by_id(self, cat_id):
        CategoryRepository.logger.debug("Fetching category by id", extra={"cat_id": cat_id})

        return self.session.get(Category, cat_id)
