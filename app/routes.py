from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from models import doughnut

router = APIRouter()

doughnuts = {
    "item1":{
        "ids": "7789",
         "name": "Glaced fritt Doughnut",
         "image": "5677.jpg",
         "price": 780,
         "description": "This doughnut is glaced with icing sugar and fritt. Delicious!",
         "topping": "Icing sugar",
         "preparation_time": "20 mins"
    },
    "item2":{
        "ids": "7790",
         "name": "Glaced Sprinkle Doughnut",
         "image": "5877.jpg",
         "price": 900,
         "description": "This doughnut is glaced with Sprinkles. Delicious!",
         "topping": "Sprinkles",
         "preparation_time": "25 mins"
    }
}

@router.get("/")
async def get_doughnuts() -> dict:
    return {
        "data": doughnut
    }

@router.get("/{id}")
async def get_doughnut(id: str) -> dict:
    if int(id) > len(doughnut):
        return {
            "error": "Invalid Doughnut ID"
        }

    for dounut in doughnut.keys():
        if dounut == id:
            return {
                "data": doughnut[dounut]
            }