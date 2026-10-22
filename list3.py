'''Print each distinct element and its number of occurrences without using count'''
l=eval(input("Enter a list:"))
c=0
l1=[]
for i in l:
    if i not in l1:
        for j in l:
            if i==j:
                c+=1
        l1.append(i)
        print(i,":",c)
        c=0
