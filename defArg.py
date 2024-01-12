# Create a function with variable length of arguments: from pynative.com

salary = input("Enter your salary: ")
name = input("Enter your name: ")
def show_employee(name, salary=9000):
    return name, salary

print(show_employee(name))
