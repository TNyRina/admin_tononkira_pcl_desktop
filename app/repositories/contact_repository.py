import logging
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from app.models.contact import Contact


class ContactRepository:
    logger = logging.getLogger(__name__)

    def __init__(self, session):
        self.session = session

    def get_all_contacts(self):
        try:
            contacts = self.session.query(Contact).all()
            ContactRepository.logger.info(f"Fetched {len(contacts)} contacts")

            return contacts
        except SQLAlchemyError:
            self.session.rollback()
            ContactRepository.logger.exception("Database error while fetching contacts")
            raise
    def add_contact(self, contact: Contact) -> Contact:
        try:
            self.session.add(contact)
            self.session.commit()
            self.session.refresh(contact)

            ContactRepository.logger.info(
                "Contact added successfully",
                extra={"contact_id": contact.id}
            )

            return contact

        except IntegrityError:
            self.session.rollback()
            ContactRepository.logger.exception("Integrity error while adding contact")
            raise

        except SQLAlchemyError:
            self.session.rollback()
            ContactRepository.logger.exception("Database error while adding contact")
            raise
    
    def update_contact(self, updated_contact: Contact) -> Contact:  
        try:
            contact = self.session.merge(updated_contact)
            self.session.commit()

            ContactRepository.logger.info(
                "Contact updated successfully",
                extra={"contact_id": contact.id}
            )

            return contact
        except IntegrityError:
            self.session.rollback()
            ContactRepository.logger.exception("Integrity error while updating contact")
            raise
    
    def delete_contact(self, contact: Contact) -> None:
        try:
            self.session.delete(contact)
            self.session.commit()

            ContactRepository.logger.info(
                "Contact deleted successfully",
                extra={"contact_id": contact.id}
            )

        except SQLAlchemyError:
            self.session.rollback()
            ContactRepository.logger.exception("Database error while deleting contact")
            raise
    
    def get_contact_by_id(self, contact_id: int) -> Contact:
        ContactRepository.logger.info(f"Fetching contact with ID: {contact_id}")
        
        return self.session.get(Contact, contact_id)