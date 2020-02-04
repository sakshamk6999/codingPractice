def decToBinary(n):
    # array to store
    # binary number 

    # counter for binary array 
    i = 0
    while (n > 0):
        # storing remainder
        # in binary array
        n = int(n / 2)
        i += 1
    print(i)

decToBinary(10**18)