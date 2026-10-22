'''Rotate a list by one position without using slicing'''
l=eval(input("Enter a list of nos:"))
l1=list()
l1.append(l[-1])
l.remove(l[-1])
l1.extend(l)
print(l1)