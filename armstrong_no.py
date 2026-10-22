#A number equal to the sum of its own digits, each raised to the power of the total number of digits is an Armstrong No.
def arm(a):
    c=str(a)
    l=len(c)
    c=int(c)
    armstrong=0
    d=0
    while a>0:
        d=a%10
        a=a//10
        armstrong+=(d**l)
    if(armstrong==c):
        print("ARMSTRONG NO.")
    else:
        print("NOT AN ARMSTRONG NO.")
n=int(input("Enter a no:"))
arm(n)

        