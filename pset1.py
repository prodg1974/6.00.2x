s='someotherword'
lcount=0
vowels=['a','e','i','o','u']
for letter in s:
    if letter in vowels:
        lcount+=1
print 'Number of vowels:', str(lcount)