from fastapi import FastAPI
from server.routes.doughnut import router as DonutRouter

app = FastAPI()

app.include_router(DonutRouter, tags=['Donut'], prefix="/doughnut")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Get your yummy doughnuts"}