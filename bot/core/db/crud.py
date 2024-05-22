from motor.motor_asyncio import (
    AsyncIOMotorCollection,
    AsyncIOMotorDatabase,
)
from pydantic import BaseModel


class AsyncMongoRegistry:
    def __init__(self, collection: AsyncIOMotorCollection) -> None:
        self.__collection = collection

    async def get_by_id(self, item_id) -> dict | None:
        """Получить запись из БД по id"""
        return await self.__collection.find_one({"_id": item_id})

    async def create(self, item_data: BaseModel):
        """Создание записи в БД"""
        result = await self.__collection.insert_one(item_data.model_dump(by_alias=True))
        return result.inserted_id

    async def update(self, item_id, new_data: BaseModel):
        """Обновление данных в БД"""
        return await self.__collection.find_one_and_update(
            {"_id": item_id},
            {"$set": new_data.model_dump()},
        )

    async def delete_by_id(self, item_id):
        """Удаление записи из БД"""
        return await self.__collection.find_one_and_delete({"_id": item_id})


class AsyncMongoRegistryFactory:
    def __init__(self, database: AsyncIOMotorDatabase):
        self.__database = database

    def get_registry(self, collection_name: str) -> AsyncMongoRegistry:
        return AsyncMongoRegistry(self.__database[collection_name])
