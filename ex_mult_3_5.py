"""
_______________________________________________________________________________________________________________________________________
|ENG:                                                                                                                                 |
|    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.|
|    Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.                        |
|RUS:                                                                                                                                 |
|    Если мы перечислим все натуральные числа ниже 10, которые кратны 3 или 5, мы получим 3, 5, 6 и 9. Сумма этих кратных 23.         |
|    Завершите решение, чтобы оно возвращало сумму всех кратных 3 или 5 числам ниже переданного числа.                                |
|_____________________________________________________________________________________________________________________________________|
"""


def solution(number):
    result = []
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            result.append(i)

    return sum(result)