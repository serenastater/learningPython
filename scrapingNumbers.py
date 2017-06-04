#  The program will use urllib to read the HTML from
# the data files below, and parse the data, extracting
# numbers and compute the sum of the numbers in the file:
#
# http://python-data.dr-chuck.net/comments_368407.html (Sum ends with 60)
#
# You are to find all the <span> tags in the file and pull
# out the numbers from the tag and sum the numbers.
#

import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

spans = soup('span')
total = 0
for span in spans:
    total = total + int(span.contents[0])
print total
