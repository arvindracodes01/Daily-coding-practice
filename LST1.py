"""
Reverse a list without using the .reverse() method or list 
slicing([::-1]).
"""
def reverse_list(lst):
    new_list = []
    n = len(lst)  # Define n using len()
    for i in range(n - 1, -1, -1):
        new_list.append(lst[i])
    return new_list  # Un-indented so it returns after the loop finishes


nums = [5, 7, 3, 69, 3, 4, 2]

ans = reverse_list(nums)
print(ans)

