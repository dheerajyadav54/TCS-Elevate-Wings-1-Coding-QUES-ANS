str = input()
l = int(input())
max = 0
li = []
for i in range(0, len(str), l):
    subString = str[i:i+l]
    li.append(subString)
for i in li:
    c = i.count('1')
    if c > max:
        max = c
print(max)