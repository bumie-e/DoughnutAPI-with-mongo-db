import motor.motor_asyncio
from bson.objectid import ObjectId
from decouple import config

MONGO_DETAILS = config('MONGO_DETAILS') # read environment variable.

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.DroidDoughnuts

donut_collection = database.get_collection("Doughnuts")

# helper function for parasing the results from database query


def donut_helper(donut) -> dict:
    return {
        "id": str(donut["_id"]),
        "name": donut["name"],
        "image": donut["image"],
        "price": donut["price"],
        "description": donut["description"],
    }

async def retrieve_donuts():
    donuts = []
    async for donut in donut_collection.find():
        donuts.append(donut_helper(donut))
    return donuts


# Add a new donut into to the database
async def add_donut(donut_data: dict) -> dict:
    donut = await donut_collection.insert_one(donut_data)
    new_donut = await donut_collection.find_one({"_id": donut.inserted_id})
    return donut_helper(new_donut)


# Retrieve a donut with a matching ID
async def retrieve_donut(id: str) -> dict:
    donut = await donut_collection.find_one({"_id": ObjectId(id)})
    if donut:
        return donut_helper(donut)


# Update a donut with a matching ID
async def update_donut(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    donut = await donut_collection.find_one({"_id": ObjectId(id)})
    if donut:
        updated_donut = await donut_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_donut:
            return True
        return False


# Delete a donut from the database
async def delete_donut(id: str):
    donut = await donut_collection.find_one({"_id": ObjectId(id)})
    if donut:
        await donut_collection.delete_one({"_id": ObjectId(id)})
        return True