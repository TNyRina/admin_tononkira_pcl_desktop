import logging
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from app.exceptions.technical_exception import DatabaseError
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
        except SQLAlchemyError as e:
            self.session.rollback()
            CategoryRepository.logger.exception("Database error while fetching categories")
            raise DatabaseError("DB_ERROR") from e       

    def add_category(self, category: Category) -> Category:
        try:
            self.session.add(category)
            self.session.commit()
            self.session.refresh(category)

            self.logger.info(
                "Category added successfully",
                extra={"category_id": category.id}
            )
            return category

        except IntegrityError as e:
            self.session.rollback()
            self.logger.exception("IntegrityError while adding category")
            raise DatabaseError("DB_INTEGRITY_ERROR") from e

        except SQLAlchemyError as e:
            self.session.rollback()
            self.logger.exception("SQLAlchemyError while adding category")
            raise DatabaseError("DB_ERROR") from e
    
    def is_category_exists(self, name: str) -> bool:
        try:
            exists = self.session.query(
                self.session.query(Category).filter_by(name=name).exists()
            ).scalar()

            CategoryRepository.logger.info(
                "Checked category existence",
                extra={"category_name": name, "exists": exists}
            )

            return exists
        except SQLAlchemyError as e:
            CategoryRepository.logger.exception("Database error while checking category existence")
            raise DatabaseError("DB_ERROR") from e
     

    def update_category(self, updated_category: Category) -> Category:  
        try:
            category = self.session.merge(updated_category)
            self.session.commit()

            CategoryRepository.logger.info(
                "Category updated successfully",
                extra={"category_id": category.id}
            )

            return category
        except IntegrityError as e:
            self.session.rollback()
            CategoryRepository.logger.exception("Integrity error while updating category")
            raise DatabaseError("DB_INTEGRITY_ERROR") from e
        except SQLAlchemyError:
            self.session.rollback()
            CategoryRepository.logger.exception("Database error while updating category")
            raise DatabaseError("DB_ERROR") from e

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
        except SQLAlchemyError as e:
            self.session.rollback()
            CategoryRepository.logger.exception("Database error while deleting category")
            raise DatabaseError("DB_ERROR") from e
    

    def get_category_by_id(self, cat_id):
        CategoryRepository.logger.debug("Fetching category by id", extra={"cat_id": cat_id})

        return self.session.get(Category, cat_id)
