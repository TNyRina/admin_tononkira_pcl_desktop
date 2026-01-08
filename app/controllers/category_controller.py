from app.exceptions.business_exception import ValidationError
from app.services.category_service import CategoryService

class CategoryController:
    def __init__(self, session):
        self.session = session

    def add_category(self, category_name: str):
        try:
            service = CategoryService(self.session)
            service.create_category(category_name)
        except ValidationError:
            raise
        