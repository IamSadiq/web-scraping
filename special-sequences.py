import re

# special sequences
# \d --- matches any decimal digit [0-9]
regex = re.compile('\d')
# print(regex.match('6352778'))

# \D --- matches any non-digit character [^0-9]
regex = re.compile('\D')
# print(regex.match('adfdfg'))

# \s --- matches any whitespace character
regex = re.compile('\s')
# print(regex.match(' hello you'))

# \w --- matches any alphanumeric character [a-zA-Z0-9_]
regex = re.compile('\w')
# print(regex.match('_a664'))

# \W --- matches any non-alphanumeric character [^a-zA-Z0-9_]
regex = re.compile('\W')
# print(regex.match('*'))