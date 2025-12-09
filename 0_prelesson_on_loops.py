Loops video  https://www.youtube.com/watch?v=KWgYha0clzw&t=1s&pp=ygUOYnJvIGNvZGUgbG9vcHM%3D
While loops  


#for loops execute a block of code a fixed number of time.

for x in range(1, 11): # counts 1-10
    print(x)

for x in reversed(range(1, 11)): # counts in reverse
    print(x)
print("HAPPY NEW YEAR!")

for x in range(1, 11, 2): # counts by twos
    print(x)

credit_card = "1234-5678-9012-3456"

for x in credit_card: # counts the numbers
    print(x)

for x in range(1, 21): # continue skips over number 13
    if x == 13:
        continue
    else:
        print(x)

for x in range(1, 21): # break ends when you hit 12 because x doesn't become 13
    if x == 13:
        break
    else:
        print(x)


this is for 1: 

# Example Practice:
# Given this list of fruits:
fruits = ["apple", "banana", "cherry", "date"]

# Challenge:
# Use a for loop to print each fruit on a new line.
print(fruits[0])
print(fruits[1])
print(fruits[2])
for fruit in fruits:
    print(fruit)
# i just worked with loops

# Given a list of school subjects:
subjects = ["Math", "Science", "History", "Art"]
for subject in subjects:
    print(subject)

# print out each subject but stop when you reach "History"
for x in (subjects):
    if x == "History":
        break
    else:
        print(x)

# skips over "Science"
for x in (subjects):
    if x == "Science":
        continue
    else:
        print(x)

# Challenge:
# Use a for loop and range to print each subject along with its index:
# Example output: "Subject 0: Math"
for i in range(len(subjects)):
    print(f"Subject {i}: {subjects[i]}")


# Given:
numbers = [5, 10, 15, 20]
# Challenge:
# Use a for loop to add all the numbers and print the total.
total = 0
for number in numbers:
    total += number
print(total)
# first time total = 0
# second time total = 0 + 5
# third time total = 5 + 10
# fourth time total = 15 + 15
# fifth time total = 30 + 20 

this is for 2: 

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
