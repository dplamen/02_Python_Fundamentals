def extract_name(text):
    start_index = text.index('@') + 1
    end_index = text.index('|')
    return text[start_index: end_index]

def extract_age(text):
    start_index = text.index('#') + 1
    end_index = text.index('*')
    return text[start_index: end_index]


n = int(input())
for i in range(n):
    string  = input()
    print(f'{extract_name(string)} is {extract_age(string)} years old.')
