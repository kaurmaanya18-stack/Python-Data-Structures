'''Write a Python program to swap the keys and values of a dictionary.'''
d1=eval(input("Enter a dictionary: "))
d2={}
for i in d1:
    d2[d1[i]]=i
print("Dictionary with swapped keys and values:")
print(d2)