import openai
import subprocess
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def recipe_idea(ingredients):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Create a recipe with the following ingredients: {ingredients} Also create a name for this recipe.",
        temperature=0.9,
        max_tokens=2048,
        n=1,
        stop=None
    )
    return response['choices'][0]['text'].strip()

ingredients = input("What ingredients do you have available? ")
recipe = recipe_idea(ingredients)
print(f"Genereted command: {recipe}")
