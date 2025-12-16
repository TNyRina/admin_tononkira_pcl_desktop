from app.models.category import Category
from app.services.category_service import CategoryService
from test.db_test import TestingSessionLocal
from app.logger import setup_logging

def test_create_category():
    setup_logging()
    session = TestingSessionLocal()

    cat_service = CategoryService(session)
    cat1 = cat_service.create_category(name="Category 1")

    assert cat1.id is not None
    assert cat1.name == "Category 1"
    cat_in_db = session.query(Category).filter_by(id=cat1.id).first()
    assert cat_in_db is not None