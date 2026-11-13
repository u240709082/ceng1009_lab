#etkinlik1
def is_odd(n):
    if n % 2 != 0:
        return True
    else:
        return False

#etkinlikk2

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

#etkinlikk3

def print_triangular_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
        print(i, "\t", total)

#etkinlik44
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


#etk5
def reverse_str(s):
    res = ""
    for ch in s:
        res = ch + res
    return res
#etkinliik6
def remove_all(sub, s):
    res = ""
    i = 0
    while i < len(s):
        if s[i:i + len(sub)] == sub:
            i = i + len(sub)
        else:
            res = res + s[i]
            i = i + 1
    return res
#etkinlik7

def encrypt(msg, mapping):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    for ch in msg.upper():
        if ch in alphabet:
            idx = alphabet.index(ch)
            res = res + mapping[idx]
        else:
            res = res + ch
    return res
#etkinlik8
def remove_dups(s):
    res = ""
    for ch in s:
        if ch not in res:
            res = res + ch
    return res

print(is_odd(5))
print(is_leap_year(2024))
print_triangular_numbers(5)
print(is_prime(7))
print(reverse_str("python"))
print(remove_all("an", "banana"))
print(encrypt("HELLO", "QWERTYUIOPASDFGHJKLZXCVBNM"))
print(remove_dups("mississippi"))

