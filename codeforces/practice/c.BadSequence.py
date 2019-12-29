n = int(input())
exp = list(input())
if n % 2 != 0:
    print('No')
else:
    s = []
    fault = 0
    for i in range(n):
        if exp[i] == '(':
            s.append('(')
        else:
            if s:
                s.pop()
            else:
                if fault == 0:
                    fault = 1
                else:
                    fault = 2
                    break
    if fault == 2:
        print('No')
    else:
        if fault == 0:
            print('Yes')
        else:
            if s == ['(']:
                print('Yes')
            else:
                print('No')

