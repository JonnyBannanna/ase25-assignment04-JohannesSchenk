from copy import deepcopy

from source.core.ingredient import Ingredient
from source.core.currency import Currency


# TODO: add sample images (too much for the scope of the exercise tho) (hello corrector person :) )
# TODO: add categories (not part of the chosen FR tho)
class Meal:
    """Represents a meal with ingredients and instructions."""

    def __init__(
        self,
        name: str,
        ingredients: list[Ingredient],
        recipe: str,
        description: str = ''
    ):
        self.name: str = name
        """Name of the meal."""
        self.ingredients: list[Ingredient] = deepcopy(ingredients)
        """List of ingredients required for the meal."""
        self.recipe: str = recipe
        """Cooking instructions / recipe steps."""
        self.description: str = description
        """Short description of the meal."""


    def get_price(self, target_currency: Currency) -> float:
        """Get the cost of the meal.
        
        :param target_currency: Currency to compute the cost in.
        :return: Amount of the ingredient in the specified currency.
        """
        return sum(ingredient.get_cost(target_currency) for ingredient in self.ingredients)
