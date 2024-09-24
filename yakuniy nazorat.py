import turtle
# to'rtburchakni chizish funksiyasi
def draw_rectangle(x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(width)
    turtle.setheading(90)
    turtle.forward(height)
    turtle.setheading(180)
    turtle.forward(width)
    turtle.setheading(270)
    turtle.forward(height)
# asosiy funksiya
def main():
    # oyna sozlash
    turtle.setup(500, 500)
    turtle.title("To'g'ri to'rtburchak")
   # to'rtburchakni chizish
    draw_rectangle(80, 80, 90, 70)
   # dasturni tugatish
    turtle.done()
# dasturni ishga tushirish
if __name__ == '__main__':
    main()

