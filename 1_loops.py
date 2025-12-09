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