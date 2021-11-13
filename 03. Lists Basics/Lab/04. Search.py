n = int(input())
word = input()
lst = []
for i in range(n):
    text = input()
    lst.append(text)
print(lst)
print([x for x in lst if word in x])
