def my_factorial(n):
    if n < 0:
        raise ValueError('n cannot be negative.')
    elif n in (0, 1):
        return 1
    else:
        p = 1
        for i in range(1, n+1):
            p *= i
        return p
