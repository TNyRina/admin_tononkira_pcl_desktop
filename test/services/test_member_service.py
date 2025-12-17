import pytest
from app.logger import setup_logging
from test.db_test import TestingSessionLocal
from datetime import date
from app.models.member import Member

setup_logging()

@pytest.fixture
def session():
    db = TestingSessionLocal()
    yield db
    db.close()

@pytest.fixture
def member_service(session):
    from app.services.member_service import MemberService
    return MemberService(session)

def test_create_member(member_service, session):
    member = member_service.create_member(firstname="RATOVOARISON", lastname="Tsiory Ny Rina", sexe="M", date_of_birth=date(2000, 1, 7), image_url=None, address="Antanetibe")

    assert member.id is not None
    assert member.firstname == "RATOVOARISON"
    assert member.lastname == "Tsiory Ny Rina"
    assert member.sexe == "M"
    assert str(member.data_of_birth) == "2000-01-07"
    assert member.image_url is None
    assert member.address == "Antanetibe"
    member_in_db = session.query(Member).filter_by(id=member.id).first()
    assert member_in_db is not None
    assert member_in_db.firstname == "RATOVOARISON"
    assert member_in_db.lastname == "Tsiory Ny Rina"
    assert member_in_db.sexe == "M"
    assert str(member_in_db.data_of_birth) == "2000-01-07"
    assert member_in_db.image_url is None
    assert member_in_db.address == "Antanetibe"

def test_update_member(member_service, session):
    member = member_service.create_member(firstname="RATOVOARISON", lastname="Tsiory Ny Rina", sexe="M", date_of_birth=date(2000, 1, 7), image_url=None, address="Antanetibe")
    assert member.id is not None

    updated_member = member_service.update_member(member.id, firstname="RABE", lastname="Solofo", sexe="F", date_of_birth=date(1999, 12, 31), image_url="http://example.com/image.jpg", address="Antananarivo")

    assert updated_member.id == member.id
    assert updated_member.firstname == "RABE"
    assert updated_member.lastname == "Solofo"
    assert updated_member.sexe == "F"
    assert str(updated_member.data_of_birth) == "1999-12-31"
    assert updated_member.image_url == "http://example.com/image.jpg"
    assert updated_member.address == "Antananarivo"

    member_in_db = session.query(Member).filter_by(id=member.id).first()
    assert member_in_db is not None
    assert member_in_db.firstname == "RABE"
    assert member_in_db.lastname == "Solofo"
    assert member_in_db.sexe == "F"
    assert str(member_in_db.data_of_birth) == "1999-12-31"
    assert member_in_db.image_url == "http://example.com/image.jpg"
    assert member_in_db.address == "Antananarivo"