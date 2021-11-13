arr = [int(x) for x in input().split()]
line = input()
while line != 'end':
    if line.startswith('exchange'):
        idx = int(line.split()[1])
        if not 0 <= idx < len(arr):
            print('Invalid index')
        else:
            arr = arr[idx + 1:] + arr[:idx + 1]
    elif line.startswith('max'):
        odd_even = line.split()[1]
        if odd_even == 'odd':
            odd_arr = [x for x in arr if x % 2 != 0]
            if odd_arr:
                print(arr.index(max(odd_arr)))
            else:
                print('No matches')
        else:
            even_arr = [x for x in arr if x % 2 == 0]
            if even_arr:
                print(arr.index(max(even_arr)))
            else:
                print('No matches')
    elif line.startswith('min'):
        odd_even = line.split()[1]
        if odd_even == 'odd':
            odd_arr = [x for x in arr if x % 2 != 0]
            if odd_arr:
                print(arr.index(min(odd_arr)))
            else:
                print('No matches')
        else:
            even_arr = [x for x in arr if x % 2 == 0]
            if even_arr:
                print(arr.index(min(even_arr)))
            else:
                print('No matches')
    elif line.startswith('first'):
        n = int(line.split()[1])
        odd_even = line.split()[2]
        if odd_even == 'odd':
            odd_arr = [x for x in arr if x % 2 != 0]
            if n <= len(arr):
                print(odd_arr[:n])
            else:
                print("Invalid count")
        else:
            even_arr = [x for x in arr if x % 2 == 0]
            if n <= len(arr):
                print(even_arr[:n])
            else:
                print("Invalid count")
    elif line.startswith('last'):
        n = int(line.split()[1])
        odd_even = line.split()[2]
        if odd_even == 'odd':
            odd_arr = [x for x in arr if x % 2 != 0]
            if n <= len(arr):
                print(odd_arr[len(odd_arr) - n:len(odd_arr)])
            else:
                print("Invalid count")
        else:
            even_arr = [x for x in arr if x % 2 == 0]
            if n <= len(arr):
                print(even_arr[len(even_arr) - n:len(even_arr)])
            else:
                print("Invalid count")
    line = input()

print(arr)
