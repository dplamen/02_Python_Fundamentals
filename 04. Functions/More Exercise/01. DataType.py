def data_actions(data_type, user_input):
    types = {'int': lambda x: 2 * int(x),
             'real': lambda x: f"{1.5 * float(x):.2f}",
             'string': lambda x: "$" + x + "$"
             }
    return types[data_type](user_input)


line1 = input()
line2 = input()
print(data_actions(line1, line2))
