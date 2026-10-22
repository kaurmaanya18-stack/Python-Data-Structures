'''Write a Python program to accept 10 numbers from the user and store them in a tuple. Then:
1. Print the largest and smallest elements.
2. Count how many times a number entered by the user occurs in the tuple.
3. Print a new tuple containing only the even numbers.'''
t=eval(input("Enter a tuple:"))
n=int(input("Enter no.:"))
print("The largest no. in the tuple:",max(t))
print("The smallest no. in the tuple:",min(t))
print("The no. of times",n,"appeared in",t,": ",t.count(n))
l=[]
for i in t:
    if(i%2==0):
        l.append(i)
te=tuple(l)
print("A new tuple containing only the even numbers:",te)