def merge_sort(array):
    if len(array) > 1:
        middle = len(array)//2
        l1 = array[:middle]
        l2 = array[middle:]
        merge_sort(l1)
        merge_sort(l2)
        array[:] = merge(l1, l2)
    return array
    
def merge(l1, l2):
    i, i1, i2 = 0, 0, 0
    result = []
    while i < len(l1)+len(l2):
        if i1 < len(l1) and i2 < len(l2):
            if l1[i1] < l2[i2]:
                result.append(l1[i1])
                i1+=1
            elif l2[i2]<=l1[i1]:
                result.append(l2[i2])
                i2+=1
        elif i1 < len(l1):
            result.append(l1[i1])
            i1+=1
        else:
            result.append(l2[i2])
            i2+=1
        i+=1
    return result
