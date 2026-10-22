'''Write a Python program to accept a string and count the frequency of each character in a dictionary.
Conditions:
- Ignore capitalization.
- Don't use count() or collections.Counter.
- Use a loop and a dictionary.'''
s=input("Enter a string: ")
s=s.lower()
l=list()
d=dict()
c=0
for i in s:
    if i not in l:
        for j in s:
            if i==j:
                c+=1
        d[i]=c
        c=0
        l.append(i)
    else:
        continue
print(d)