'''
_____________________________________________________________________________________________________________
|ENG:                                                                                                       |
|    Write a function that takes an integer as input, and returns the number of bits                        |
|    that are equal to one in the binary representation of that number. You can guarantee                   |
|    that input is non-negative.                                                                            |
|    Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case|
|                                                                                                           |
|RUS:                                                                                                       |
|    Напишите функцию, которая принимает на вход целое число и возвращает количество битов, равных единице в|
|    двоичном представлении этого числа. Вы можете гарантировать, что ввод неотрицательный.                 |
|    Пример: двоичное представление 1234 - 10011010010, поэтому в этом случае функция должна вернуть 5.     |
|___________________________________________________________________________________________________________|
'''
def count_bits(n):
    j = 0
    while n > 0:
        j += n % 2
        n >>= 1
    return j

'''
__________________________________
|Можно было еще так:             |
|    def countBits(n):           |
|        bits = 0                |
|        while n > 0:            |
|            if n & 1:           |
|                bits += 1       |
|            n /= 2              |
|                                |
|        return bits             |
|________________________________|
|Или так:                        |
|    def countBits(n):           |
|        return bin(n).count("1")|
|________________________________|
'''