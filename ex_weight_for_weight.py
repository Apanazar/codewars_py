'''
____________________________________________________________________________________________________________________________________________
|ENG:                                                                                                                                      |
|    My friend John and I are members of the "Fat to Fit Club (FFC)". John is worried because each month a                                 |
|    list with the weights of members is published and each month he is the last on the list which means he is the heaviest.               |
|    I am the one who establishes the list so I told him: "Don't worry any more, I will modify the order of the list". It                  |
|    was decided to attribute a "weight" to numbers. The weight of a number will be from now on the sum of its digits.                     |
|    For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99. Given a string                 |
|    with the weights of FFC members in normal order can you give this string ordered by "weights" of these numbers?                       |
|RUS:                                                                                                                                      | 
|    Мы с моим другом Джоном являемся членами «Клуба жирных и подтянутых» (FFC). Джон обеспокоен тем, что каждый месяц                     |
|    публикуется список с весом участников, и каждый месяц он занимает последнее место в списке, что означает, что он самый тяжелый.       |
|    Я составляю список, поэтому я сказал ему: «Больше не волнуйтесь, я изменю порядок в списке». Было решено присвоить цифрам «вес».      | 
|    С этого момента вес числа будет складываться из суммы его цифр.                                                                       |
|    Например, 99 будет иметь «вес» 18, 100 будет иметь «вес» 1, поэтому в списке 100 будет стоять перед 99. Если дана строка с весами     |
|    членов FFC в нормальном порядке, можете ли вы дать эту строку, упорядоченную по «весам» эти числа?                                    |
|__________________________________________________________________________________________________________________________________________|
|                                                        | Example |                                                                       |
|    "56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes: "100 180 90 56 65 74 68 86 99"                                     |
|    When two numbers have the same "weight", let us class them as if they were strings (alphabetical ordering) and not numbers: 100 is    |
|    before 180 because its "weight" (1) is less than the one of 180 (9) and 180 is before 90 since, having the same "weight" (9),         |
|    it comes before as a string. All numbers in the list are positive numbers and the list can be empty.                                  |
|__________________________________________________________________________________________________________________________________________|
'''

def order_weight(strng):
    bar = sorted(strng.split(' '))
    baz = sorted(bar, key=foo)
    return " ".join(baz)
    
    
def foo(n):
    return sum([int(item) for item in n])

'''
___________________
|Еще одно решение |
|_________________|______________________________________________________________________________
|    def order_weight(strng):                                                                   |
|        return " ".join(sorted(strng.split(' '), key=lambda s: (sum([int(i) for i in s]), s))) |
|_______________________________________________________________________________________________|
'''