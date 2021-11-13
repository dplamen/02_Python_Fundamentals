import re
pattern = r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))'
string = input()
matches = re.finditer(pattern, string)
for match in matches:
    print(match.group(0), end=' ')
