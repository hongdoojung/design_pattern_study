# 데코레이터 패턴(Decorator pattern)이란 주어진 상황 및 용도에 따라 어떤 객체에 책임을 덧붙이는 패턴으로, 기능 확장이 필요할 때 서브클래싱 대신 쓸 수 있는 유연한 대안이 될 수 있다.

from abc import ABCMeta, abstractmethod 

# 음료 클래스 
class Beverage(object):
    __metaclass__ = ABCMeta #추상 클래스로 선언 
    def __init__(self): 
        self.description = "Null" 
    def get_description(self): 
        return self.description 
    @abstractmethod #추상 메소드 선언 
    def cost(self): 
        pass 

# 음료를 상속받은 아메리카노 객체 선언 
class Americano(Beverage): #아메리카노 객체 생성 
    def __init__(self): 
        self.description = "Americano" 

    def cost(self): 
        return 1.99 

# 데코레이터 클래스 선언 
class CondimentDecorator(Beverage): 
    __metaclass__ = ABCMeta

    @abstractmethod 
    def get_description(self): 
        pass 

# 소이밀크를 추가하는 클래스 선언 - 데코레이터 상속 
class Soy(CondimentDecorator):
    def __init__(self, beverage): 
        self.beverage = beverage #기존 음료에 소이밀크 추가 
    
    def get_description(self):
        return self.beverage.get_description() + ", Soy" 

    def cost(self): 
        return self.beverage.cost() + 0.5 

def main():        
    a = Americano() 
    a_soy = Soy(a)

if __name__ == "__main__":
    main()
