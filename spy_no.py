def spy(a):
    d=0
    s=0
    p=1
    while a>0:
        d=a%10
        a=a//10
        s+=d
        p*=d
    if(s==p):
        return 1
    else:
        return 0
n=int(input("Enter a no.:"))
result=spy(n)
if(result==1):
    print("SPY NO.")
else:
    print("NOT SPY NO.")