
#########################################################################

# Write a program that prints the numbers from 1 to a given number n. 
# But for multiples of 3, print "Fizz" instead of the number, 
# and for the multiples of 5, print "Buzz". 
# For numbers which are multiples of both 3 and 5, print "FizzBuzz".
# If the number doesn't go with any of the above conditions print out the number

def fizzBuzz(number):
    for i in range(1, number + 1):
        stringA = ""
        if(i % 3 == 0):
            stringA += "Fizz"
        if(i % 5 == 0):
            stringA += "Buzz"
        if(stringA):
            print(stringA)
        else:
            print(i)
    
#fizzBuzz(15)