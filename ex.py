'''
__________________________________________________________________________________________________________________
|ENG:                                                                                                            |
|    In this kata you are required to, given a string, replace every letter with its position in the alphabet.   |
|    If anything in the text isn't a letter, ignore it and don't return it.                                      |
|    "a" = 1, "b" = 2, etc.                                                                                      |
|RUS:                                                                                                            |
|    В этом ката вы должны, учитывая строку, заменить каждую букву ее позицией в алфавите.                       |
|    Если что-то в тексте не является буквой, игнорируйте это и не возвращайте.                                  |
|    «a» = 1, «b» = 2 и т. д.                                                                                    |
|________________________________________________________________________________________________________________|
'''

def alphabet_position(text):
	x = ''
	j = list('abcdefghijklmnopqrstuvwxyz')
	for i in text:
		if i.isalpha():
			x += str(j.index(i.lower()) + 1) + ' '
	return x[0:len(x)-1]