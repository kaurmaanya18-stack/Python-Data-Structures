a=int(input("Enter a no:"))
b=int(input("Enter a no:"))
c=int(input("Enter a no:"))
rev1=0
rev2=0
rev3=0
d=0
c1=a
c2=b
c3=c
while a>0:
    d=a%10
    a=a//10
    rev1=rev1*10+d
d=0
while b>0:
    d=b%10
    b=b//10
    rev2=rev2*10+d
d=0
while c>0:
    d=c%10
    c=c//10
    rev3=rev3*10+d
if(c1==rev1):
    print("PALINDROME")
else:
    print("NOT PALLINDROME")
if(c2==rev2):
    print("PALINDROME")
else:
    print("NOT PALLINDROME")
if(c3==rev3):
    print("PALINDROME")
else:
    print("NOT PALLINDROME")

