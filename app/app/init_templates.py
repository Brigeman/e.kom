from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://mongo:27017"
client = AsyncIOMotorClient(MONGO_URI)
db = client["forms"]
collection = db["form_templates"]

async def init_templates():
    templates = [
        {
            "name": "Template 1",
            "field_name_1": "email",
            "field_name_2": "phone"
            # Добавьте другие поля и шаблоны по необходимости
        },
        # Добавьте другие примеры шаблонов по необходимости
    ]

    for template in templates:
        await collection.insert_one(template)

if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(init_templates())
