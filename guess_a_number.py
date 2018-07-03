#========== STEP 1 ==============================

# secret_number = 5
# print "I am thinking of a number between 1 and 10."

#========= Version 1 =========
# guess = int(raw_input("What's the number? "))
# if guess == secret_number:
#     print "Yes! You win"
# while guess != secret_number:
#     print "Nope, try again"
#     guess = raw_input("What's the number? ")
#     if guess == secret_number:
#         print "Yes! You win"



#============ Version 2 =================
# while True:
#     guess = int(raw_input("What's the number? "))
#     if guess == secret_number:
#         print "Yes! You win!"
#         break
#     else:
#         print "Nope, try again."


#==============  STEP 2 =========================

# secret_number = 5

# print "I am thinking of a number between 1 and 10."
# guess = raw_input("What's the number? ")

# secret_number = 5
# print "I am thinking of a number between 1 and 10."

# while True:
#     guess = int(raw_input("What's the number? "))
#     if guess == secret_number:
#         print "Yes! You win"
#         break
#     elif guess > secret_number:
#         print "%i is too high" % guess
#     elif guess < secret_number:
#         print "%i is too low" % guess


#=============  STEP 3 =====================
# import random
# secret_number = random.randint(1, 10)

# print "I am thinking of a number between 1 and 10."

# while True:
#     guess = int(raw_input("What's the number? "))
#     if guess == secret_number:
#         print "Yes! You win"
#         break
#     elif guess > secret_number:
#         print "%i is too high" % guess
#     elif guess < secret_number:
#         print "%i is too low" % guess


#==============  STEP 4 ====================
# import random
# secret_number = random.randint(1, 10)

# print "I am thinking of a number between 1 and 10."

# guess_left = 5

# while guess_left > 0:
#     guess = int(raw_input("What's the number? "))
#     guess_left -= 1
#     if guess == secret_number:
#         print "Yes! You win"
#         break
#     elif guess > secret_number:
#         print "%i is too high" % guess
#         if guess_left == 0:
#             print "You ran out of guesses!"
#         else:
#             print "You have %i guesses left." % guess_left
#     elif guess < secret_number:
#         print "%i is too low" % guess
#         if guess_left == 0:
#             print "You ran out of guesses!"
#         else:
#             print "You have %i guesses left." % guess_left
    


#===============  STEP 5 =====================

import random
secret_number = random.randint(1, 10)

print "I am thinking of a number between 1 and 10."

guess_left = 5

while guess_left > 0:
    guess = int(raw_input("What's the number? "))
    guess_left -= 1
    if guess == secret_number:
        print "Yes! You win"
        guess_left = 0
    else:
        print guess_hint(guess, secret_number)
        print show_guesses(guess_left)

    if guess_left == 0:
        play_again = raw_input("Do You Want to play again (Y or N)?").lower()
        if play_again == 'y':
            guess_left = 5
        else:
            print "Bye!"

#==============  Change code above to include functions  ======================
import random

init()

def init():
    low_number = 1
    high_number = 10
    secret_number = random.randint(low_number, high_number)
    max_guesses = 5
    print "I am thinking of a number between %i and %i." % (low_number, high_number)
    make_guess(secret_number, max_guesses)
    play_again()

def make_guess(secret_number, guesses_left):
    while guesses_left > 0:
        guess = int(raw_input('What\'s the number? '))
        guesses_left -= 1
        if guess == secret_number:
            print "Yes! You win"
            guesses_left = 0
        else:
            print guess_hint(guess, secret_number)
            print show_guesses(guesses_left)

def play_again():
    play_again = raw_input("Do You Want to play again (Y or N)?").lower()
    if play_again == 'y':
        init()
    else:
        print "Bye!"

def guess_hint(guess, secret_number):
    if guess > secret_number:
        return "%i is too high." % guess
    elif guess < secret_number:
        return "%i is too low." % guess

def show_guesses(guesses):
    if guesses == 0:
        return "You ran out of guesses"
    else:
        return "You have %i guesses left." % guesses