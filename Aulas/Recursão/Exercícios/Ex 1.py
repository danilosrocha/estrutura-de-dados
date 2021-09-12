def fatorial(n):
    if n == 0:
        return 1
    elif n <= 6:
        return n * fatorial(n - 1)
    else:
        return n * fatorial(n - 1) % 2357

print(fatorial())

"""elif n * fatorial(n - 1) > 2357:
        return n * fatorial(n - 1) % 2357"""