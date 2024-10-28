from libs.third_party_lib import UploadFile, File, Path, List, APIRouter, Query
from app.services import upload_product_file, get_sdata_by_id, get_product_by_name, delete_product_by_id, insert_product_into_sdata, get_prods_in_range
from app.schemas import Product

router = APIRouter()

@router.post("/upload")
async def upload_json(file: UploadFile = File(...)):
    return await upload_product_file(file)

@router.get("/sdata/{doc_id}")
async def get_sdata(doc_id: str):
    return await get_sdata_by_id(doc_id)

@router.get("/sdata/{doc_id}/{product_name}")
async def get_product(doc_id: str, product_name: str):
    return await get_product_by_name(doc_id, product_name)

@router.delete("/delete/{doc_id}")
async def delete_doc_by_id(doc_id: str):
    return await delete_product_by_id(doc_id)

@router.put("/sdata/{doc_id}/add-product")
async def add_product_to_sdata(doc_id: str, product: Product):
    return await insert_product_into_sdata(doc_id, product)

@router.get("/sdata/{doc_id}/{offset}/{limit}")
async def get_products_by_offset_limit(doc_id: str, offset: int = 0, limit: int = 5):
    return await get_prods_in_range(doc_id, offset, limit)