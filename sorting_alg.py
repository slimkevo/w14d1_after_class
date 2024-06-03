def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left_half = merge_sort(nums[:mid])
    right_half = merge_sort(nums[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    if left_index < len(left):
        merged.extend(left[left_index:])
    
    if right_index < len(right):
        merged.extend(right[right_index:])
    
    return merged

def sortArray(nums):
    return merge_sort(nums)

print(sortArray([6, 5, 3, 1, 8, 7, 2, 4]))
print(sortArray([2, 7, 4, 1, 5, 3, 8, 6]))
print(sortArray([4, 3, 2, 1, 0, -1, -2, -3]))