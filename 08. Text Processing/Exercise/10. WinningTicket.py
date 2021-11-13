def is_valid_ticket(text):
    if len(text) == 20:
        return True
    return False


def longest_sequence(text, symbols):
    max_length = 0
    symbol_target = ''
    for s in symbols:
        for i in range(1, 11):
            if i * s in text:
                if max_length < i:
                    max_length = i
                    symbol_target = s
    return max_length, symbol_target


winning_symbols = ['@', '#', '$', '^']
tickets = [x.strip() for x in input().split(',')]
for ticket in tickets:
    if not is_valid_ticket(ticket):
        print("invalid ticket")
    else:
        left_count, symbol_left = longest_sequence(ticket[:10], winning_symbols)
        right_count, symbol_right = longest_sequence(ticket[10:], winning_symbols)
        if left_count > 0 and symbol_left == symbol_right:
            if 6 <= right_count < 10 and 6 <= left_count < 10:
                print(f'ticket "{ticket}" - {min([left_count, right_count])}{symbol_left}')
            elif left_count == right_count == 10:
                print(f'ticket "{ticket}" - {min([left_count, right_count])}{symbol_right} Jackpot!')
        else:
            print(f'ticket "{ticket}" - no match')
