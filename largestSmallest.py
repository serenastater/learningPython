# Write a program that repeatedly prompts a user for integer
# numbers until the user enters 'done'. Once 'done' is entered,
# print out the largest and smallest of the numbers. If the user
# enters anything other than a valid number catch it with a
# try/except and put out an appropriate message and ignore the
# number. Enter the numbers from the book for problem 5.1 and
# Match the desired output as shown.

largest = None
smallest = None
total = 0

while True:
    inp = raw_input("Enter a number: ")
    if inp == "done" : break
    if len(inp) < 1 : break
    try:
        num = int(inp)
    except:
        print "Invalid input"
        continue
    if smallest is None:
        smallest = num
        total = smallest + num
    if num > largest:
        largest = num
        total = largest + num
    elif num < smallest:
        smallest = num
        total = smallest + num

print "Total is", total
print "Maximum is", largest
print "Minimum is", smallest
