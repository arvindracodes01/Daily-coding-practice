"""
given a list of numbers(which may contain duplicates) write
 a python script that  takes as input from user and 
 removes all occurrenc of that integer from the list
"""

def remove_occurence(lst, target):
    new_list = []
    for num in lst:
        if num != target:
            new_list.append(num)
    return new_list


nums = [1, 1, 1, 1, 5, 8, 8, 5, 5, 8]
print(remove_occurence(nums, 1))
