'''Write a Python program to accept a tuple of numbers and create a new tuple containing only the elements that occur exactly once, preserving their original order.
Example:
Input tuple: (2, 4, 2, 5, 7, 4, 9)
Output tuple: (5, 7, 9)
Rules: Don't use sets or dictionaries. Use loops and basic tuple operations.'''
t=eval(input("Enter a tuple:"))
l=list()
c=0
for i in t:
    for j in t:
        if i==j:
            c+=1
    if(c==1):
        l.append(i)
    c=0
t1=tuple(l)
print(t1)
