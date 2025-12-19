"""Database for the prototype containing global variables for available
ingredients and available meals.
"""
import json

from pathlib import Path

from source.core import Meal
from source.core import Ingredient


AVAILABLE_INGREDIENTS: dict[str, Ingredient] = {}
AVAILABLE_MEALS: dict[str, Meal] = {}


def update_available_ingredients() -> None:
    global AVAILABLE_INGREDIENTS
    file_path: str = str(Path(__file__).parents[2] / 'sample_data' / 'ingredients.json')

    AVAILABLE_INGREDIENTS.clear()

    with open(file_path, 'r') as file:
        AVAILABLE_INGREDIENTS.update({
            sample['name']: Ingredient(
                sample['name'],
                sample['cost'],
                sample['calories']
            )
            for sample in json.load(file)
        })


def update_available_meals() -> None:
    global AVAILABLE_MEALS
    file_path: str = str(Path(__file__).parents[2] / 'sample_data' / 'meals.json')

    AVAILABLE_MEALS.clear()

    with open(file_path, 'r') as file:
        AVAILABLE_MEALS.update({
            sample['name']: Meal(
                sample['name'],
                [
                    ingredient
                    for name, ingredient in AVAILABLE_INGREDIENTS.items()
                    if name in sample['ingredients']],
                sample['recipe'],
                sample['description']
            )
            for sample in json.load(file)
        })
