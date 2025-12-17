import logging
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from app.models.member import Member
from app.models.member_parent import MemberParent
from app.models.parent import Parent


class ParentRepository:
    logger = logging.getLogger(__name__)

    def __init__(self, db_session):
        self.db_session = db_session
    
    def get_all_parents(self):
        try:
            parents = self.db_session.query(Parent).all()
            ParentRepository.logger.info(f"Fetched {len(parents)} parents")
            return parents
        except SQLAlchemyError:
            self.db_session.rollback()
            ParentRepository.logger.exception("Database error while fetching parents")
            raise
    def add_parent(self, parent: Parent, link: MemberParent) -> Parent:
        try:
            self.db_session.add(parent)
            self.db_session.add(link)
            self.db_session.commit()
            self.db_session.refresh(parent)
            
            ParentRepository.logger.info(
                "Parent added successfully",
                extra={"parent_id": parent.id}
            )
            
            return parent
        except IntegrityError:
            self.db_session.rollback()
            ParentRepository.logger.exception("Integrity error while adding parent")
            raise
        except SQLAlchemyError:
            self.db_session.rollback()
            ParentRepository.logger.exception("Database error while adding parent")
            raise
    
    def update_parent(self, updated_parent: Parent) -> Parent:  
        try:
            parent = self.db_session.merge(updated_parent)
            self.db_session.commit()
            
            ParentRepository.logger.info(
                "Parent updated successfully",
                extra={"parent_id": parent.id}
            )
            
            return parent
        except IntegrityError:
            self.db_session.rollback()
            ParentRepository.logger.exception("Integrity error while updating parent")
            raise
        except SQLAlchemyError:
            self.db_session.rollback()
            ParentRepository.logger.exception("Database error while updating parent")
            raise
    
    def update_link(self, updated_link: MemberParent) -> MemberParent:  
        try:
            link = self.db_session.merge(updated_link)
            self.db_session.commit()
            
            ParentRepository.logger.info(
                "Link updated successfully")
            return link 
        
        except IntegrityError:
            self.db_session.rollback()
            ParentRepository.logger.exception("Integrity error while updating link")
            raise
        except SQLAlchemyError:
            self.db_session.rollback()
            ParentRepository.logger.exception("Database error while updating link")
            raise
    
    def delete_parent(self, parent_id: int) -> None:
        try:
            parent = self.db_session.query(Parent).get(parent_id)
            if parent:
                self.db_session.delete(parent)
                self.db_session.commit()
                
                ParentRepository.logger.info(
                    "Parent deleted successfully",
                    extra={"parent_id": parent_id}
                )
            else:
                ParentRepository.logger.warning(
                    "Parent not found for deletion",
                    extra={"parent_id": parent_id}
                )
        except SQLAlchemyError:
            self.db_session.rollback()
            ParentRepository.logger.exception("Database error while deleting parent")
            raise
    
    def get_parent_by_id(self, parent_id: int) -> Parent:
        ParentRepository.logger.info(f"Fetching parent with ID: {parent_id}")
        
        return self.db_session.get(Parent, parent_id)
    
    def get_link_by_ids(self, member_id: int, parent_id: int) -> MemberParent:
        ParentRepository.logger.info(
            f"Fetching link with Member ID: {member_id} and Parent ID: {parent_id}"
        )
        
        return self.db_session.query(MemberParent).filter_by(
            member_id=member_id,
            parent_id=parent_id
        ).first()