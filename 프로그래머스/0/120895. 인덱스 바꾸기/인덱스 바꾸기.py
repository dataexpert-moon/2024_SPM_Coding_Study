def solution(my_string, num1, num2):
    str_list = list(my_string)
    
    temp = str_list[num1]
    str_list[num1] = str_list[num2]
    str_list[num2] = temp
    
    return ''.join(str_list)