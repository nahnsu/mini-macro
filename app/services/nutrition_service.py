import os
from jinja2 import Environment, FileSystemLoader
from app.core.openai_client import client
from app.models.nutrition import UserFood, MacroNutrient

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
env = Environment(loader=FileSystemLoader(os.path.join(parent_dir, "templates")))

async def get_micronutrients(user_food: UserFood):
    
    nutrition_template = env.get_template("nutrition.jinja2")
    system_prompt = nutrition_template.render()
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_food.description}
    ]
    
    response = client.beta.chat.completions.parse(
        model="grok-2-latest",
        messages=messages,
        response_format=MacroNutrient
    )
    
    # Return the structured response (already a NutritionResponse model)
    return response.choices[0].message.parsed
