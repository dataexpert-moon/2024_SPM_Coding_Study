def solution(my_string, is_suffix):
    for idx in range(len(my_string)):
        temp = my_string[-idx:]
        if (is_suffix == temp):
            return 1
    return 0