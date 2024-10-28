from libs.third_party_lib import BaseModel, Optional, HttpUrl, List, Field
from libs.standard_lib import datetime

class Product(BaseModel):
    name: str
    price: float
    currency: str
    link: str

class SData(BaseModel):
    filtered_products: List[Product]
    total_sum: float
    timestamp: datetime

class SProd(BaseModel):
    status: Optional[str]
    source: Optional[str]
    data: SData
    