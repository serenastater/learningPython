# Write a program to read through the mbox-short.txt
# and figure out the distribution by hour of the day
# for each of the messages. You can pull the hour out
# from the 'From ' line by finding the time and then
# splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print
# out the counts, sorted by hour as shown below.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

count = dict()

for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        # print line
        words = line.split()
        time = words[5]
        # print time
        hour = time[0:time.find(":"):1]
        # print hour
        # if hour not in count:
        #     count[hour] = 1
        # else:
        #     count[hour] += 1
        count[hour] = count.get(hour,0) + 1
        # print count
list = count.keys()
# print list
list.sort()
for key in list:
    print key, count[key]







        # for word in words:
        #     count[word] = count.get(word, 0) + 1
        #     print count
