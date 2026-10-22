'''Write a Python program to create a new dictionary containing only the entries whose values are greater than 50.'''

d=eval(input("Enter a dictionary:"))
d2={}

for i in d:
    if d[i]>50:
        d2[i]=d[i]

print("Dictionary with values greater than 50:")
print(d2)

