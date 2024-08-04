def partition(arr , low , high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
   if low < high:
        q = partition(arr, low, high)


        quick_sort(arr, low, q - 1)
        quick_sort(arr, q + 1, high)


arr = [7,2,1,6,8,5,3,4]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted Array:", arr)
