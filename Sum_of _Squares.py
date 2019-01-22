number = 1
total = 0
while total < 200:
    total += (number*number) #adds square of the present integer to the total
    number += 1
print('Total sum of the squares is: ',total)
print('The final integer is: ', number)