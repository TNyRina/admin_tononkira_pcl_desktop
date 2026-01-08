from app.exceptions.business_exception import ValidationError
from app.exceptions.technical_exception import DatabaseError
from app.models.category import Category
from app.repositories.category_repository import CategoryRepository
class CategoryService:
    def __init__(self, session):
        self.session = session

    def categories(self):
        return CategoryRepository(self.session).get_all_categories()

    def create_category(self, name: str) -> Category:
        if not name or name.strip() == "":
            raise ValidationError(message=f"Field {name} is required.", code="FIELD_REQUIRED", field="name")

        if CategoryRepository(self.session).is_category_exists(name):
            raise ValidationError(
                message=f"Category with name '{name}' already exists.",
                code="DUPLICATE_FIELD",
                field="name"
            )

        try:
            return CategoryRepository(self.session).add_category(
                Category(name=name)
            )

        except DatabaseError as e:
            raise ValidationError("Failed to create category", code="CREATE_FAILED") from e
    
    def update_category(self, id: int, name: str) -> Category:
        repository = CategoryRepository(self.session)
        category = repository.get_category_by_id(id)
        category.name = name

        return repository.update_category(category)

    def delete_category(self, id: int):
        CategoryRepository(self.session).delete_category(id)

    
    def _analyze_integrity_error(self, e):
        msg = str(e.orig).lower()

        if "unique constraint" in msg:
            return "duplicate"

        if "not null constraint" in msg:
            return "null_violation"

        return "unknown"


