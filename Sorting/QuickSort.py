def quick_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    
    left = [x for x in arr if x < pivot]
    center = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + center + quick_sort(right)