def l_sym(a, b):
    return 1


def solve_x_2(c, p):
    c = c%p
    l_symbol = l_sym(c, p)
    if c == 0:
        return 0
    if c == 1:
        return 1, p-1
    if l_symbol != -1:
        if p%4 == 3:
            return (c**((p+1)//4))%p, p-(c**((p+1)//4))%p
        for i in range(p//2 + 1):
            if i**2 % p == c:
                return i, p-i
    return


def solve_2_x(c, p):
    n = 1
    ans = []
    for i in range(p):
        if n%p == c:
            ans.append(n)
        n*=2
    return ans