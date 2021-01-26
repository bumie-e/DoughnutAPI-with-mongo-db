from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    add_donut,
    delete_donut,
    retrieve_donut,
    retrieve_donuts,
    update_donut,
)
from server.models.doughnut import (
    ErrorResponseModel,
    ResponseModel,
    DoughnutSchema,
    UpdateDonutOrderModel,
)

router = APIRouter()

# handler for creating new donut
@router.post("/", response_description="Doughnut data added successfully!")
async def add_donut_data(donut: DoughnutSchema = Body(...)):
    donut = jsonable_encoder(donut)
    new_donut = await add_donut(donut)
    return ResponseModel(new_donut, "Doughnut has been added successfully.")

# handler for retreiving all donuts
@router.get("/", response_description="Doughnuts retrieved")
async def get_donuts():
    donuts = await retrieve_donuts()
    if donuts:
        return ResponseModel(donuts, "Doughnuts retrieved successfully")
    return ResponseModel(donuts, "Empty list returned")

# handler for retreiving one donut
@router.get("/{id}", response_description="Doughnut retrieved")
async def get_donut_data(id):
    donut = await retrieve_donut(id)
    if donut:
        return ResponseModel(donut, "Doughnut retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Donut type doesn't exist.")

# handler for updating donut 
@router.put("/{id}")
async def update_donut_data(id: str, req: UpdateDonutOrderModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_donut = await update_donut(id, req)
    if updated_donut:
        return ResponseModel(
            "Doughnut with ID: {} name update is successful".format(id),
            "Doughnut name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the donut data.",
    )

# handler for deleting donut
@router.delete("/{id}", response_description="Donut data deleted from the database")
async def delete_donut_data(id: str):
    deleted_donut = await delete_donut(id)
    if deleted_donut:
        return ResponseModel(
            "Doughnut with ID: {} removed".format(id), "Doughnut deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Doughnut with id {0} doesn't exist".format(id)
    )