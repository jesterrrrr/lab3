class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self.__balance += amount
        print(f"Пополнено на {amount}. Баланс: {self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self.__balance:
            raise ValueError("Недостаточно средств")
        self.__balance -= amount
        print(f"Снято {amount}. Баланс: {self.__balance}")

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Счёт {self.__owner}: {self.__balance} руб."


if __name__ == '__main__':
    acc = BankAccount("Максим", 1000)
    print(acc)
    acc.deposit(500)
    acc.withdraw(200)
    print(acc)
