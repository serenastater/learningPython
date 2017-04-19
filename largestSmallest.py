# Write a program that repeatedly prompts a user for integer
# numbers until the user enters 'done'. Once 'done' is entered,
# print out the largest and smallest of the numbers. If the user
# enters anything other than a valid number catch it with a
# try/except and put out an appropriate message and ignore the
# number. Enter the numbers from the book for problem 5.1 and
# Match the desired output as shown.

# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.33333333333

largest = None
smallest = None

try:
    while True:
        inp = raw_input("Enter a number: ")
        num = float(inp)
        if num == "done":
            break
        elif num < smallest:
            smallest = num
        elif num > largest:
            largest = num
        print num, smallest, largest
except:
    if type(num) != int:
        print("Invalid input")


#print "Maximum", largest
