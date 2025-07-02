from pydantic import BaseModel, Field

class InventoryStatus(BaseModel):
    sold: int
    approved: int
    placed: int
    string: int
    pending: int
    available: int
    avalible: int  # Похоже на опечатку в ключе, но включаю как есть
    weisskeiner1: int
    delivered: int
    un_available: int = Field(..., alias="un-available")
    qora: int = Field(..., alias="QORA")
    soldout: int

    class Config:
        allow_population_by_field_name = True