# # In this assignment you will write a Python program that
# # expands on http://www.pythonlearn.com/code/urllinks.py.
# # The program will use urllib to read the HTML from the
# # data files below, extract the href= vaues from the anchor
# # tags, scan for a tag that is in a particular position
# # relative to the first name in the list, follow that link
# # and repeat the process a number of times and report the
# # last name you find.
#
# Start at: http://python-data.dr-chuck.net/known_by_Kirstie.html
# Find the link at position 18 (the first name is 1). Follow that
# link. Repeat this process 7 times. The answer is the last name
# that you retrieve.
# Hint: The first character of the name of the last page that you
# will load is: A

import urllib
from BeautifulSoup import *

url = raw_input('Enter URL:')
# URL is: http://python-data.dr-chuck.net/known_by_Kirstie.html
repeats = int(raw_input('Enter count:'))
position = int(raw_input('Enter position:'))

print url

for i in range(repeats):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    url = tags[position-1].get('href', None)
    print url
