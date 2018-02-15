import math
from collections import defaultdict

def make_prime_list(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]

def main():
    Q = int(input())

    is_prime = defaultdict(lambda: False)
    primes = make_prime_list(100000)
    for prime in primes:
        is_prime[prime] = True

    query_list = []
    for i in range(Q):
        query_list.append([int(_) for _ in input().split()])

    for query in query_list:
        begin = query[0]
        end   = query[1] + 1

        n_like_2017 = 0
        for target in range(begin, end, 2):
            if (is_prime[target]) and (is_prime[(target + 1) // 2]):
                n_like_2017 += 1

        print(n_like_2017)

main()
