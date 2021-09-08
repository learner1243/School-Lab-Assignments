def mergeSort(lst):
    if len(lst) > 1:
        middle = len(lst) // 2
        left = lst[:middle]
        right = lst[middle:]

        mergeSort(left)
        mergeSort(right)

        lst.clear()
        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                lst.append(left[0])
                left.pop(0)
            else:
                lst.append(right[0])
                right.pop(0)

        if len(left) > 0: 
            lst.extend(left)

        if len(right) > 0:
            lst.extend(right)


def main(): 
    # function calling
    array = []
    for m in range(21):
        array.append((5 * m + 2) % 37)
    print(array)

    mergeSort(array)
    print(array)

# Main function calling 
if __name__=="__main__":       
    main() 