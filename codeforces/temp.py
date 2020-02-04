import math

def f(x, y):
    distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
    print("Euclidean", distance)
    print('Manhattan ', sum([abs(a - b) for a, b in zip(x, y)]))
    p = 3
    print('Minkowski', pow(sum([abs(a - b) ** p for a, b in zip(x, y)]), 1 / p))
    X = set(x)
    Y = set(y)
    inter = X.intersection(Y)
    uni = X.union(Y)
    ans = len(inter) / len(uni)
    print('Jaccard', 1 - ans)


x = []
print('X')
for i in range(3):
    x.append(int(input()))
y = []
print('Y')
for i in range(3):
    y.append(int(input()))
f(x, y)
