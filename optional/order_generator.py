import aiohttp
import asyncio
from faker import Faker
import random

# Initialize the Faker instance
fake = Faker()


# Function to generate random order details
def generate_random_order():
    return {
        "dish_id": random.randint(1, 800),  # Random ID between 1 and 1000
        "customer_id": random.randint(1, 800),  # Random ID between 1 and 1000
        "order_time": fake.date_between(start_date="-1y", end_date="+1y").strftime(
            "%Y-%m-%d"
        ),  # Random date in ISO format
        "order_pay_type": random.choice(["cash", "card"]),  # Random payment type
    }


# Async function to send a POST request
async def post_order(session, url, order_data, request_number):
    try:
        async with session.post(url, json=order_data) as response:
            # Get response text for logging/debugging
            response_text = await response.text()
            print(
                f"Request {request_number}: Status {response.status}, Response: {response_text}"
            )
    except Exception as e:
        print(f"Request {request_number}: An error occurred - {e}")


# Main async function to execute multiple requests concurrently
async def main():
    # API endpoint and headers
    url = "http://127.0.0.1:8000/api/v1/order/"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }

    # Number of requests
    num_requests = 1000  # Adjust based on your needs

    # Create an async session
    async with aiohttp.ClientSession(headers=headers) as session:
        # List to hold async tasks
        tasks = []
        for i in range(1, num_requests + 1):
            order_data = generate_random_order()  # Generate random order data
            tasks.append(
                post_order(session, url, order_data, i)
            )  # Add each task to the list

        # Execute all tasks concurrently
        await asyncio.gather(*tasks)


# Run the async script
if __name__ == "__main__":
    asyncio.run(main())
