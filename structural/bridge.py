# 구현부에서 추상층을 분리하여 각자 독립적으로 변형할 수 있게 하는 패턴이다.

# Implementor
class DrawingAPI:
    def draw_circle(self, x, y, radius):
        pass

# ConcreteImplementor 1/2
class DrawingAPI1(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"API1.circle at {x}:{y} {radius}")

# ConcreteImplementor 2/2
class DrawingAPI2(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"API2.circle at {x}:{y} {radius}")

# Abstraction
class Shape:
    def draw(self):
        pass
    def resize_by_percentage(pct):
        pass

# Refined Abstraction
class CircleShape(Shape):
    x = 0
    y = 0
    radius = 0
    drawing_api = None

    def __init__(self, x, y, radius, drawing_api):
        self.x = x
        self.y = y
        self.radius = radius
        self.drawing_api = drawing_api

    def draw(self):
        self.drawing_api.draw_circle(self.x, self.y, self.radius)

    def resize_by_percentage(self, pct):
        self.radius *= pct

def main():
    dap1 = DrawingAPI1()
    dap2 = DrawingAPI2()
    circle1 = CircleShape(1, 2, 3, dap1)
    circle2 = CircleShape(5, 7, 11, dap2)
    circle1.resize_by_percentage(2.5)
    circle2.resize_by_percentage(2.5)
    circle1.draw()
    circle2.draw()

if __name__ == "__main__":
    main()
