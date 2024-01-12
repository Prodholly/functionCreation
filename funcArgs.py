'''Create a function with variable length of arguments'''
def func1(*args):
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    print(f"Your name is {name} and your age is {age}")

func1()
