from collections import deque
elements = deque(input().split())
k = int(input())
output = []
while elements:
    elements.rotate(-k + 1)
    output.append(elements.popleft())

result = '['
result += ','.join(output)
result += ']'
print(result)
