data = {}
for _ in range(int(input())):
    a = input()
    if data.get(a, 0) == 0:
        data[a] = 1
        print('OK')
    else:
        data[a + str(data[a])] = 1
        data[a] += 1
        print(a + str(data[a] - 1))
