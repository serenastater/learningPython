# # In this assignment you will write a Python program somewhat
# # similar to http://www.pythonlearn.com/code/geoxml.py. The
# # program will prompt for a URL, read the XML data from that
# # URL using urllib and then parse and extract the comment
# # counts from the XML data, compute the sum of the numbers
# # in the file.
#
# Data: http://python-data.dr-chuck.net/comments_368404.xml
#
# Data Format and Approach
# The data consists of a number of names and comment counts in
# XML as follows:
#
# <comment>
#   <name>Matthias</name>
#   <count>97</count>
# </comment>
#
# You are to look through all the <comment> tags and find the
# <count> values and sum the numbers. The closest sample code that
# shows how to parse XML is geoxml.py.
#
# To make the code a little simpler, you can use an XPath selector
# string to look through the entire tree of XML for any tag named
# 'count' with the following line of code:
# 
# counts = tree.findall('.//count')
#
# Take a look at the Python ElementTree documentation and look
# for the supported XPath syntax for details. You could also work
# from the top of the XML down to the comments node and then loop
# through the child nodes of the comments node.
