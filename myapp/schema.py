# schemas.py
from pydantic import BaseModel
from typing import List
from typing import Union

# TO support creation and update APIs
class CreateAndUpdateCar(BaseModel):
    manufacturer: str
    modelName: str
    cc: int
    onRoadPrice: int
    seatingCapacity: int
    gearBox: int
   


# TO support list and get APIs
class Car(CreateAndUpdateCar):
    id: int

    class Config:
        orm_mode = True


# To support list cars API
class PaginatedCarInfo(BaseModel):
    limit: int
    offset: int
    data: List[Car] 
    


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None


class UserInDB(User):
    hashed_password: str