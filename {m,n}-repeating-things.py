import re

# recap 
# * ---- returns a match for 0 to infinity time occurence of the previous character
# + ---- returns a match for 1 to 1 time occurence of the previous character
# ? ---- returns a match for 0 to 1 time occurence of the previous character

# {m,n} --- where 'm' & 'n' are integer values --- this qualifier means, there must be atleast 'm' repetitions and at most 'n'
regex = re.compile('a{2,4}') # this says to match only aa, aaa or aaaa and onwards
print(regex.match('a')) # this will fail
print(regex.match('aa')) # this will match
print(regex.match('aaa')) # this will match
print(regex.match('aaaa')) # this will match
print(regex.match('aaaaa')) # this will match

# we can use the {m,n} regular expression to mimic the * + and ? xters as such:

# * xter --- {0,}
pattern = re.compile('a{0,}')
print(pattern.match('')) # will match
print(pattern.match('aaaaaaaaaaa')) # will match

# + xter --- {1,}
pattern = re.compile('a{1,}')
print(pattern.match('')) # will fail
print(pattern.match('aaaaaaaaaaa')) # will match

# ? xter --- {0,1}
pattern = re.compile('a{0,1}')
print(pattern.match('')) # will match
print(pattern.match('a')) # will match
print(pattern.match('aaaaa')) # will match only the first xter, once