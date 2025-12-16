from app.models.song import Song
from app.repositories.category_repository import CategoryRepository
from app.repositories.song_repository import SongRepository

class SongService:
    def __init__(self, session):
        self.session = session

    def songs(self):
        return SongRepository(self.session).get_all_songs()

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
            category = cat_repo.get_category_by_id(cat_id)

            new_song.categories.append(category)

        return SongRepository(self.session).add_song(new_song)
    
    def update_song(self, id, title, release, author, composer, description, verse, refrain, categories):
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

    def delete_song(self, id: int):
        SongRepository(self.session).delete_song(id)