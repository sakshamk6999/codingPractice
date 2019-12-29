import math


def count(arr, x, n):
    # get the index of first
    # occurrence of x
    i = first(arr, 0, n - 1, x, n)

    # If x doesn't exist in
    # arr[] then return -1
    if i == -1:
        return i

        # Else get the index of last occurrence
    # of x. Note that we are only looking
    # in the subarray after first occurrence
    j = last(arr, i, n - 1, x, n)

    # return count
    return j - i + 1


# if x is present in arr[] then return
# the index of FIRST occurrence of x in
# arr[0..n-1], otherwise returns -1
def first(arr, low, high, x, n):
    if high >= low:
        # low + (high - low)/2
        mid = (low + high) // 2

        if (mid == 0 or x > arr[mid - 1]) and arr[mid] == x:
            return mid
        elif x > arr[mid]:
            return first(arr, (mid + 1), high, x, n)
        else:
            return first(arr, low, (mid - 1), x, n)
    return -1


# if x is present in arr[] then return
# the index of LAST occurrence of x
# in arr[0..n-1], otherwise returns -1
def last(arr, low, high, x, n):
    if high >= low:
        # low + (high - low)/2
        mid = (low + high) // 2

        if (mid == n - 1 or x < arr[mid + 1]) and arr[mid] == x:
            return mid
        elif x < arr[mid]:
            return last(arr, low, (mid - 1), x, n)
        else:
            return last(arr, (mid + 1), high, x, n)
    return -1

def primeFactors(n, l, unique):
    flag = 1
    while n % 2 == 0:
        if flag == 1:
            unique.append(2)
            flag = 0
        l.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        flag = 1
        while n % i == 0:
            if flag == 1:
                unique.append(int(i))
                flag = 0
            l.append(int(i))
            # flag = 0
            n = n / i

    if n > 2:
        l.append(int(n))
        unique.append(int(n))

for i in range(int(input())):
    l, r = map(int, input().split())
    ans = 0
    for j in range(l, r + 1):
        l = []
        unique = []
        primeFactors(j, l, unique)
        # print(l)
        n = len(l)
        numEven = 0
        start = 0
        if l[0] == 2:
            numEven = count(l, 2, n)
            start = 1
        numOdd = 1
        for k in range(start, len(unique)):
            numOdd *= (count(l, unique[k], n) + 1)
        diff = abs((numEven + 1)*(numOdd) - 2*numOdd)
        if diff <= 2:
            ans += 1
    print("Case #" + str(i + 1) + ":", ans)


