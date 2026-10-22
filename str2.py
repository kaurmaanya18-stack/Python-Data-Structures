'''Determine whether an input sentence is a palindrome after ignoring spaces, punctuation, and letter case.'''
s=input("Enter a string: ")
copy=""
s=s.lower()
for i in s:
    if(i.isalnum()):
        copy+=i
if(copy==copy[::-1]):
    print("Palindrome!")
else:
    print("Not palindrome!")