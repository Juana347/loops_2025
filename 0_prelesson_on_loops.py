#Loops video  https://www.youtube.com/watch?v=KWgYha0clzw&t=1s&pp=ygUOYnJvIGNvZGUgbG9vcHM%3D
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