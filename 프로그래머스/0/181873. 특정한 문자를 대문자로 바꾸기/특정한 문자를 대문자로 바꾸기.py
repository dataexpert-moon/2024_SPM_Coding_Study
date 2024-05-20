def solution(my_string, alp):
    new_char = chr(ord(alp) - 32)
    return my_string.replace(alp, new_char)
    