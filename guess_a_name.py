'''Write a program which keeps prompting the user to guess a word. The user is allowed up to ten guesses –
write your code in such a way that the secret word and the number of allowed guesses are easy to change. Print
messages to give the user feedback.'''

name = 'yellow'
trials = 9
guess = input("Guess my favorite colour (You ave 10 attempts!):")
#responses = ['I like that but my favorite', 'You are close but not yet', 'Nope, not that one']

while guess != name and trials > 0:    
    guess = input("You are close but not yet!, Try gain (%d attempts remaining): "%trials)
    trials -= 1

if(guess == name):
    print("You got it right, my favorite colour is", name)
else:
    print("My favorite color is",name)