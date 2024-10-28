from libs.third_party_lib import UploadFile, File, HTTPException, Path, StreamingResponse, Query
from libs.standard_lib import base64, io, os, datetime, json
from database import *
from app.schemas import SProd, SData, Product


MAX_DOCUMENTS = 10

async def upload_product_file(file: UploadFile = File(...)):
    await connect_db()
    
    if file.content_type != "application/json":
        raise HTTPException(status_code=400)
        
    try:
        contents = await file.read()
        product_data = json.loads(contents)
        validated_data = SProd(**product_data)
        inserted_id = await insert_product_data(validated_data)
        return {"status": "Data uploaded successfully", "id": str(inserted_id)}
    
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON file format")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def get_sdata_by_id(doc_id: str):
    try:
        document = await get_doc_by_id(doc_id)
        
        sdata = document.get("data")

        validated_sdata = SData(**sdata)
        return validated_sdata.dict()
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def get_product_by_name(doc_id: str, product_name: str):
    try:
        document = await get_doc_by_id(doc_id)
        
        sdata = document.get("data")
        validated_sdata = SData(**sdata)
        products = validated_sdata.filtered_products
        
        matching_products = [
            product.dict() for product in products if product_name.lower() in product.name.lower()
        ]
        
        if not matching_products:
            raise HTTPException(status_code=404, detail="No products found matching the given name")
        
        return matching_products
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
async def delete_product_by_id(doc_id: str):
    try:
        await delete_product(doc_id)
        return {"status": "Succesfully deleted document", "id": str(doc_id)}
        
    except Exception as e:
        raise HTTPException(status_code=404, detail="No document with that ID matching")
    
    
async def insert_product_into_sdata(doc_id: str, new_product: Product):
    try:
        document = await get_doc_by_id(doc_id)
        
        sdata = document.get("data")
        if not sdata:
            raise HTTPException(status_code=404, detail="SData field not found in the document")
        
        validated_sdata = SData(**sdata)
        
        validated_sdata.filtered_products.append(new_product)
        
        validated_sdata.total_sum += new_product.price
        
        updated_sdata = validated_sdata.dict()
        await update_doc_by_id(doc_id, {"data": updated_sdata})
        
        return {"status": "Product inserted successfully"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def get_prods_in_range(doc_id: str, offset: int, limit: int):
    try:
        document = await get_doc_by_id(doc_id)
        
        sdata = document.get("data")

        validated_sdata = SData(**sdata)
        products = validated_sdata.filtered_products
        paginated_products = products[offset:offset + limit]
        return paginated_products
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))