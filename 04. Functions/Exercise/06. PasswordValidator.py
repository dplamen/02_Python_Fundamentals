def is_valid(password):
    if not 6 <= len(password) <= 10:
        return "Password must be between 6 and 10 characters"
    if not password.isalnum():
        return "Password must consist only of letters and digits"
    count = 0
    for ch in password:
        if ch.isdigit():
            count += 1
    if count < 2:
        return "Password must have at least 2 digits"

    return 'Password is valid'


print(is_valid(input()))
