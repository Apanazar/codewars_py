'''
____________________________________________________________________________________________________________
|ENG:                                                                                                      |
|    Welcome. In this kata, you are asked to square every digit of a number and concatenate them.          |
|    For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. |
|    Note: The function accepts an integer and returns an integer                                          |
|                                                                                                          |
|RU:                                                                                                       |
|    Добро пожаловать. В этом ката вас просят возвести в квадрат каждую цифру числа и соединить их.        |
|    Например, если мы пропустим 9119 через функцию, выйдет 811181, потому что 92 - это 81, а 12 - 1.      |
|    Примечание: функция принимает целое число и возвращает целое число.                                   |
|__________________________________________________________________________________________________________|
'''

def square_digits(num):
    x = ''
    for i in str(num):
        ans += str(int(i)**2)

    return int(x)