def remove_duplicates(nums):
    write_index = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[write_index - 1]:
            nums[write_index] = nums[i]
            write_index += 1

    for i in range(write_index, len(nums)):
        nums[i] = '_'
    return nums
