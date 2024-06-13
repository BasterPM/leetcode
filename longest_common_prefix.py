def longest_common_prefix(lst):
    string = ''
    for i in range(len(lst[0])):
        for j in range(1, len(lst)):
            if lst[0][i] != lst[j][i]:
                return string
        string += lst[0][i]
