def enumerate_primes(n):

    primes = [False, False] + [True] * (n-1)
    res = []
    for i in range(2, n+1):
        if primes[i]:
            res.append(i)
            for p in range(i, n+1, i):
                if primes[p]:
                    primes[p] = False

    return res


if __name__ == '__main__':
    print(enumerate_primes(97))