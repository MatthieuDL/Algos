def binary_search(arr: list, num: int) -> int:   
    head = 0
    tail = len(arr) - 1
    
    while head <= tail:
        mid = (head + tail) // 2
        
        if num == arr[mid]:
            return mid
        elif num > arr[mid]:
            head = mid + 1
        else:
            tail = mid - 1
        
    return -1