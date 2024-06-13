def palindrome_number(num):
    num = str(num)
    if num == num[::-1]:
        return True
    else:
        return False
