import logging
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from app.models.member import Member


class MemberRepository:
    logger = logging.getLogger(__name__)
    
    def __init__(self, db_session):
        self.db_session = db_session
    
    def get_all_members(self):
        try:
            members = self.db_session.query(Member).all()
            MemberRepository.logger.info(f"Fetched {len(members)} members")
            return members
        except SQLAlchemyError:
            self.db_session.rollback()
            MemberRepository.logger.exception("Database error while fetching members")
            raise
    
    def add_member(self, member: Member) -> Member:
        try:
            self.db_session.add(member)
            self.db_session.commit()
            self.db_session.refresh(member)
            
            MemberRepository.logger.info(
                "Member added successfully",
                extra={"member_id": member.id}
            )
            
            return member
        except IntegrityError:
            self.db_session.rollback()
            MemberRepository.logger.exception("Integrity error while adding member")
            raise
        except SQLAlchemyError:
            self.db_session.rollback()
            MemberRepository.logger.exception("Database error while adding member")
            raise

    def update_member(self, updated_member: Member) -> Member:  
        try:
            member = self.db_session.merge(updated_member)
            self.db_session.commit()
            
            MemberRepository.logger.info(
                "Member updated successfully",
                extra={"member_id": member.id}
            )
            
            return member
        except IntegrityError:
            self.db_session.rollback()
            MemberRepository.logger.exception("Integrity error while updating member")
            raise
        except SQLAlchemyError:
            self.db_session.rollback()
            MemberRepository.logger.exception("Database error while updating member")
            raise
    
    def delete_member(self, member_id: int) -> None:
        try:
            member = self.db_session.query(Member).get(member_id)
            if member:
                self.db_session.delete(member)
                self.db_session.commit()
                
                MemberRepository.logger.info(
                    "Member deleted successfully",
                    extra={"member_id": member_id}
                )
            else:
                MemberRepository.logger.warning(
                    "Attempted to delete non-existent member",
                    extra={"member_id": member_id}
                )
        except SQLAlchemyError:
            self.db_session.rollback()
            MemberRepository.logger.exception("Database error while deleting member")
            raise
    def get_member_by_id(self, member_id: int) -> Member:
        MemberRepository.logger.info(f"Fetching member with ID: {member_id}")
        
        return self.db_session.get(Member, member_id)