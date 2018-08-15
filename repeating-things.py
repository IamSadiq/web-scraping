import re

# * character -- this specifies that the previous character can be matched zero or more times, instead of just once
# lower-limit is 0 and upper-limit is infinity

regex = re.compile('a*')  # match any number of 'a' occurences from zero to infinte
print(regex.match('')) # lower limit -- 0 occurence
print(regex.match('bdbdbbjdy'))
print(regex.match('aaaaaaaaaaaaaa'))
 
regex = re.compile('[a-c]*') # match any number of abc occurences from zero to infinte in any order e.g cababcca
print(regex.match('')) # lower limit -- 0 occurence
print(regex.match('abc'))
print(regex.match('cababcca'))

regex = re.compile('.*')
print(regex.match('')) # lower limit -- 0 occurence
print(regex.match('.jpg'))

regex = re.compile('.*') # match any number of '.' occurences from zero to infinte in any order e.g .jpg or .....png
print(regex.match('')) # lower limit -- 0 occurence
print(regex.match('.jpg'))
print(regex.match('.....png'))

# + character --- this specifies that the previous character can be matched 1 - infinity times
# lower-limit is 1 and upper-limit is infinity
regex = re.compile('[a-h]+')
print(regex.match('')) # this will fail to match
print(regex.match('abdhdcde'))

# ? character --- this specifies that the previous character can be matched 0 to 1 time
# min ---0 and max --- 1

regex = re.compile('a?b')
print(regex.match('')) # this will fail to match -- a is 0 and b is 0
print(regex.match('b')) # Match -- a is 0 and b is 1
print(regex.match('ab')) # Match -- a is 0 and b is 1