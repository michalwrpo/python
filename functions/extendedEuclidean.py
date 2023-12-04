
def exEuclidean(a: int, b: int) -> tuple[int, int, int]:
    x: int = 0 
    prev_x: int = 1 
    y: int = 1 
    prev_y: int = 0
    while b != 0:
        q: int = a//b
        a, b = b, a % b
        x, prev_x = prev_x - q * x, x
        y, prev_y = prev_y - q * y, y
    return a, prev_x, prev_y
