class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        pass

    def info(self):
        return f"{self.name}, возраст: {self.age}"


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        return f"{self.name} говорит: Гав!"

    def info(self):
        return f"{super().info()}, порода: {self.breed}"


class Cat(Animal):
    def speak(self):
        return f"{self.name} говорит: Мяу!"


if __name__ == '__main__':
    dog = Dog("Шарик", 3, "Лабрадор")
    cat = Cat("Мурка", 2)

    print(dog.info())
    print(dog.speak())
    print(cat.info())
    print(cat.speak())
