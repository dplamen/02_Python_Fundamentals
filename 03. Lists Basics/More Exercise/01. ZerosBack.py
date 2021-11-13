lst = [int(x) for x in input().split(', ')]
new_lst = [x for x in lst if x != 0]
new_lst.extend([x for x in lst if x == 0])
print(new_lst)


