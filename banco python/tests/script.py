from random import randint


def f(N, s):
    T = [0]*(N-s)
    #T = sorted([randint(8, 240) for _ in range(N-s)])
    D = [randint(1, 9) for _ in range(N-s)]
    return list(zip(T, D))


for N in (600,):
    print("N", N)
    print(f(N, 5))
    print()


# for N in (600, 1000):

#     print("N", N)
#     print(f(N, 5))
