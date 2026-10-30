#etkinlik1
def sumTo(n):
    total = (n * (n + 1)) // 2
    return total

# denemeetkinlik1
print(sumTo(10))


#etkinlikk2
import turtle

def draw_star(t, n, size):
    angle = 180 - (180 / n)
    for _ in range(n):
        t.forward(size)
        t.right(angle)

wn = turtle.Screen()
alex = turtle.Turtle()
draw_star(alex, 5, 100)

wn.mainloop()

#etkinlik3
def sumTo(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total

print(sumTo(10))

#etkinlikk4
def mySqrt(n):
    oldguess = n / 2
    for _ in range(20):
        newguess = (1 / 2) * (oldguess + (n / oldguess))
        oldguess = newguess
    return newguess

print(mySqrt(25))
print(mySqrt(2))

#etkinik5
import turtle

def draw_triangle(t, length):
    for _ in range(3):
        t.forward(length)
        t.left(120)

def drawSprite(t, legs, length):
    angle = 360 / legs
    for _ in range(legs):
        t.forward(length)
        draw_triangle(t, 10)
        t.backward(length)
        t.right(angle)

def fancySquare(t, size):
    for _ in range(4):
        t.forward(size)
        drawSprite(t, 8, 20)
        t.right(90)

wn = turtle.Screen()
alex = turtle.Turtle()
alex.speed(8)
fancySquare(alex, 100)

wn.mainloop()

#etkinlik66
def check_number(n):
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"

print(check_number(15))
print(check_number(-8))
print(check_number(0))

#etkinlik7:)
import turtle


def drawBar(t, height, label_offset):
    t.begin_fill()
    t.left(90)
    t.forward(height)

    t.penup()
    t.forward(label_offset)
    t.write(str(height), align="center")
    t.backward(label_offset)
    t.pendown()

    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()


def barChart(data):
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    t = turtle.Turtle()
    t.color("blue", "red")
    t.pensize(3)

    t.penup()
    t.goto(-180, -150)
    t.pendown()

    max_height = max(data)
    label_offset = max_height * 0.05

    for val in data:
        drawBar(t, val, label_offset)

    wn.mainloop()

barChart([48, 117, 200, 240, 160, 260, 220])


