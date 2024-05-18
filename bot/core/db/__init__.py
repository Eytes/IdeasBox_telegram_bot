from .crud import AsyncMongoRegistryFactory
from .helper import mongo_helper

mongo_registry_factory = AsyncMongoRegistryFactory(mongo_helper.get_database())

UserMongoRegistry = mongo_registry_factory.get_registry("users")
