"""This module contains algorithms related to binary searching"""

def binary_search(arr: list, num: int) -> int:
    """
    https://en.wikipedia.org/wiki/Binary_search
    
    Time complexity:
        O(logn)
        
    Space complexity:
        O(1)
    """
    head = 0
    tail = len(arr) - 1

    while head <= tail:
        mid = (head + tail) // 2

        if num == arr[mid]:
            return mid
        if num > arr[mid]:
            head = mid + 1
        else:
            tail = mid - 1

    return -1
