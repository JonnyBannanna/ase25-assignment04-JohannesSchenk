from enum import Enum


class Currency(Enum):
    """Enum of supported currencies."""
    EUR = 'EUR'
    USD = 'USD'
    GBP = 'GBP'


# TODO: Make exchange rates more flexible
#   - Currently hardcoded for the prototype.
#   - Possible improvements:
#       A: Load live rates from a reliable stock exchange API
#       B: Update rates at regular intervals (e.g. daily) using an API
EXCHANGE_RATES: dict[Currency, float] = {
    Currency.EUR: 1.0,
    Currency.USD: 1.1,
    Currency.GBP: 0.88
}
"""Exchange rates from EUR -> [CURRENCY]."""
