'''Accept a list of numbers and print the second-largest distinct element with using sort() or max()'''
l=eval(input("Enter a list:"))
s=set(l)
l=list(s)
max1=max(l)
l.remove(max1)
max2=max(l)
print("2nd maximum element in list is",max2)
'''Accept a list of numbers and print the second-largest distinct element without using sort() or max()'''
l = eval(input("Enter a list:"))
l = list(set(l))

if len(l) < 2:
    print("No second-largest distinct element")
else:
    max1 = l[0]

    for i in range(1, len(l)):
        if l[i] > max1:
            max1 = l[i]

    l.remove(max1)

    max2 = l[0]
    for i in range(1, len(l)):
        if l[i] > max2:
            max2 = l[i]

    print("2nd maximum element in list is", max2)

