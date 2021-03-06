'''
_______________________________________________________________________________________________________________
|ENG:                                                                                                         |
|    This time no story, no theory. The examples below show you how to write function accum                   |
|RU:                                                                                                          |
|    На этот раз ни рассказа, ни теории. В приведенных ниже примерах показано, как написать функцию накопителя|
|_____________________________________________________________________________________________________________|
_____________________________________________| TASK |___________________________________________
|                                                                                              |
|                                                                                              |
|                                accum("abcd")    # "A-Bb-Ccc-Dddd"                            |
|                                accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"       |
|                                accum("cwAt")    # "C-Ww-Aaa-Tttt"                            |
|______________________________________________________________________________________________|
'''

def accum(s):
    j = ''
    i = 0
    while i < len(s):
    	n = 0
    	while n < i+1:
    		if n == 0:
    			j += s[i].upper()
    		else:
    			j += s[i].lower()
    		n += 1
    	j += '-'
    	i += 1
    return j[:len(j)-1]