from pydantic import BaseModel
from typing import List, Optional, Dict, Any, Union


class UserFood(BaseModel):
    description: str


class MacroNutrient(BaseModel):
    calories: float
    protein: float
    carbohydrates: float
    fat: float
    fiber: Optional[float] = None

