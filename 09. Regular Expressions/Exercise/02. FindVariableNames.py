import re
sentence = input()
pattern = r'(?:(?<=\s_)|(?<=^_))[a-zA-Z0-9]+\b'
matches = re.findall(pattern, sentence)
print(','.join(matches))
