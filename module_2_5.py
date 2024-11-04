def get_matrix(n, m, value):
    matrix = []
    raw = []
    for i in range(0,m):
        raw = [0] * n
        for j in range(0,n):
            raw[j] = value
        matrix.append(raw)
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
result4 = get_matrix(0, -1, 13)

print(result1)
print(result2)
print(result3)
print(result4)
