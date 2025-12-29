from pydantic import BaseModel


class DivisionDomain(BaseModel):
    name: str
    full_name: str

    class Config:
        from_attributes = True
