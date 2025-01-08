from sqlalchemy import and_

from db.models import Customer


async def get_filter(
    customer_id: int = None,
    customer_name: str = None,
    customer_organization: str = None,
    customer_preferences: str = None,
    customer_age: int = None,
    customer_weight: float = None,
):
    where_filter = []
    if customer_id:
        where_filter.append(Customer._id_ == customer_id)
    if customer_name:
        where_filter.append(Customer.customer_fullname == customer_name)
    if customer_organization:
        where_filter.append(Customer.customer_organization == customer_organization)
    if customer_preferences:
        where_filter.append(Customer.customer_preferences == customer_preferences)
    if customer_age:
        where_filter.append(Customer.customer_weight == customer_age)
    if customer_weight:
        where_filter.append(Customer.customer_weight == customer_weight)
    return and_(*where_filter) if where_filter else None
