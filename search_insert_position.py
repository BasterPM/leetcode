def search_insert_position(lst, target):
    if len(lst) == 0:
        return 0
    if target < lst[0]:
        return 0
    if target > lst[-1]:
        return len(lst)
    for i in range(len(lst)):
        if lst[i] == target:
            return i
        if lst[i] < target < lst[i + 1]:
            return i + 1
