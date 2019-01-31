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
try:
    number = int(input("Enter number:"))
    for i in reversed(range(1,number)): # or you can reverse the iteration with reversed() function
        number *= i
    print(number)
except ValueError:
    print("Input must be a positive integer! Try again.")'''

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
print("Weight:",weight)

#It can be simplified using a loop

person = {}

for prop in ["first name", "last name", "age", "height", "weight"]:
    person[prop] = input("Please enter your %s: " % prop.capitalize())

print("\nKINDLY CONFIRM YOUR DETAILS BEFORE SUBMIT.\n")

for detail in person.keys():
    print("%s: %s"%(detail.capitalize(),person[detail].capitalize()))

# Try and except error handling

try:
    dividend = int(input("Please enter the dividend: "))
    divisor = int(input("Please enter the divisor: "))
    print("%d / %d = %f" % (dividend, divisor, dividend/divisor))
except ValueError:
    print("The divisor and dividend have to be numbers!")
except ZeroDivisionError:
    print("The dividend may not be zero!")

# Here we keep asking the user for input until the input is correct
# with checks
n = None

while n is None:
    s = input("Please enter an integer: ")
    if s.lstrip('-').isdigit():
        n = int(s)
    else:
        print("%s is not an integer." % s)

# with exception handling
n = None

while n is None:
    try:
        s = input("Please enter an integer: ")
        n = int(s)
    except ValueError:
        print("%s is not an integer." % s)

# try & except and else & continue statements

try:
    name = input("Remind me your name, please:")
except valueError:
    print("\nI didn't really understand that, what's your again?")
else:
    print("\nAw, it's you %s! Welcome back."%name.capitalize())
finally:
    print("It was nice interacting with you.")

class Student:
    def __init__(self, name, student_number):
        self.name = name
        self.student_number = student_number
        self.classes = []
    def enrol(self, course_running):
        self.classes.append(course_running)
        course_running.add_student(self)
class Department:
    def __init__(self, name, department_code):
        self.name = name
        self.department_code = department_code
        self.courses = {}
    def add_course(self, description, course_code, credits):
        self.courses[course_code] = Course(description, course_code, credits, self)
        return self.courses[course_code]
class Course:
    def __init__(self, description, course_code, credits, department):
        self.description = description
        self.course_code = course_code
        self.credits = credits
        self.department = department
        self.department.add_course(self)

        self.runnings = []
    def add_running(self, year):
        self.runnings.append(CourseRunning(self, year))
        return self.runnings[-1]
class CourseRunning:
    def __init__(self, course, year):
        self.course = course
        self.year = year
        self.students = []
    def add_student(self, student):
        self.students.append(student)
        
maths_dept = Department("Mathematics and Applied Mathematics", "MAM")
mam1000w = maths_dept.add_course("Mathematics 1000", "MAM1000W", 1)
mam1000w_2013 = mam1000w.add_running(2013)
bob = Student("Bob", "Smith")
bob.enrol(mam1000w_2013)

# Sometimes the exception message contains useful information which we want to display to the user. In order to access
# the message, we need to be able to access the exception object. We can assign the object to a variable that we can use
# inside the except clause like this

try:
    age = int(input("Please enter your age: "))
except ValueError as err:
    print("You entered incorrect age input: %s" % err)'''

#We can raise exceptions ourselves using the raise statement:
try:
    age = int(input("Please enter your age: "))
    if age < 0:
        raise ValueError("%d is not a valid age. Age must be positive or zero."% age)
except ValueError as err:
    print("You entered incorrect age input: %s" % err)
else:
    print("I see that you are %d years old." % age)