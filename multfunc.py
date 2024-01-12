#  Return multiple values from a function

p = int(input("input a number: "))
b = int(input("input another number:"))
def calculation(p, b):

    sum = p + b
    sub = p - b
    return sum, sub

print(calculation(p, b))
