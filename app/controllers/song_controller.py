from app.exceptions.business_exception import ValidationError
from app.services.song_service import SongService


class SongController:
    def __init__(self, session):
        self.service = SongService(session)

    def add_song(self, title, categories, verse, author=None, composer=None, description=None, refrain=None, release=None):
        verse_string = ":".join(verse)

        try:
            self.service.create_song(title=title, 
            release=release, 
            author=author, 
            composer=composer, 
            description=description, 
            verse=verse_string, 
            refrain=refrain, 
            categories=categories)
        except ValidationError :
            raise 
    
    def get_songs(self):
        try: 
            return self.service.songs()
        except Exception: 
            raise

    def delete_song(self, id): 
        try: 
            self.service.delete_song(id)
        except Exception:
            raise