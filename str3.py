'''Given a string, find the first character that occurs exactly once, ignoring case but preserving the original character for output.'''
m=input("Enter a string:")
c=0
s=m.lower()
l=[]
ind=-1
for i in s:
    ind+=1
    if i.isalnum():
        if(i in l):
            continue
        else:
            for j in s:
                if i==j:
                    c+=1
            if(c==1):
                print(m[ind])
                break
            c=0
            l.append(i)
    else:
        continue
