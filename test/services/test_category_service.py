import pytest
from app.models.category import Category
from app.services.category_service import CategoryService
from test.db_test import TestingSessionLocal
from app.logger import setup_logging

setup_logging()

# Fixture pour la session
@pytest.fixture
def session():
    db = TestingSessionLocal()
    yield db
    db.close()  

# Fixture pour le service
@pytest.fixture
def category_service(session):
    return CategoryService(session)

def test_create_category(category_service, session):
    cat = category_service.create_category(name="Category 1")

    assert cat.id is not None
    assert cat.name == "Category 1"

    # Vérification dans la DB
    cat_in_db = session.query(Category).filter_by(id=cat.id).first()
    assert cat_in_db is not None
    assert cat_in_db.name == "Category 1"

def test_update_category(category_service, session):
    # Création initiale
    cat = category_service.create_category(name="Category 1")
    assert cat.id is not None

    # Mise à jour
    updated_cat = category_service.update_category(cat.id, "updated name")
    assert updated_cat.id == cat.id
    assert updated_cat.name == "updated name"

    # Vérification dans la DB
    cat_in_db = session.query(Category).filter_by(id=cat.id).first()
    assert cat_in_db is not None
    assert cat_in_db.name == "updated name"
