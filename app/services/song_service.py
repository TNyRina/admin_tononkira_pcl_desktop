from app.exceptions.business_exception import ValidationError
from app.exceptions.technical_exception import DatabaseError
from app.models.song import Song
from app.repositories.category_repository import CategoryRepository
from app.repositories.song_repository import SongRepository

class SongService:
    def __init__(self, session):
        self.session = session

    def songs(self):
        return SongRepository(self.session).get_all_songs()

    def create_song(self, title, categories, verse, author=None, composer=None, description=None, refrain=None, release=None):
        try:
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
                category = cat_repo.get_category_by_id(cat_id)

                new_song.categories.append(category)

            return SongRepository(self.session).add_song(new_song)
        except DatabaseError as e:
            raise ValidationError("Failed to create song", code="CREATE_FAILED") from e
    
    def update_song(self, id, title, release, author, composer, description, verse, refrain, categories):
        try:
            repository = SongRepository(self.session)
            song = repository.get_song_by_id(id)
            song.title = title
            song.release = release
            song.author = author
            song.composer = composer
            song.description = description
            song.verse = verse
            song.refrain = refrain

            song.categories = []
            for cat_id in categories:
                cat_repo = CategoryRepository(self.session)
                category = cat_repo.get_category_by_id(cat_id)
                if not category:
                    raise ValueError(f"Category id {cat_id} not found")
                song.categories.append(category)

            return repository.update_song(song)
        except DatabaseError as e:
            raise ValidationError("Failed to update song", code="UPDATE_FAILED") from e

    def delete_song(self, id: int):
        try:
            SongRepository(self.session).delete_song(id)
        except DatabaseError as e:
            raise ValidationError("Failed to delete song", code="DELETE_FAILED") from e