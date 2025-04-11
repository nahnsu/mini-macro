import os
from jinja2 import Environment, FileSystemLoader
from app.core.openai_client import client

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
env = Environment(loader=FileSystemLoader(os.path.join(parent_dir, "templates")))

async def general_quesiton(question: str):
    """General regular LLM/ open ai API """
    nutrition_template = env.get_template("general.jinja2")
    system_prompt = nutrition_template.render()
    response = client.chat.completions.create(
        model="grok-2-latest",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question},
        ],
        max_tokens=180
    )
    return response.choices[0].message.content