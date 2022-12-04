def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return(max(a, b))


def coprime(a, b):
    return gcd(a, b) == 1


def deliteli(n):
    deliteli = set()
    k = 2
    while k**2 <= n:
        if n%k == 0:
            deliteli.add(k)
            deliteli.add(n//k)
        k += 1
    return deliteli


def find_order_sum(a, m):
    delit = deliteli(m)
    for i in delit:
        if (a*i)%m == 0:
            return i
    return -1


def find_order_mult(a, m):
    delit = deliteli(m)
    for i in delit:
        if (a**i)%m == 1:
            return i
    return -1


def find_order_for_all_sum(m):
    ans = []
    for i in range(m):
        ans.append(find_order_sum(i,m))
    return ans


def elements_mul(m):
    delit = deliteli(m)
    l =  [i for i in range(1, m)]
    ans =[]
    for i in l:
        if coprime(m, i):
            ans.append(i)
    return ans


def find_order_for_all_mult(m):
    ans = []
    elements = elements_mul(m)
    for i in elements:
        ans.append(find_order_mult(i, m))
    return ans
