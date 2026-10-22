'''Create two lists: one containing all even numbers and the other containing all odd numbers.'''
l=eval(input("Enter a list of numbers:"))
e=list()
o=list()
for i in l:
    if(i%2==0):
        e.append(i)
    else:
        o.append(i)
print("EVEN:",e)
print("ODD:",o)