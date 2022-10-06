# Напишите программу, которая будет преобразовывать
# десятичное число в двоичное.
# o 45 -> 101101
# o 3 -> 11
# o 2 -> 10


# Вариант 1


def dec_to_bin_1(dec_n):
    b = ''
    while dec_n > 0:
        b = str(dec_n % 2) + b
        dec_n //= 2
    return b

# Вариант 2


def dec_to_bin_2(dec_n):
    if dec_n == 0:
        return ''
    else:
        return dec_to_bin_2(dec_n//2) + str(dec_n % 2)

# Вариант 3


def dec_to_bin_3(dec_n):
    return int(bin(dec_n).replace('0b', ''))


num = int(input('Enter in integer: '))

print(dec_to_bin_1(num))
print(dec_to_bin_2(num))
print(dec_to_bin_3(num))
