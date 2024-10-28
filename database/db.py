from motor.motor_asyncio import AsyncIOMotorClient
from settings import MongoSettings
import logging

MAX_DOCUMENTS = 10

settings = MongoSettings()

class MongoDatabase:
    client: AsyncIOMotorClient = None
    db = None

mongo_instance = MongoDatabase()

async def connect_db():
    mongo_instance.client = AsyncIOMotorClient(settings.MONGODB_URI)
    mongo_instance.db = mongo_instance.client[settings.DATABASE_NAME]
    logging.info("Instance connection established")

async def disconnect_db():
    mongo_instance.client.close()
    logging.info("Instance disconnected")