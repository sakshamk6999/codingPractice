n, k = map(int, input().split())
s = list(input())

if n == 1 and k:
    print('0')
elif k == 0:
    print(''.join(s))

else:
    i = 0
    while i < n:
        if k :
            if i == 0:
                if s[i] != '1':
                    s[i] = '1'
                    k -= 1
            else:
                if s[i] != '0':
                    s[i] = '0'
                    k -= 1
            i += 1
        else:
            break
    print(''.join(s))
