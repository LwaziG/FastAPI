from pydantic import BaseModel, Config

class OrderCreate(BaseModel):
    user_id: int
    item_id: int

class OrderOut(BaseModel):
    order_id: int
    user_id: int
    item_id: int

    model_config = Config.from_attributes()