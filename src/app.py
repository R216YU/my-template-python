from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Add Your Project Title Here",
    description="Add Your Project Description Here",
)


class ExampleResponseModel(BaseModel):
    success: bool
    message: str


@app.get("/", response_model=ExampleResponseModel)
async def read_root():
    return {"success": True, "message": "Hello, World!"}
