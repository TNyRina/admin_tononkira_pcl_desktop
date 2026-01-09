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
    
    def update_category(self, id, name):
        try:
            service = CategoryService(self.session)
            service.update_category(id=id, name=name)
        except ValidationError:
            raise
    
    def delete_category(self, id):
        try:
            service = CategoryService(self.session)
            service.delete_category(id)
        except ValidationError:
            raise

    def get_categories(self):
        try:
            service = CategoryService(self.session)
            return service.categories()
        except ValidationError:
            raise