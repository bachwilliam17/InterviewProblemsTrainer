test_string = '123456780'
print(test_string[:4])
print(test_string[3:])

def isIbanValidFormat(string) : 
	
	# 2nd step of the algorithm
	four_first_digits = string[:4]
	first_alteration = string[4:] + four_first_digits

    # 3rd step of the algorithm
    second_iteration = ''
    for char in first_alteration : 
        if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' : 
            new_digit = ord(char) + 10
            second_iteration += str(new_digit)
        else second_iteration += char
    
    # 4th step of the algorithm
    if int(second_iteration) % 97 != 1 : 
        return False
    else : 
        return True



transfo = arr * 12
arr = [0 for i in range(len)]

	
