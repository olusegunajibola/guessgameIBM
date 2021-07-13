import random
num = random.randint(1,10)
guess = int(input('Guess a number from 1 to 10. My number is '))
if guess < num:
    print("Your guess is smaller than the actual number.")
elif guess > num:
    print("Your guess is greater than the actual number.")
else:
    print("You guessed it correctly!")
chances = 2     # Chances is 2 since the first guess was used in the input above
while guess != num and chances: #this checks that you guessed wrongly while having a chance
    chances -= 1
    guess = int(input("Wrong guess. Try again! My number is "))
    if guess < num:
        print("Your guess is smaller than the actual number.")
    elif guess > num:
        print("Your guess is greater than the actual number.")
    else:
        print("Congratulations!!! You guessed it correctly!")
    if guess != num and chances ==0:
        print("You have used all your 3 chances.\n")
        print("The number is",num, ".")

# git add .
# git commit -m 'message'
# git push origin "name of branch"
# git pull origin "name of branch"
