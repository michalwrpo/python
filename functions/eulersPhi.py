
def phi(n: int) -> int:
    i: int = 3
    coprime: int = n
    if n % 2 == 0:
        coprime = coprime // 2
        while n % 2 == 0:
            n = n // 2
    while i**2 <= n:
        if n % i == 0:
            coprime = coprime * (i - 1) // i
            while n % i == 0:
                n = n // i
        i += 2
    coprime = coprime * (n-1) // n
    return coprime