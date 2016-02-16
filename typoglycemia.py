'''
Daily Programmer
2015-Nov-25
Python 2.7
Chris

https://www.reddit.com/r/dailyprogrammer/comments/3s4nyq/20151109_challenge_240_easy_typoglycemia/

Input Description
Any string of words with/without punctuation.

Output Description
A scrambled form of the same sentence
but with the word's first and last letter's positions intact.
'''

import re, random

input = """According to a research team at Cambridge University,
it doesn't matter in what order the letters in a word are,
the only important thing is that the first and last letter be in the right place.
The rest can be a total mess and you can still read it without a problem.
This is because the human mind does not read every letter by itself, but the word as a whole.
Such a condition is appropriately called Typoglycemia."""

# need to remove punctuation

words = re.findall(r"[\w']+|[.,!?;]", input)
words2 = []
strStr = ""

for word in words:
    if len(word) > 1:
        scrWord = word[0] + ''.join(random.sample(word[1:-1], len(word)-2)) + word[-1]
        strStr += " " + scrWord
    elif len(word) <= 1:
        if re.search("[a-zAz]", word):
            strStr += " " + word
        else:
            strStr += word

print strStr
