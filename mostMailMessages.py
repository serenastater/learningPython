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

file = raw_input("Enter file:")

if len(file) < 1:
    name = "mbox-short.txt"

handle = open(name)

from_lines = []
senders = {}

for line in handle:
    line = line.rstrip()
    if line.find('From ') == 0:
        line = line.split(' ')
        sender = line[1]
        if sender not in senders:
            senders[sender] = 1
        else:
            senders[sender] += 1

sender = ''
count = 0

for key in senders:
    if senders[key] > count:
        count = senders[key]
        sender = key

print "%s %s" % (sender, str(count))
