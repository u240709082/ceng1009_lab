import turtle


# -----------------------------------------------------------
# Soru 1
# -----------------------------------------------------------
def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"


print("--- Soru 1 Testleri ---")
test_marks = [95, 83, 79.9999, 70, 65, 50]
for m in test_marks:
    print("Mark:", m, "-> Grade:", get_grade(m))


# -----------------------------------------------------------
# Soru 4:
# -----------------------------------------------------------
def findHypot(a, b):
    return (a ** 2 + b ** 2) ** 0.5


print("\n--- Soru 4 Testleri ---")
print("Kenarlar 3 ve 4 -> Hipotenus:", findHypot(3, 4))
print("Kenarlar 5 ve 12 -> Hipotenus:", findHypot(5, 12))


# -----------------------------------------------------------
# Soru 2 & 3:
# -----------------------------------------------------------
def draw_bar(t, height):
    # Soru 2: Renk araliklari
    if height >= 200:
        t.color("blue", "red")
    elif height >= 100:
        t.color("blue", "yellow")
    else:
        t.color("blue", "green")

    t.begin_fill()
    t.left(90)
    t.forward(height)

    # Soru 3: Negatif degerlerde sayiyi cizginin ustune (0 eksenine) yazdirma
    if height < 0:
        t.penup()
        t.backward(height)
        t.write("  " + str(height))
        t.forward(height)
        t.pendown()
    else:
        t.write("  " + str(height))

    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.forward(10)


# Cizim
wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.pensize(3)

# Pozitif ve negatif
data = [-48, 117, 200, -240, 160, 260, -90]

for d in data:
    draw_bar(alex, d)

wn.mainloop()