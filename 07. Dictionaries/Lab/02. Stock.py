text = input().split()
dictionary = {}
for i in range(0, len(text), 2):
    dictionary[text[i]] = int(text[i + 1])

searched_products = input().split()
for product in searched_products:
    if product in dictionary:
        print(f"We have {dictionary[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
