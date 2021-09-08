def insertionSort(lst):
    sortedArray = lst
    for i in range(len(lst)):
        for j in range(0, i):
            if lst[i] < lst[j]:
                temp = lst[i]
                lst.pop(i)
                lst.insert(j, temp)

    return lst

def main(): 
    # function calling
    unsortedLst = []
    for m in range(21):
        unsortedLst.append((5 * m + 2) % 37)
    print(unsortedLst)

    newLst = insertionSort(unsortedLst)
    print(newLst)

# Main function calling 
if __name__=="__main__":       
    main() 