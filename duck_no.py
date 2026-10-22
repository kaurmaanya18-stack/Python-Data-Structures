def duck(a):
    a=str(a)
    if ("0" in a):
        print("DUCK NO.")
    else:
        print("NOT DUCK NO.")
n=int(input("Enter a no.:"))
duck(n)