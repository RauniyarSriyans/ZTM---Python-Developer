# Regular Expressions

# re is a built in module for regular expressions
import re

string_text = 'search inside of this text please this!'

# a will be NonType object if the pattern is not found
a = re.search('this', string_text)

# prints where the pattern occurs
print(a.span())
# prints the starting index of where the pattern occurs
print(a.start())
# prints the ending index of where the pattern occurs
print(a.end())
# prints the substring that was matched by the regular expression
print(a.group())

# we can also define a pattern initially and use that pattern to do the search as follows:
pattern = re.compile('this')
b = pattern.search(string_text)
print(b.group())

# here, one thing to notice is that the second pattern is not being recognized. To do so, use findall. 
# returns a list of all found patterns
c = pattern.findall(string_text)
print(c)

# also, there is something called fullmatch(). This requires that the query string completely matches the regular expression. 
text_2 = 'hello!'
pattern_2 = re.compile('hello!')
# returns a re object, None if not found
d = pattern_2.fullmatch(text_2)
# again, group is used to print the actual found string
print(d.group())

# there's also something called match() which checks for substrings rather than fullmatch. 
text_3 = 'hello! my name is Shree'
pattern_3 = re.compile('hello!')
# returns a re object, None if not found
e = pattern_3.match(text_3)
# again, group is used to print the actual found string
print(e.group())

# let's look at some complex patterns now
# look at https://regex101.com/
email_pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
test_email = 'rauniyar@princeton.edu'
a = email_pattern.match(test_email)
print(a.group())
