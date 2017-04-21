# Write code using find() and string slicing (see
# section 6.10) to extract the number at the end
# of the line below. Convert the extracted value
# to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475";

firstDigit = text.find('0')
lastDigit = text.find('5')

number = text[firstDigit:lastDigit+1]
finalNumber = float(number)
print finalNumber
