from app.models.member_parent import MemberParent
from app.models.parent import Parent
from app.repositories.member_repository import MemberRepository
from app.repositories.parent_repository import ParentRepository


class ParentService:
    def __init__(self, session):
        self.session = session  
    
    def parents(self):
        return ParentRepository(self.session).get_all_parents()

    def create_parent(self, name, address=None, role=None, member_id=None):
        new_parent = Parent(
            name=name,
            address=address
        )

        member = MemberRepository(self.session).get_member_by_id(member_id)

        link = MemberParent(member=member, parent=new_parent, role=role)

        return ParentRepository(self.session).add_parent(new_parent, link)

    def update_parent(self, id, name=None, address=None):
        repository = ParentRepository(self.session)
        parent = repository.get_parent_by_id(id)

        parent.name = name
        parent.address = address

        return repository.update_parent(parent)

    def update_link_role(self, member_id, parent_id, role):
        repository = ParentRepository(self.session)
        link = repository.get_link_by_ids(member_id, parent_id)
        link.role = role

        return repository.update_link(link)
    

    def delete_parent(self, id):
        ParentRepository(self.session).delete_parent(id)

