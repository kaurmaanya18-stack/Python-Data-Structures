'''Accept a sentence and a target word from the user. Display all words in the sentence that are anagrams of the target word, ignoring capitalization.'''
s = input("Enter a string: ")
a = input("Enter the word: ")
l = list(a.lower())
s = s.lower()
words = s.split()
temp = []
k = 0

for i in words:
    temp = list(i)
    k = 0

    if len(l) == len(temp):
        for j in l:
            if l.count(j) == temp.count(j):
                k += 1

        if k == len(l):
            print(i)
