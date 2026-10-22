def neon(a):
    s=a**2
    d=0
    sum=0
    while s>0:
        d=s%10
        sum+=d
        s=s//10
    if(sum==a):
        print("NEON NO.")
    else:
        print("NOT NEON NO.")
n=int(input("Enter a no.:"))
neon(n)
