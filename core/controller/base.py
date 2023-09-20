from typing import Any, Generic, Type, TypeVar, List

from fastapi_filter.contrib.sqlalchemy import Filter
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound

from core.database import Base, Propagation, Transactional
from core.exceptions import NotFoundException
from core.repository import BaseRepository

ModelType = TypeVar("ModelType", bound=Base)


class BaseController(Generic[ModelType]):
    """Base class for data controllers."""

    def __init__(self, model: Type[ModelType], repository: BaseRepository):
        self.model_class = model
        self.repository = repository

    async def get_by_id(self, id_: int, join_: set[str] | None = None) -> ModelType:
        """
        Returns the model instance matching the id.

        :param id_: The id to match.
        :param join_: The joins to make.
        :return: The model instance.
        """

        try:
            db_obj = await self.repository.get_by(
                field="id", value=id_, join_=join_, unique=True
            )
        except NoResultFound:
            db_obj = None

        if not db_obj:
            raise NotFoundException(
                f"{self.model_class.__tablename__.title()} with id: {id_} does not exist"
            )

        return db_obj

    async def delete_by_id(self, id_: int) -> None:
        model = await self.get_by_id(id_)
        return await self.delete(model)

    async def update_by_id(self, id_: int, data: BaseModel) -> ModelType:
        model = await self.get_by_id(id_)
        return await self.update(model, data)

    async def filter_and_search(self, filters: Filter) -> List[ModelType]:
        query = filters.filter(select(self.model_class))
        return await self.repository._all(filters.sort(query))

    @Transactional(propagation=Propagation.REQUIRED)
    async def create(self, attributes: dict[str, Any]) -> ModelType:
        """
        Creates a new Object in the DB.

        :param attributes: The attributes to create the object with.
        :return: The created object.
        """
        return await self.repository.create(attributes)

    @Transactional(propagation=Propagation.REQUIRED)
    async def delete(self, model: ModelType) -> None:
        """
        Deletes the Object from the DB.

        :param model: The model to delete.
        :return: True if the object was deleted, False otherwise.
        """
        return await self.repository.delete(model)

    @Transactional(propagation=Propagation.REQUIRED)
    async def update(self, model: ModelType, fields: BaseModel) -> ModelType:
        """
        Updates the Object with given attributes.

        :param model: The model to update.
        :param fields: The fields to update the object with.
        :return: The updates object.
        """
        return await self.repository.update(model, fields.dict(exclude_unset=True))

    @staticmethod
    async def extract_attributes_from_schema(
            schema: BaseModel, excludes: set = None
    ) -> dict[str, Any]:
        """
        Extracts the attributes from the schema.

        :param schema: The schema to extract the attributes from.
        :param excludes: The attributes to exclude.
        :return: The attributes.
        """

        return schema.dict(exclude=excludes, exclude_unset=True)
