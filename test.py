username = input("Enter your username: ")
age = input("Enter your age: ")
while not age.isdigit() or int(age) <= 0:
    print("Invalid age. Please enter a positive number.")
    age = input("Enter your age: ")

if int(age) < 18:
    print("Hi " + username + "! Welcome to the program.")
elif int(age) < 36:
    print("Hello " + username + "! Welcome to the program.")
elif int(age) < 54:
    print("Welcome " + username + "! Welcome to the program.")
elif int(age) < 72:
    print("It is a pleasure to meet you, " + username + "! Welcome to the program.")
else:
    print("I welcome thee, " + username + "! Welcome to the program.")