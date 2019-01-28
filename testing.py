'''s = "abracadabra"

print(len(s))
print(s.index("a"))

print(s[0])
print(s[3:5])

l = ['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a']
s = "".join(l)
print(s)

pet_list = "the quick brown fox jumped over the lazy dog".split()
print(pet_list)

s = "antidisestablishmentarianism"
s2 = "".join(sorted(s))
print(s2)

# Write a program which sums the integers from 1 to 10 using a for loop 
# (and prints the total at the end).
total = 0
for i in range(1,11):
    total += i
print(total)

# Write a program which finds the factorial of a given number.
number = int(input("Enter number:"))
for i in reversed(range(1,number)): # or you can reverse the iteration with reversed() function
    number *= i
print(number)'''

'''WEEKDAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
# now we iterate over each day in the timetable
for day in timetable:
# and over each timeslot in each day
    for i, event in enumerate(day):
        if event: # if the slot is not an empty string
            print("%s at %02d:00 -- %s" % (WEEKDAYS[day], i, event))
#How to use continue and break
# 1. Continue
for x in range(1, 10 + 1): # this will count from 1 to 10
    if x == 5:
        continue
    print(x)

# 2. Break
x = 1
while x <= 10:
    if x == 5:
        break
    print(x)
    x += 1

#The program requests details from the user 

fname = input("Enter your first name:")
lname = input("Enter your last name(Surname):")
age = input("Enter your age (Years):")
height = input("Enter your height(ft):")
weight = input("Enter your weight (Kgs):")

print("You have entered the following details:")
print("Name: %s %s"%(fname.upper(),lname.upper()))
print("Age:", age)
print("Height:",height)
print("Weight:",weight)'''

#It can be simplified using a loop

person = {}

for prop in ["first name", "last name", "age", "height", "weight"]:
    person[prop] = input("Please enter your %s: " % prop.capitalize())

print("\nKINDLY CONFIRM YOUR DETAILS BEFORE SUBMIT.\n")

for detail in person.keys():
    print("%s: %s"%(detail.capitalize(),person[detail].capitalize()))