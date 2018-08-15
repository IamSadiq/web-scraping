import re

# re.compile(pattern) -- returns a regex onject
# regex = re.compile('a')

# regex.match(string to match) --- returns a match if founf else None
# print(regex.match('ab'))

# character class
# regex = re.compile('[a-zA-Z]')
regex = re.compile('[^a-zA-Z]')
regex = re.compile('[+]')
print(regex.match('+'))

# Metacharacters --- . ^ : $ * + ? { } \ | [ ] ( )
# All metacharacters lose their meaning inside a character class