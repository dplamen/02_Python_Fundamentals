lst1 = input().split(', ')
lst2 = input().split(', ')
out_lst = []
for word1 in lst1: 
    for word2 in lst2:
        if word1 in word2 and word1 not in out_lst:
            out_lst.append(word1)
print(out_lst)
