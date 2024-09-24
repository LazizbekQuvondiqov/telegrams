
import turtle

# Задаем координаты трех точек
x1, y1 = 100, 100
x2, y2 = 150, 100
x3, y3 = 100, 150
x4,y4=150,150
# Создаем экран и черепашку
ekran = turtle.Screen()
t = turtle.Turtle()

# Перемещаем черепашку в первую точку
t.penup()
t.goto(x1, y1)
t.pendown()

# Рисуем треугольник
t.goto(x2, y2)
t.goto(x4, y4)
t.goto(x3,y3)

t.goto(x1, y1)





