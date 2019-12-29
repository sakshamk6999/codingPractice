def mergeSort(arr, n):
    temp_arr = [0] * n
    return mergeSortUtility(arr, temp_arr, 0, n - 1)

def mergeSortUtility(arr, temp_arr, left, right):

    inv_count = 0


    if left < right:

        mid = (left + right) // 2


        inv_count = mergeSortUtility(arr, temp_arr, left, mid)

        inv_count += mergeSortUtility(arr, temp_arr, mid + 1, right)
        inv_count += merge(arr, temp_arr, left, mid, right)
    return inv_count

def merge(arr, temp_arr, left, mid, right):
    i = left  # Starting index of left subarray
    j = mid + 1  # Starting index of right subarray
    k = left  # Starting index of to be sorted subarray
    inv_count = 0

    # Conditions are checked to make sure that i and j don't exceed their
    # subarray limits.

    while i <= mid and j <= right:

        # There will be no inversion if arr[i] <= arr[j]

        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            # Inversion will occur.
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            k += 1
            j += 1

    # Copy the remaining elements of left subarray into temporary array
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1

    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1

    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]

    return inv_count


for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(q):
        k = int(input())
        b = [a[i] ^ k for i in range(n)]
        print(mergeSort(b, n))