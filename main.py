class BankAccount:
    def __init__(self, name_user: str, balans: int):
        self.name_user = name_user
        self.balans = balans

    def minus_balans(self, summa):
        return self.balans-summa

    def plus_balans(self,summa):
        return self.balans + summa

    def __str__(self):
        return f'Шановний {self.name_user}! Ваш баланс - {self.balans}'


misha = BankAccount("Misha Sahan",250)
print(misha)