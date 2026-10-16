# #soru1
# import random
# for i in range(10):
#     print(random.random())
# #soru2
# import random
# for i in range(10):
#     print(random.randint(25, 35))
#
# #soru3
# import math
# a = int(input("Enter length: "))
# b = int(input("Enter width: "))
# hypotenuse = math.sqrt(a**2 + b**2)
#
# #soru4
# print(hypotenuse)
#
# import math
# def areaOfCircle(r):
#     return math.pi * (r ** 2)
# print(areaOfCircle(5))
#
# #soru5
# import turtle
# def draw_star(t, sz):
#     for i in range(5):
#         t.forward(sz)
#         t.right(144)
#
# wn = turtle.Screen()
# alex = turtle.Turtle()
# draw_star(alex, 100)
# #wn.mainloop()

#soru6
# import turtle
# def draw_square(t, sz):
#     for i in range(4):
#         t.forward(sz)
#         t.left(90)
#
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# alex = turtle.Turtle()
# alex.color("hotpink")
# alex.pensize(3)
#
# for i in range(5):
#     draw_square(alex, 20)
#     alex.penup()
#     alex.forward(40)
#     alex.pendown()
#
# wn.mainloop()

# import turtle
#
# def draw_square(t, sz):
#     for i in range(4):
#         t.forward(sz)
#         t.left(90)
#
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# alex = turtle.Turtle()
# alex.color("hotpink")
# alex.pensize(3)
#
# boyut = 20
# for i in range(5):
#     draw_square(alex, boyut)
#     alex.penup()
#     alex.backward(10)
#     alex.right(90)
#     alex.forward(10)
#     alex.left(90)
#     alex.pendown()
#     boyut += 20
#
# alex.penup()
# alex.backward(80)
# alex.right(90)
# alex.forward(70)
# alex.left(90)
#
# wn.mainloop()
