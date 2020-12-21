'''
____________________________________________________________________________________________________________________________________________
|ENG:                                                                                                                                      |
|    Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.          |
|    Rules for a smiling face:                                                                                                             |
|                                                                                                                                          |
|        Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;                                                  |
|        A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~                                     |
|        Every smiling face must have a smiling mouth that should be marked with either ) or D                                             |
|                                                                                                                                          |
|    No additional characters are allowed except for those mentioned.                                                                      |
|                                                                                                                                          |
|RUS:                                                                                                                                      |
|    Учитывая массив (arr) в качестве аргумента, завершите функцию countSmileys, которая должна вернуть общее количество улыбающихся лиц.  |
|    Правила улыбающегося лица:                                                                                                            |
|                                                                                                                                          |
|        Каждый смайлик должен содержать допустимую пару глаз. Глаза можно обозначить как: или;                                            |
|        У смайлика может быть нос, но это не обязательно. Допустимые символы для носа - или ~                                             |
|        У каждого улыбающегося лица должен быть улыбающийся рот, который должен быть отмечен либо), либо D                                |
|                                                                                                                                          |
|    Использование дополнительных символов не допускается, кроме упомянутых.                                                               |
|__________________________________________________________________________________________________________________________________________|
'''

def count_smileys(arr):
    eyes = [':',';']
    nose = ['-','~']
    mouth = [')', 'D']
    count = 0
     
    for i, item in enumerate(arr):
        if len(item)==2:
            if item[0] in eyes and item[1] in mouth:
                count += 1
        elif len(item)==3:
            if item[0] in eyes and item[1] in nose and item[2] in mouth:
                count += 1
    return count