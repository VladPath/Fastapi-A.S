from pydantic import BaseModel, Field


class Hotels(BaseModel):
    name:str
    title:str

class HotelsPutch(BaseModel):
    name: str | None = Field(None, description='Имя отеля')
    title:str | None = Field(None, description="Заголовок отеля")
