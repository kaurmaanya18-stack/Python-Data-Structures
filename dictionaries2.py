'''Write a Python program to accept two dictionaries and merge them into a new dictionary.
Rules:
- If a key appears in both dictionaries, add their values together.
- Don't modify the original dictionaries.
- Use loops and basic dictionary operations.'''
d1=eval(input("Enter a dictionary:"))
d2=eval(input("Enter a dictionary:"))
d3={}
for i in d1:
    for j in d2:
        if i==j:
            d3[i]=d1[i]+d2[j]
for i in d1:
    if i not in d3:
        d3[i]=d1[i]
    else:
        continue
for i in d2:
    if i not in d3:
        d3[i]=d2[i]
    else:
        continue