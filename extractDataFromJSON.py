# In this assignment you will write a Python program
# somewhat similar to http://www.pythonlearn.com/code/json2.py.
# The program will prompt for a URL, read the JSON data from
# that URL using urllib and then parse and extract the comment
# counts from the JSON data, compute the sum of the numbers
# in the file and enter the sum below:
#
# URL: http://python-data.dr-chuck.net/comments_368408.json

import urllib
import json

url = raw_input('Enter URL:')
# URL is: http://python-data.dr-chuck.net/comments_368408.json

handle = urllib.urlopen(url)
data = handle.read()

info = json.loads(data)

counts = []

comments = info["comments"]

for comment in comments:
    counts.append(comment['count'])

print sum(counts)
