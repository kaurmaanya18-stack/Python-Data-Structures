s=input("Enter a string:")
s=s.lower()
l='abcdefghijklmnopqrstuvwxyz'
for i in l:
    if(i not in s):
        print(i)
c=0
for i in l:
    c=s.count(i)
    print(i,":",c)
    c=0
    