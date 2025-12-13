from app.services.category_service import CategoryService
from test.db_test import TestingSessionLocal
from app.services.song_service import SongService
from app.models.song import Song

def test_create_song():

    session = TestingSessionLocal()
    service = SongService(session)

    cat_service = CategoryService(session)
    cat1 = cat_service.create_category(name="Category 1")
    cat2 = cat_service.create_category(name="Category 2")
    catIds = [cat1.id, cat2.id]

    song = service.create_song(
        title="Test Song",
        release="2024-01-01",
        author="Test Author",
        composer="Test Composer",
        description="This is a test song.",
        verse="This is a test verse.",
        refrain="This is a test refrain.",
        categories=catIds
    )

    assert song.id is not None
    assert song.title == "Test Song"    
    assert song.author == "Test Author"
    assert song.composer == "Test Composer"
    assert song.description == "This is a test song."
    assert song.verse == "This is a test verse."
    assert song.refrain == "This is a test refrain."
    assert len(song.categories) == 2

    song_in_db = session.query(Song).filter_by(id=song.id).first()
    assert song_in_db is not None

    
