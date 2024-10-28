import pydantic
import pydantic_settings

class MongoSettings(pydantic_settings.BaseSettings):
    MONGODB_URI: str = pydantic.Field(env='MONGODB_URI', default="mongodb://localhost:27017")
    DATABASE_NAME: str = pydantic.Field(env='DATABASE_NAME', default="productsdb")
    COLLECTION_NAME: str = pydantic.Field(env='COLLECTION_NAME', default="products")
