def roman_to_integer(num):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(num)):
        if i > 0 and roman_dict[num[i]] > roman_dict[num[i - 1]]:
            result += roman_dict[num[i]] - 2 * roman_dict[num[i - 1]]
        else:
            result += roman_dict[num[i]]
    return result
