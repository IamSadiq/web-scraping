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