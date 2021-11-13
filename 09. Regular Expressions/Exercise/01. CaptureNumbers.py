import re
text = input()
matches = []
while text:
    pattern = r'[0-9]+'
    matches.extend(re.findall(pattern, text))
    text = input()
print(' '.join(matches))
