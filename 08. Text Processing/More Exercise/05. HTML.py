html = []
title = input()
article = input()
html.append(f'<h1>\n\t{title}\n</h1>\n<article>\n\t{article}\n</article>')
line  = input()
while line != 'end of comments':
    html.append(f'<div>\n\t{line}\n</div>')
    line  = input()
print('\n'.join(html))
