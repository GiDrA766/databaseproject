import asyncio

from faker import Faker
from random import randint

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from db.config import connect_to_base
from db.models import JsonTable

# Инициализируем Faker
fake = Faker()


def generate_random_json():
    """
    Генерация случайного JSON объекта с Faker.
    """
    json_data = {
        "user_id": fake.uuid4(),  # Случайный UUID
        "name": fake.name(),  # Случайное имя
        "email": fake.email(),  # Случайный email
        "address": {
            "street": fake.street_address(),
            "city": fake.city(),
            "country": fake.country(),
        },
        "purchase_history": [
            {
                "item_id": fake.uuid4(),
                "item_name": fake.word(),
                "price": round(fake.random.uniform(10.0, 100.0), 2),
                "quantity": randint(1, 5),
            }
            for _ in range(randint(1, 5))  # Генерируем от 1 до 5 покупок
        ],
        "is_active": fake.boolean(),  # Случайное значение True/False
        "signup_date": fake.date(),  # Случайная дата
    }

    return json_data


async def main():
    """
    Main function to handle asynchronous database operations.
    """
    # Ensure connect_to_base() provides the async connection string
    engine = create_async_engine(connect_to_base(), echo=False)

    # Use async_sessionmaker for managing asynchronous sessions
    async_session = async_sessionmaker(engine, expire_on_commit=False)

    async with async_session() as session:
        async with session.begin():  # Start a transaction
            try:
                # Generate and insert 400 rows into the table
                for _ in range(400):
                    json_data = generate_random_json()
                    jsonobj = JsonTable()
                    jsonobj.data = json_data
                    session.add(jsonobj)
                await session.commit()  # Commit asynchronously
            except Exception as e:
                print(f"An error occurred: {e}")
                await session.rollback()  # Rollback on failure

    await engine.dispose()  # Close the connection pool


if __name__ == "__main__":
    # Run the async main function using asyncio
    asyncio.run(main())
