'''Write a Python program to find the key with the maximum value in a dictionary.'''
d = eval(input("Enter a dictionary:"))

max1 = 0
key1 = ""

for i in d:
    if d[i] > max1:
        max1 = d[i]
        key1 = i

print("Maximum Value:", max1)
print("Key:", key1)
