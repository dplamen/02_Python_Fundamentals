def shuffle(lst):
    new_lst = []
    half = int(len(lst)/2)
    for i in range(half):
        new_lst.append(lst[i])
        new_lst.append(lst[i + half])
    return new_lst


deck = input().split(' ')
n = int(input())
for j in range(n):
    deck = shuffle(deck)
print(deck)
