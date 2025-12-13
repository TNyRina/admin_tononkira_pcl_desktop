class SongRepository:
    def __init__(self, session):
        self.session = session

    def add_song(self, song):
        self.session.add(song)
        self.session.commit()
        self.session.refresh(song)
        self.session.close()

        return song
