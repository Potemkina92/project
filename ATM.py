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

    @staticmethod
    def _validate_cash(currency: str, nominal: str) -> bool:
        return currency in currencies and nominal in nominals

    def put(self, currency: str, nominal: str, count: int) -> None:
        if self._validate_cash(currency, nominal):
            self.bankroll[currency][nominal] += count
            print('Funds credited')
        else:
            raise ValidationError('Operation failed, this nominal or currency not accepted')

    def get(self, currency: str, amount):
        if self.totalsum_of_currency(currency) < amount:
            raise UnavailableError('В банкомате нет денег')
        total = 0
        bills = []
        b = self.bankroll[currency].copy()
        for nom in nominals[::-1]:
            for i in range(self.bankroll[currency][nom]):
                total += int(nom)
                if total < amount:
                    bills.append(int(nom))
                    self.bankroll[currency][nom] -= 1
                elif total > amount:
                    total -= int(nom)
                    if nom == '1':
                        self.bankroll[currency] = b
                    continue
                else:
                    bills.append(int(nom))
                    self.bankroll[currency][nom] -= 1
                    s = {}
                    for bill in bills:
                        if bill not in s:
                            s[bill] = 1
                        else:
                            s[bill] += 1
                    print(sum(bills), currency, ':', s)
        if sum(bills) < amount:
            self.bankroll[currency] = b
            print(self.bankroll[currency])
            raise UnavailableError('В банкомате нет денег')

    def totalsum_of_currency(self, currency, total=0):
        for nom in nominals[::-1]:
            for i in range(self.bankroll[currency][nom]):
                total += int(nom)
        return total


x = ATM()
x.put('RUB', '50', 4)
x.put('RUB', '10', 6)
x.put('RUB', '5', 10)
x.put('EUR', '100', 3)
x.put('EUR', '50', 2)
x.put('USD', '50', 3)
x.get('USD', 50)
# try:
#     x.get('RUB', 165)
# except UnavailableError as e:
#     print(f'Ошибка: {e}')
x.get('RUB', 200)
x.get('RUB', 15)
x.get('EUR', 50)
print(x.bankroll, end='\n')

