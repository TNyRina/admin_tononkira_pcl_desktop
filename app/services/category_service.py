from app.models.category import Category
from app.models.song import Song
from app.repositories.category_repository import CategoryRepository

class CategoryService:
    def __init__(self, session):
        self.session = session

    def categories(self):
        return CategoryRepository(self.session).get_all_categories()

    def create_category(self, name: str) -> Category:
        new_category = Category(name=name)

        return CategoryRepository(self.session).add_category(new_category)
    
    def update_category(self, id: int, name: str) -> Category:
        repository = CategoryRepository(self.session)
        category = repository.get_category_by_id(id)
        category.name = name

        return repository.update_category(category)

    def delete_category(self, id: int):
        CategoryRepository(self.session).delete_category(id)