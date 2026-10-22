def harshad(a):
    if a == 0:
        return 0

    c = a
    s = 0
    while a > 0:
        d = a % 10
        a = a // 10
        s += d

    if c % s == 0:
        return 1
    else:
        return 0

n = int(input("Enter a no.:"))
k = harshad(n)
if k == 1:
    print("HARSHAD/NIVEN NO.")
else:
    print("NOT HARSHAD/NIVEN NO.")
