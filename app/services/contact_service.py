from app.models.contact import Contact
from app.repositories.contact_repository import ContactRepository


class ContactService:
    def __init__(self, session):
        self.session = session
    
    def contacts(self):
        return ContactRepository(self.session).get_all_contacts()

    def create_contact(self, contact:str, owner: int):
        new_contact = Contact(
            contact=contact,
            owner=owner
        )
        return ContactRepository(self.session).add_contact(new_contact)
    
    def update_contact(self, id: int, contact: str = None, owner: int = None):
        repository = ContactRepository(self.session)
        contact_obj = repository.get_contact_by_id(id)

        contact_obj.contact = contact
        contact_obj.owner = owner

        return repository.update_contact(contact_obj)
    
    def delete_contact(self, id: int):
        ContactRepository(self.session).delete_contact(id)