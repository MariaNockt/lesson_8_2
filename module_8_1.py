def add_everything_up(a, b):

    try:
        if type(a) != type(b):
            return a + b
        else:
            return TypeError
    except TypeError:
        return f'{str(a)}{str(b)}'


# Примеры использования функции
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))