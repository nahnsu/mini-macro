import os
from jinja2 import Environment, FileSystemLoader
from app.core.openai_client import client
from app.models.nutrition import UserFood, MacroNutrient

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
env = Environment(loader=FileSystemLoader(os.path.join(parent_dir, "templates")))


async def get_micronutrients(user_food: UserFood):
    """ STRUCTURED OUTPUTS. LLM's response will be in the Pydantic Data model you pass in 'response_format'. AKA JSON if you want"""
    question = user_food.description
    nutrition_template = env.get_template("nutrition.jinja2")
    system_prompt = nutrition_template.render()

    response = client.beta.chat.completions.parse(
        model="grok-2-latest",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question},
        ],
        response_format=MacroNutrient,
    )

    # Return the structured response (already a NutritionResponse model)
    nutrients = response.choices[0].message.parsed

    return nutrients
