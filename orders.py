class Product:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.name} x{self.quantity} — {self.total()} руб."


class Cart:
    def __init__(self):
        self.__items = []

    def add(self, product):
        self.__items.append(product)
        print(f"Добавлено: {product.name}")

    def remove(self, name):
        self.__items = [p for p in self.__items if p.name != name]
        print(f"Удалено: {name}")

    def total(self):
        return sum(p.total() for p in self.__items)

    def show(self):
        if not self.__items:
            print("Корзина пуста")
            return
        print("Корзина:")
        for item in self.__items:
            print(f"  {item}")
        print(f"Итого: {self.total()} руб.")


if __name__ == '__main__':
    cart = Cart()
    cart.add(Product("Хлеб", 50, 2))
    cart.add(Product("Молоко", 80, 1))
    cart.add(Product("Сыр", 200, 3))
    cart.show()
    cart.remove("Молоко")
    cart.show()
