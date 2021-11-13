import re
string = input()
seeked_word = input()
pattern = r'\b' + seeked_word + r'\b'
matched = re.findall(pattern, string, re.IGNORECASE)
print(len(matched))
