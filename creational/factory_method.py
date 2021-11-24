# 팩토리 메소드
	# 부모(상위) 클래스에 알려지지 않은 구체 클래스를 생성하는 패턴이며. 자식(하위) 클래스가 어떤 객체를 생성할지를 결정하도록 하는 패턴이기도 하다. 부모(상위) 클래스 코드에 구체 클래스 이름을 감추기 위한 방법으로도 사용한다. Factory Method가 중첩되기 시작하면 굉장히 복잡해 질 수 있다. 또한 상속을 사용하지만 부모(상위) 클래스를 전혀 확장하지 않는다. 따라서 이 패턴은 extends 관계를 잘못 이용한 것으로 볼 수 있다. extends 관계를 남발하게 되면 프로그램의 엔트로피가 높아질 수 있으므로 Factory Method 패턴의 사용을 주의해야 한다.

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