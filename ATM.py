currencies = ('RUB', 'USD', 'EUR')
nominals = ('1', '5', '10', '50', '100', '500', '1000', '5000')


class UnavailableError(Exception):
    pass


class ValidationError(Exception):
    pass


class ATM:
    def __init__(self, currencies: tuple = currencies, nominals: tuple = nominals) -> None:
        self.currencies = currencies
        self.nominals = nominals
        self.bankroll = self._create_empty_bankroll()

    @staticmethod
    def _create_empty_bankroll():
        bankroll = {}
        for cur in currencies:
            bankroll[cur] = {}
            for nom in nominals:
                bankroll[cur][nom] = 0

        return bankroll
