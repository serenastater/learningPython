# Write a program that prompts for a file name,
# then opens that file and reads through the file,
# and print the contents of the file in upper case.

fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.upper().rstrip()
    print line
