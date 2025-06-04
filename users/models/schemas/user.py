from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserOut(BaseModel):
    user_id: int
    username: str
    email: str

    model_config = ConfigDict(from_attributes=True)