if value[i] == value[j]:
    flag = 0
    break
else:
    if value[j] == 0:
        value[j] = -1 * value[i]
