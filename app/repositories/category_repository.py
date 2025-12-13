from app.models.category import Category


class CategoryRepository:
    def __init__(self, session):
        self.session = session

    def add_category(self, category):
        self.session.add(category)
        self.session.commit()
        self.session.refresh(category)
        self.session.close()

        return category

    def get_by_id(self, cat_id):
        category = self.session.query(Category).filter(Category.id == cat_id).first()
        self.session.close()
        return category
