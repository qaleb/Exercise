'''1. Write a program which uses a while loop to sum the squares of integers (starting from 1) until the total exceeds
200. Print the final total and the last number to be squared and added.'''

number = 0
total = 0

while total < 200:
    number += 1
    total += number ** 2 #adds square of the present integer to the total
    
print('Total sum of the squares is:',total)
print('The final integer is:', number)