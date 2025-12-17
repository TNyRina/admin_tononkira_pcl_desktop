from app.models.member import Member
from app.repositories.member_repository import MemberRepository


class MemberService:
    def __init__(self, session):
        self.session = session
    
    def members(self):
        return MemberRepository(self.session).get_all_members()

    def create_member(self, firstname, lastname, sexe, date_of_birth, image_url=None, address=None):
        new_member = Member(
            firstname=firstname,
            lastname=lastname,
            sexe=sexe,
            data_of_birth=date_of_birth,
            image_url=image_url,
            address=address
        )

        return MemberRepository(self.session).add_member(new_member)
    
    def update_member(self, id, firstname=None, lastname=None, sexe=None, date_of_birth=None, image_url=None, address=None):
        repository = MemberRepository(self.session)
        member = repository.get_member_by_id(id)

        member.firstname = firstname
        member.lastname = lastname
        member.sexe = sexe
        member.data_of_birth = date_of_birth
        member.image_url = image_url
        member.address = address

        return repository.update_member(member)

    def delete_member(self, id):
        MemberRepository(self.session).delete_member(id)