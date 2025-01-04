from pydantic import BaseModel, ConfigDict


class CustomerBase(BaseModel):
    customer_fullname: str
    customer_organization: str
    customer_preferences: str
    customer_age: int
    customer_weight: float


class CreateCustomer(BaseModel):
    pass


class Customer(CustomerBase):
    model_config = ConfigDict(from_attributes=True)

    customer_id: int
