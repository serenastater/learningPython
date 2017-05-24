import re

name = raw_input("Enter file:")
if len(name) < 1 : name = "realRegexSumData.txt"
handle = open(name)

numbers = []

for line in handle:
    line = line.rstrip()
    number = re.findall('[0-9]+', line)
    numbers.extend(number)

integer = [int(x) for x in numbers]
total = sum(integer)
print total
