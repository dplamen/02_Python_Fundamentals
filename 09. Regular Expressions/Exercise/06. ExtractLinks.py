import re

valid_links = []
line = input()
pattern = r'www\.[a-zA-Z0-9\-]+(\.[a-z]+)+'
while line:
    link = re.search(pattern, line)
    if link:
        valid_links.append(link.group(0))
    line = input()
print('\n'.join(valid_links))
