'''Write a program that accepts a sentence and reports the frequency of every distinct character and treating uppercase and lowercase as equivalent.'''
s=input("Enter a string: ")
c=0
L=[]
i=""
for i in s:
    if(i in L):
        continue
    else:
        for j in s:
            if i==j:
                c+=1
        print("The frequency of",i,":",(c))
        c=0
        L.append(i)

