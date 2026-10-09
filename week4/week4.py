# for i in range(100):
#     print("We like Python's turtles!")
#
# months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
#               "November", "December"]
# for month in months:
#     print("One of the months of the year is " + month)
#
# numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# for n in numbers:
#     print(n)
# for n in numbers:
#     print(n, n ** 2)

# import turtle
# t = turtle.Turtle()
# # 1) Eşkenar Üçgen
# for i in range(3):
#     t.forward(100)
#     t.left(120)
#
# t.penup()
# t.forward(150)
# t.pendown()
#
# # 2) Kare
# for i in range(4):
#     t.forward(80)
#     t.left(90)
#
# t.penup()
# t.forward(150)
# t.pendown()
#
# # 3) Altıgen
# for i in range(6):
#     t.forward(60)
#     t.left(60)
#
# t.penup()
# t.forward(150)
# t.pendown()
#
#
# # 4) Sekizgen
# for i in range(8):
#     t.forward(40)
#     t.left(45)
#
#
#
# import turtle
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
#
# t = turtle.Turtle()
# t.shape("turtle")
# t.color("blue")
# t.penup()
#
# for _ in range(12):
#     t.forward(100)
#     t.pendown()
#     t.forward(10)
#     t.penup()
#     t.forward(20)
#     t.stamp()
#     t.backward(130)
#     t.right(30)
#
# turtle.done()


# import turtle
#
# pirate = turtle.Turtle()
#
# screen = turtle.Screen()
# turns = [160, -43, 270, -97, -43, 200, -940, 17, -86]
# for angle in turns:
#     pirate.left(angle)
#     pirate.forward(100)
#
# screen.exitonclick()