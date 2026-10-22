def happy(a):
    while a != 1 and a != 4:
        s = 0
        while a > 0:
            d = a % 10
            s += d ** 2
            a = a // 10
        a = s

    if a == 1:
        print("HAPPY NO.")
    else:
        print("NOT HAPPY NO.")

n = int(input("Enter a no.:"))
happy(n)
