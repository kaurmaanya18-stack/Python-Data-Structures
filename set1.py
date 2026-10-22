'''Write a Python program to accept two sets of integers from the user and display:
1. The union of the two sets.
2. The intersection of the two sets.
3. The elements present in the first set but not in the second.
4. The elements present in either set, but not in both.'''
s=eval(input("Enter a set:"))
s=set(s)
m=eval(input("Enter a set:"))
m=set(m)
u=s|m
i=s&m
s_m=s-m
m__s=s^m
print("Union:",u)
print("Intersection:",i)
print("1st set - 2nd set:",s_m)
print("Symmetric difference of sets",m__s)