'''Create a new list containing each element only once, preserving the original order.'''
l = eval(input("Enter a list:"))
copy = []

for i in l:
    if i not in copy:
        copy.append(i)

print("The list with duplicates removed is:")
print(copy)