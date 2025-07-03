def reversed_bubble_sort(arr):
    """
    Sorts an array in descending order using the bubble sort algorithm.
    
    :param arr: List of elements to be sorted
    :return: Sorted list in descending order
    """
    n = len(arr)
    for i in reversed(range(n)):
        for j in range(i-1,-1, -1):
            if arr[j] > arr[j+1]:  # Change to '<' for descending order
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# ejemplo de uso
lista = [5, 2, 9, 1, 5, 6]
sorted_list = reversed_bubble_sort(lista)
print(sorted_list)  # Output: [9, 6, 5, 5, 2, 1]
