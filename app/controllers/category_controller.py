from app.controllers.controller import Controller
from app.exceptions.business_exception import ValidationError
from app.services.category_service import CategoryService

class CategoryController(Controller):
    def __init__(self, session):
        super().__init__()
        self.service = CategoryService(session)

    def add_category(self, category_name: str):
        try:
            self.service.create_category(category_name)
        except ValidationError:
            raise
    
    def update_category(self, id, name):
        try:
            self.service.update_category(id=id, name=name)
        except ValidationError:
            raise
    
    def delete_category(self, id):
        try:
            self.service.delete_category(id)
        except ValidationError:
            raise

    def get_categories(self):
        try:
            return self.service.categories()
        except Exception:
            raise