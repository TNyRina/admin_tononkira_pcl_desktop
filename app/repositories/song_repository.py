import logging
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

class SongRepository:
    def __init__(self, session):
        self.session = session
        self.logger = logging.getLogger(__name__)

    def add_song(self, song):
        try:
            self.session.add(song)
            self.session.commit()
            self.session.refresh(song)

            self.logger.info(
                "Song added successfully",
                extra={"song_id": song.id}
            )

            return song
        except IntegrityError:
            self.session.rollback()
            self.logger.exception("Error while adding song")
            raise 
        except SQLAlchemyError:
            self.session.rollback()
            self.logger.exception("Database error while adding category")
            raise
