from app.models.category import Category
from app.models.song import Song
from app.repositories.song_repository import SongRepository

class CategoryService:
    def __init__(self, session):
        self.session = session

    def create_category(self, name):
        new_category = Category(name=name)

        cat_repo = SongRepository(self.session)

        return cat_repo.add_song(new_category)