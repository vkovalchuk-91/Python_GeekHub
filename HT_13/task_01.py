"""
Напишіть програму, де клас «геометричні фігури» (Figure) містить властивість color з початковим значенням white і метод
для зміни кольору фігури, а його підкласи «овал» (Oval) і «квадрат» (Square) містять методи __init__ для
завдання початкових розмірів об'єктів при їх створенні.
"""


class Figure:
    def __init__(self):
        self.color = "White"

    def set_color(self, color):
        self.color = color


class Oval(Figure):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height


class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.side_length = side_length


oval = Oval(3, 4)
square = Square(5)
oval.set_color("Blue")
print(f"Oval width: {oval.width}, height: {oval.height}, color: {oval.color}")
print(f"Square side length: {square.side_length}, color: {square.color}")
