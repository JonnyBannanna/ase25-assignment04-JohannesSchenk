from source.core.currency import Currency, EXCHANGE_RATES


class Ingredient:
    """Represents an ingredient."""
    
    def __init__(
        self,
        name: str,
        cost: tuple[Currency, float] | tuple[str, float],
        calories: float
    ):
        """
        :param name: Name of the ingredient.
        :param cost: Tuple containing the currency and the amount of the ingredient in that currency.
        :param calories: Calories of the ingredient in kcal.
        """
        currency_val, amount = cost
        currency = Currency(currency_val) if isinstance(currency_val, str) else currency_val

        if currency not in EXCHANGE_RATES:
            raise ValueError(f'Unsupported currency: {currency}')
        if amount < 0:
            raise ValueError('Cost can not be negative!')
        if calories < 0:
            raise ValueError('Calories can not be negative!')

        self.name: str = name
        """Name of the ingredient."""
        self._cost: float = amount / EXCHANGE_RATES[currency]
        """Cost of the ingredient in EUR."""
        self.calories: float = calories
        """Calories of the ingredient in `kcal`."""

    
    def get_cost(self, target_currency: Currency) -> float:
        """Get the cost of the ingredient.
        
        :param target_currency: Currency to compute the cost in.
        :return: Amount of the ingredient in the specified currency.
        """
        if target_currency not in EXCHANGE_RATES:
            raise ValueError(f'Unsupported currenct: {target_currency}')
        return self._cost * EXCHANGE_RATES[target_currency]
