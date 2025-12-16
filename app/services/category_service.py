from app.models.category import Category
from app.models.song import Song
from app.repositories.category_repository import CategoryRepository

class CategoryService:
    def __init__(self, session):
        self.session = session

    def create_category(self, name):
        new_category = Category(name=name)

        cat_repo = CategoryRepository(self.session)

        try:
            return cat_repo.add_category(new_category)
        finally:
            pass
            self.session.close()