def find_the_index(haystack, needle):
    for i in range(len(haystack)):
        if needle in haystack:
            return haystack.index(needle[0])
    return -1
