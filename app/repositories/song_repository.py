import logging
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from app.models.song import Song

class SongRepository:
    
    logger = logging.getLogger(__name__)

    def __init__(self, session):
        self.session = session

    def get_all_songs(self):
        try:
            songs = self.session.query(Song).all()
            SongRepository.logger.info(f"Fetched {len(songs)} songs")
            
            return songs
        except SQLAlchemyError:
            self.session.rollback()
            SongRepository.logger.exception("Database error while fetching songs")
            raise   
        
    def add_song(self, song: Song) -> Song:
        try:
            self.session.add(song)
            self.session.commit()
            self.session.refresh(song)

            SongRepository.logger.info(
                "Song added successfully",
                extra={"song_id": song.id}
            )

            return song
        except IntegrityError:
            self.session.rollback()
            SongRepository.logger.exception("Error while adding song")
            raise 
        except SQLAlchemyError:
            self.session.rollback()
            SongRepository.logger.exception("Database error while adding category")
            raise
    
    def update_song(self, updated_song: Song) -> Song:
        try:
            song = self.session.merge(updated_song)
            self.session.commit()

            SongRepository.logger.info("Song updated successfully", extra={"song_id": song.id})

            return song
        except IntegrityError:
            self.session.rollback()
            SongRepository.logger.exception("Integrity error while updating song")
            raise
        except SQLAlchemyError:
            self.session.rollback()
            SongRepository.logger.exception("Database error while updating song")
            raise
    
    def delete_song(self, song_id: int):
        try:
            song = self.session.get(Song, song_id)
            if not song:
                raise ValueError("Song not found")

            self.session.delete(song)
            self.session.commit()

            SongRepository.logger.info(
                "Song deleted successfully",
                extra={"song_id": song_id}
            )

        except ValueError:
            self.session.rollback()
            SongRepository.logger.exception("Value error while deleting song")
            raise
        except IntegrityError:
            self.session.rollback()
            SongRepository.logger.exception("Integrity error while deleting song")
            raise
        except SQLAlchemyError:
            self.session.rollback()
            SongRepository.logger.exception("Database error while deleting song")
            raise

    def get_song_by_id(self, song_id):
        SongRepository.logger.debug("Fetching song by id", extra={"song-id": song_id})

        return self.session.get(Song, song_id)