# https://ko.wikipedia.org/wiki/팩토리_메서드_패턴#파이썬

class Pizza:
    HAM_MUSHROOM_PIZZA_TYPE = 0
    DELUXE_PIZZA_TYPE = 1
    SEAFOOD_PIZZA_TYPE= 2

    def __init__(self):
        self.__price = None

    def getPrice(self):
        return self.__price

class HamAndMushroomPizza(Pizza):
    def __init__(self):
        self.__price = 8.50

class DeluxePizza(Pizza):
    def __init__(self):
        self.__price = 10.50

class SeafoodPizza(Pizza):
    def __init__(self):
        self.__price = 11.50

class PizzaFactory:
    def createPizza(self, pizzaType):
        if pizzaType == Pizza.HAM_MUSHROOM_PIZZA_TYPE:
            return HamAndMushroomPizza()
        elif pizzaType == Pizza.DELUXE_PIZZA_TYPE:
            return DeluxePizza()
        elif pizzaType == Pizza.SEAFOOD_PIZZA_TYPE:
            return SeafoodPizza()
        else:
            return DeluxePizza()

# Usage
pizzaPrice = PizzaFactory().createPizza(Pizza.HAM_MUSHROOM_PIZZA_TYPE).getPrice()
print(f"{pizzaPrice}")