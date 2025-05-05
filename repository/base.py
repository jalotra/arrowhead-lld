

from typing import TypeVar, Generic, Dict

# Define a generic type variable
T = TypeVar('T')

# this is a base repository
# which does CRUD operations
class BaseRepository(Generic[T]):
    def __init__(self):
        self.entities: Dict[str, T] = {}
    
    def create(self, entity_id: str, entity: T) -> T:
        self.entities[entity_id] = entity
        return entity

    def read(self, entity_id: str) -> T:
        return self.entities[entity_id]

    def update(self, entity_id: str, entity: T) -> T:
        self.entities[entity_id] = entity
        return entity

    def delete(self, entity_id: str) -> None:
        del self.entities[entity_id]