# 26. Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# Пример:
# o для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def fibonacci(number):
    """Принимает целое число 'N'. Возвращает ряд Фибоначчи
    диапазона от -N до N.
    """
    # Вычисляем положительную часть ряда.   
    
    pos_fib = []
    for n in range(number+1):
        if n == 0:
            pos_fib.append(0)
        elif n == 1:
            pos_fib.append(1)
        else:
            pos_fib.append(pos_fib[n-1] + pos_fib[n-2])
    print('Positive numbers: ', pos_fib)
   
    # Вычисляем отрицательную часть ряда.

    nega_fib = [(-1)**(n+1)*pos_fib[n] for n in range(len(pos_fib)-1, 0, -1)]
    print('Negative numbers: ', nega_fib)
    
    # Возвращаем общий список
    
    return nega_fib + pos_fib


num = int(input('Enter an integer positive number: '))
print('Fibonacci: ', fibonacci(num))
