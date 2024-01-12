# Create a function with variable length of arguments

salary = input("Enter your salary: ")
name = input("Enter your name: ")
def show_employee(name, salary=9000):
    return name, salary

print(show_employee(name))
