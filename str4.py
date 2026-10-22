
s = input("Enter a paragraph: ")
l = s.split()
d = {}
check = []

# Count frequency of each word
for i in l:
    if i not in check:
        c = 0
        for j in l:
            if i == j:
                c += 1
        d[i] = c
        check.append(i)

# Find the most frequent word
m1 = ""
m2 = ""
m3 = ""

for i in d:
    if m1 == "" or d[i] > d[m1]:
        m1 = i

# Find the second most frequent word
for i in d:
    if i != m1:
        if m2 == "" or d[i] > d[m2]:
            m2 = i

# Find the third most frequent word
for i in d:
    if i != m1 and i != m2:
        if m3 == "" or d[i] > d[m3]:
            m3 = i

# Display results
for i in [m1, m2, m3]:
    if i != "":
        print(i, ":", d[i])
