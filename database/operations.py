from database.db import mongo_instance, settings, MAX_DOCUMENTS
from app.schemas import SProd, SData
from pymongo import ASCENDING
from bson import ObjectId
from libs.third_party_lib import List, Optional

async def get_doc_by_id(product_id: str) -> Optional[SProd]:
    collection = mongo_instance.db[settings.COLLECTION_NAME]
    document = await collection.find_one({"_id": ObjectId(product_id)})
    if document:
        return document
    return None

async def insert_product_data(product_data: SProd):
    collection = mongo_instance.db[settings.COLLECTION_NAME]
    result = await collection.insert_one(product_data.dict())
    return result.inserted_id

###############################################################################
async def delete_product(product_id: str) -> bool:
    collection = mongo_instance.db[settings.COLLECTION_NAME]
    result = await collection.delete_one({"_id": ObjectId(product_id)})
    return result.deleted_count > 0

async def update_doc_by_id(doc_id: str, updated_data: dict):
    collection = mongo_instance.db[settings.COLLECTION_NAME]
    result = await collection.update_one({"_id": ObjectId(doc_id)}, {"$set": updated_data})
    if result.matched_count == 0:
        return result
    

