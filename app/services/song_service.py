from app.models.song import Song
from app.repositories.category_repository import CategoryRepository
from app.repositories.song_repository import SongRepository

class SongService:
    def __init__(self, session):
        self.session = session

    def create_song(self, title, release, author, composer, description, verse, refrain, categories):
        new_song = Song(
            title=title,
            release=release,
            author=author,
            composer=composer,
            description=description,
            verse=verse,
            refrain=refrain
        )

        for cat_id in categories:
            cat_repo = CategoryRepository(self.session)
            category = cat_repo.get_by_id(cat_id)

            new_song.categories.append(category)
                
        song_repository = SongRepository(self.session)

        try:
            return song_repository.add_song(new_song)
        finally:
            pass
            self.session.close()