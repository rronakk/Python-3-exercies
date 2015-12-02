# An example to learn exceptions
# print a box from the symbol, height, and width given.


def print_box(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol should be single character')
    if width <= 2:
        raise Exception('Width must be more than 2')
    if height <= 2:
        raise Exception('Height must be more than 2')

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2) + symbol))
    print(symbol * width)


for sym, w, h in (('*', 20, 10), ('$', 40, 20), ('%^', 2, 2), ('@', 2, 1)):
    try:
        print_box(sym, w, h)
    except Exception as err:
        print('Exception has occurred :' + str(err))
