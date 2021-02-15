def enumerate_primes(n):
    is_prime = [False, False] + [True] * (n-1)
    p = 2
    primes = []
    for p in range(2, n+1):
        i = p
        if is_prime[p]:
            i = i + p
            primes.append(p)
            while i < n:
                is_prime[i] = False
                i += p
    return primes


if __name__ == '__main__':
    print(enumerate_primes(97))