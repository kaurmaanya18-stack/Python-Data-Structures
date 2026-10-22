s=input("Enter string:")
rev=""
l=len(s)
l=((-1)*(l+1))
for i in range(-1,l,-1):
    rev+=s[i]
print(rev)
if s==rev:
    print("PALINDROME")
else:
    print("NOt PALLINDROME")

