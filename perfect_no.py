def perfect(a):
    s=0
    for i in range(1,a):
        if(a%i==0):
            s+=i
    if(s==a):
        print("PERFECT NO.")
    else:
        print("NOT PERFECT NO.")
n=int(input("Enter no.:"))
perfect(n)
