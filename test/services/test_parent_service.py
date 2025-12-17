from datetime import date
import pytest
from app.logger import setup_logging
from app.models.member_parent import MemberParent
from app.models.parent import Parent
from test.db_test import TestingSessionLocal

setup_logging()
@pytest.fixture
def session():
    db = TestingSessionLocal()
    yield db
    db.close()

@pytest.fixture
def parent_service(session):
    from app.services.parent_service import ParentService
    return ParentService(session)

@pytest.fixture
def member_service(session):
    from app.services.member_service import MemberService
    return MemberService(session)

def test_create_parent(member_service, parent_service, session):
    member = member_service.create_member(firstname="RATOVOARISON", lastname="Tsiory Ny Rina", sexe="M", date_of_birth=date(2000, 1, 7), image_url=None, address="Antanetibe")

    parent = parent_service.create_parent(name="RATOVOSON Charlot", role="dad", member_id=member.id)

    assert parent.id is not None
    assert parent.name == "RATOVOSON Charlot"
    parent_in_db = session.query(Parent).filter_by(id=parent.id).first()
    assert parent_in_db is not None
    assert parent_in_db.name == "RATOVOSON Charlot"

    link_in_db = session.query(MemberParent).filter_by(member_id=member.id, parent_id=parent.id).first()
    assert link_in_db is not None
    assert link_in_db.role == "dad"
    assert link_in_db.member_id == member.id
    assert link_in_db.parent_id == parent.id

def test_update_parent(member_service, parent_service, session):
    member = member_service.create_member(firstname="RATOVOARISON", lastname="Tsiory Ny Rina", sexe="M", date_of_birth=date(2000, 1, 7), image_url=None, address="Antanetibe")

    parent = parent_service.create_parent(name="RATOVOSON Charlot", role="dad", member_id=member.id)

    updated_parent = parent_service.update_parent(parent.id, name="RATOVOSON Charles", address="Antananarivo")

    assert updated_parent.id == parent.id
    assert updated_parent.name == "RATOVOSON Charles"
    assert updated_parent.address == "Antananarivo"

    parent_in_db = session.query(Parent).filter_by(id=parent.id).first()
    assert parent_in_db is not None
    assert parent_in_db.name == "RATOVOSON Charles"
    assert parent_in_db.address == "Antananarivo"

def test_update_link_role(member_service, parent_service, session):
    member = member_service.create_member(firstname="RATOVOARISON", lastname="Tsiory Ny Rina", sexe="M", date_of_birth=date(2000, 1, 7), image_url=None, address="Antanetibe")

    parent = parent_service.create_parent(name="RATOVOSON Charlot", role="dad", member_id=member.id)

    updated_link = parent_service.update_link_role(member.id, parent.id, role="guardian")

    assert updated_link.member_id == member.id
    assert updated_link.parent_id == parent.id
    assert updated_link.role == "guardian"

    link_in_db = session.query(MemberParent).filter_by(member_id=member.id, parent_id=parent.id).first()
    assert link_in_db is not None
    assert link_in_db.role == "guardian"

def test_delete_parent(member_service, parent_service, session):
    member = member_service.create_member(firstname="RATOVOARISON", lastname="Tsiory Ny Rina", sexe="M", date_of_birth=date(2000, 1, 7), image_url=None, address="Antanetibe")

    parent = parent_service.create_parent(name="RATOVOSON Charlot", role="dad", member_id=member.id)

    parent_service.delete_parent(parent.id)

    parent_in_db = session.query(Parent).filter_by(id=parent.id).first()
    assert parent_in_db is None

    link_in_db = session.query(MemberParent).filter_by(member_id=member.id, parent_id=parent.id).first()
    assert link_in_db is None