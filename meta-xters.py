import re

# ^ character --- match any character that begins with the xters in the pattern
regex = re.compile('^abc')
print(regex.match('abc')) # this will match
print(regex.match('abbecdd')) # will not match

# | character --- this is the OR xter --- matches any of the xter(s) seperated by the | sign
regex = re.compile('a|b')
print(regex.match('a')) # this will match
print(regex.match('b')) # this will match
print(regex.match('c')) # will not match

print(regex.match('abc')) # this will match

# it can also be used to match a set of xters
regex = re.compile('abc|xyz')
print(regex.match('abcdef')) # this will match
print(regex.match('xyz')) # this will match
print(regex.match('cdebd')) # will not match

# $ character --- matches the end of line --- any set of xters ending with the xters before the $ sign
regex = re.compile('ing$')
print(regex.match('ing')) # this will match