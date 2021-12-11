# 컴포지트 패턴(Composite pattern)이란 객체들의 관계를 트리 구조로 구성하여 부분-전체 계층을 표현하는 패턴으로, 사용자가 단일 객체와 복합 객체 모두 동일하게 다루도록 한다.

from abc import abstractmethod

class Component:
    @abstractmethod
    def my_list(self):
        pass

class Leaf(Component):
    val = None
    
    def __init__(self, val) -> None:
        super().__init__()
        self.val = val
    
    def my_list(self):
        print(self.val)

class Composite(Component):
    val = None
    composite_list = None

    def __init__(self, val) -> None:
        super().__init__()
        self.val = val
    
    def add(self, obj):
        if not self.composite_list:
            self.composite_list = []
        self.composite_list.append(obj)

    def my_list(self):
        print(self.val, ":")
        for obj in self.composite_list:
            obj.my_list()
        
def main():
    num0 = Leaf(0)
    num1 = Leaf(1)
    num2 = Leaf(2)
    num3 = Leaf(3)
    num4 = Leaf(4)

    container1 = Composite("Container 1")
    container2 = Composite("Container 2")

    container1.add(num0)
    container1.add(num1)

    container2.add(num2)
    container2.add(num3)
    container2.add(num4)

    container1.add(container2)
    container1.my_list()

if __name__ == "__main__":
    main()
