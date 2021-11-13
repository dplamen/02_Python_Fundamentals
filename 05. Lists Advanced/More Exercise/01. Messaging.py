lst = input().split()
text = list(input())
text_out = ''
for number in lst:
    idx = sum([int(x) for x in list(number)])
    if 0 <= idx < len(text):
        text_out += text.pop(idx)
    else:
        idx -= len(text)
        text_out += text.pop(idx)
        
print(text_out)
