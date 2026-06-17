class Shape:
    def __init__(self):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14 * self.radius
```

Kodni ishlatish uchun misol:
```python
rectangle = Rectangle(5, 10)
print(rectangle.area())  # 50
print(rectangle.perimeter())  # 30

circle = Circle(5)
print(circle.area())  # 78.5
print(circle.perimeter())  # 31.4
