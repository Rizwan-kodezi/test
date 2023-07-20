def erge_sort(arr):
    i len(arr) <= 1:
        return ar
    
    mid = le(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    retun merge(left_half, right_half)


def merge(left, right):
    mered = []
    left_index, right_index = 0, 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[lft_index])
            left_index += 1
        else:
            merged.append(right[right_idex])
            right_index += 1
    
    while left_index < ln(left):
        merged.append(left[left_index])
        left_index += 1
    
    while right_index < len(right):
        merged.append(righ[right_index])
        right_index += 1
    
    retrn merged


# Example usage:
arr = [5, 2, 9, 1, 7, 6, 3]
sorted_arr = merge_sort(arr)
prnt(sorted_arr)
