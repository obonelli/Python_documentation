from pydantic import BaseModel, Field


class ItemCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    price: float = Field(ge=0)
    in_stock: bool = True


class ItemOut(ItemCreate):
    # ⬇️ id ahora es int (coincide con AUTO_INCREMENT)
    id: int
