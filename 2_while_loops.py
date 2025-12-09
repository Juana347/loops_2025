# Notes on while loops
# while loops execute some code WHILE some condition remains true

# name = input("Enter your name. ")
# if name == " ": # normal code. it only asks you once.
#     print("You did not enter your name.")
# else:
#     print(F"Hello {name}.")


# name = input("Enter your name. ")
# while name == "": # prompts user to repeatedly type in a name
#     print("You did not enter your name.")
#     name = input("Enter your name. ")
# print(F"Hello {name}.")


# name = input("Enter your name. ")
# while name == "": # infinite loop. no chance to escape.
#     print("You did not enter your name.")
# print(F"Hello {name}.")


# age = int(input("Enter your age. "))
# while age < 0:
#     print("Age can't be negative.")
#     age = int(input("Enter your age.")) #This is not infinite. You enter a positive number to stop.
# print(f"You are {age} years old.")


# food = input("Enter a food you like. (q to quit.) ") #Use q to escape the code.
# list = []
# while not food == "q":
#     print(f"You like {food}.")
#     food = input("Enter another food you like. (q to quit.) ")
#     list.append(food)
#     print(list)
# print("Bye.")


# num = int(input("Enter a number between 1 - 10 : "))
# while num < 1 or num > 10:
#     print(f"{num} is not valid.")
#     num = int(input("Enter a number between 1 - 10 : "))
# print(f"Your number is {num}.")


# Given:
colors = ["red", "blue", "green", "yellow", "purple"]

# Challenge:
# Use a while loop to print each color UNTIL you find "yellow".
# Do NOT print "yellow" — stop before it.
index = 0
while index < len(colors):
    if colors[index] == "yellow":
        break
    print(colors[index])
    index += 1 # increments the index to avoid infinite loops
