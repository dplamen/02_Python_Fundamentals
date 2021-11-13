import re
string = input()
pattern = r'(?:(?<=^)|(?<=\s))[a-zA-Z0-9]+[a-zA-Z0-9\.\-_]+' \
          r'[a-zA-Z0-9]+@[a-zA-Z0-9]+[a-zA-Z0-9\.+\-]+\.[a-zA-Z0-9\.+\-]+[a-zA-Z0-9]+'
matches = re.findall(pattern, string)
print('\n'.join(matches))
