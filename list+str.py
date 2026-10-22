'''Write a Python program to accept a sentence and print the longest word that appears only once, ignoring capitalization.'''
s = input("Enter a string:").lower()
l = s.split()
l_len = []

for i in l:
    l_len.append(len(i))

max1 = 0
word = ""

for i in range(len(l)):
    c = 0
    for j in l:
        if l[i] == j:
            c += 1

    if c == 1 and l_len[i] > max1:
        max1 = l_len[i]
        word = l[i]

if word != "":
    print(word)
else:
    print("No unique word found")
