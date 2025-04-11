from contextlib import asynccontextmanager
import traceback

from fastapi import FastAPI, Header, HTTPException
from app.models.nutrition import UserFood
from app.models.general import GeneralQuestion
from app.services.nutrition_service import get_micronutrients
from app.services.general import general_quesiton


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

    pass


app = FastAPI(
    title="Mini-Macro",
    description="Food nutrition analysis API",
    version="0.1.0",
    lifespan=lifespan,
)


@app.get("/")
async def root():
    return {
        "app": "Mini-Macro",
        "version": "0.1.0",
        "description": "Food nutrition analysis API",
    }


@app.get("/healthcheck")
async def healthcheck():
    return "checking mini macro and it looks healthy"


@app.post("/nutrients")
async def extract_nutrients(
    request: UserFood, accept: str = Header(default="application/json")
):
    try:
        result = await get_micronutrients(request)  # Call the new function
        return result
    except Exception as e:
        print(f"Error: {str(e)}")
        print(f"Traceback:\n{traceback.format_exc()}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    

@app.post("/general")
async def general_llm_call(
    request: GeneralQuestion, accept: str = Header(default="application/json")
):
    try:
        result = await general_quesiton(request.question)  
        return result
    except Exception as e:
        print(f"Error: {str(e)}")
        print(f"Traceback:\n{traceback.format_exc()}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
