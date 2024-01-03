
def mmulti(matrix1: list[list[float | int]], matrix2: list[list[float | int]]) -> list[list[float | int]]:
    m: int = len(matrix1)
    n: int = len(matrix1[0])
    p: int = len(matrix2[0])
    ans: list[list[float | int]] = []
    print(m, n, p, len(matrix2))
    if len(matrix2) != n:
        raise ValueError("matrices sizes are not matching")
    for i in range(m):
        if len(matrix1[i]) != n:
            raise ValueError("matrix's rows must be of the same length")
    for i in range(n):
        if len(matrix2[i]) != p:
            raise ValueError("matrix's rows must be of the same length")
    for i in range(m):
        ans.append([])
        for j in range(p):
            sum: float | int = 0
            for k in range(n):
                sum += matrix1[i][k] * matrix2[k][j]
            ans[i].append(sum)
    return ans


m1: list[list[int | float]] = [[1, 2], [3, 4]]
m2: list[list[int | float]] = [[1, 2, 3], [4, 5, 6]]
product = mmulti(m1, m2)
for i in range(len(product)):
    print(product[i])