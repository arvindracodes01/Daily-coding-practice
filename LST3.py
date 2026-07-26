"""
given a list, remove all duplicate lements while preserving the
original order of the unique items
"""
def remove_duplicate(lst):
    result = []
    for num in lst:
        if num not in result:
            result.append(num)

    return result  


num = [5, 65, 25, 5, 6, 5, 5, 7, 7, 5]
ans = remove_duplicate(num)
print(ans)
