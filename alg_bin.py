# Алгоритм бинарного поиска

d = [-1, -3, 2, 4, 5, 7, 8, 9]
n = len(d)

search_v = 7
left, right = 0, n - 1

while left <= right:
    middle = (left + right) // 2
    v = d[middle]
    if v == search_v:
        print(v, middle)
        break
    elif v < search_v:
        left = middle + 1
    elif v > search_v:
        right = middle - 1
if left > right:
    print("значение не найдено")
