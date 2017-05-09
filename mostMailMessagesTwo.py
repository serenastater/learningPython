# Write a program to read through the mbox-short.txt
# and figure out who has the sent the greatest number
# of mail messages. The program looks for 'From '
# lines and takes the second word of those lines as
# the person who sent the mail. The program creates
# a Python dictionary that maps the sender's mail
# address to a count of the number of times they
# appear in the file. After the dictionary is
# produced, the program reads through the dictionary
# using a maximum loop to find the most prolific
# committer.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

count = dict()

for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        for word in words:
            count[word] = count.get(word, 0) + 1

#Print list of tuples
#print count.items()

maxVal = None
maxKee = None
for kee,val in count.items():
    if maxVal == None or maxVal < val:
        maxVal = val
        maxKee = kee

print maxKee, maxVal

#This currently prints the word that occurs the most, not the sender who sends the most
