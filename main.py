print "Hi and Welcome to the FizzBuzz game!"

guess = raw_input("Please enter a number between 1 and 100: ")

guess = int (guess)

for number in range( 1, guess + 1 ):
    if number % 3 == 0 and number % 5 == 0:
        print "FizzBuzz!"
    elif number % 3 == 0:
        print "Fizz!"
    elif number % 5 == 0:
        print "Buzz!"
    else:
        print number
