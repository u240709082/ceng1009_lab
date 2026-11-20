#etknlkkk1
my_list = [76, 92.3, "hello", True, 4, 76]

my_list.append("apple")
my_list.append(76)
my_list.insert(3, "cat")
my_list.insert(0, 99)
print(my_list.index("hello"))
print(my_list.count(76))
my_list.remove(76)
my_list.pop(my_list.index(True))
print(my_list)


#etknlk2
def sum_of_squares(xs):
    total = 0
    for x in xs:
        total = total + x * x
    return total


#etkinlik3
def sum_even(xs):
    total = 0
    for x in xs:
        if x % 2 == 0:
            total = total + x
    return total


#etknlk4

def count_words(words):
    count = 0
    for w in words:
        if len(w) == 5:
            count = count + 1
    return count


#etkinlk5
def sum_until_even(xs):
    total = 0
    for x in xs:
        if x % 2 == 0:
            break
        total = total + x
    return total


#etlinmlik6
def count_until_sam(words):
    count = 0
    for w in words:
        count = count + 1
        if w == "sam":
            break
    return count


#etkinlikk7
def replace(s, old, new):
    parts = s.split(old)
    result = new.join(parts)
    return result


#etknlk8
def max(xs):
    biggest = xs[0]
    for x in xs:
        if x > biggest:
            biggest = x
    return biggest

#test
print(sum_of_squares([2, 3, 4]))
print(sum_even([1, 2, 3, 4, 5, 6]))
print(count_words(["apple", "cat", "hello", "python"]))
print(sum_until_even([1, 3, 5, 4, 7]))
print(count_until_sam(["ali", "veli", "sam", "ayse"]))
print(replace("Mississippi", "i", "I"))
s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
print(replace(s, "om", "am"))
print(replace(s, "o", "a"))
print(max([4, 12, 7, 25, 3]))