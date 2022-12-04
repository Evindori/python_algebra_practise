def deliteli(n):
    deliteli = set()
    k = 2
    while k ** 2 <= n:
        if n % k == 0:
            deliteli.add(k)
            deliteli.add(n // k)
        k += 1
    return deliteli

def all_sub_groups_sum(m):
    delit = deliteli(m)
    ans = []
    for i in delit:
        elem = 0
        c_ans = []
        while elem < m:
            c_ans.append(elem)
            elem+=i
        ans.append(c_ans)
    return ans

def uniquise(l):
    ans = []
    for i in l:
        if i in ans:
            continue
        else:
            ans.append(i)
    return ans

def all_sub_groups_mul(m):
    elements = elements_mul(m)
    ans = []
    for i in elements:
        elem = i
        c_ans = [1]
        while elem != 1 :
            c_ans.append(elem)
            elem = (i*elem)%m
            print(elem)
        ans.append(sorted(c_ans))
    return uniquise(ans)

def related_classes_mul(m):
    l = all_sub_groups_mul(m)
    elements = elements_mul(m)
    ans = []
    for i in l:
        c_ans = []
        for j in elements:
            cur_c_ans = []
            for k in i:
                cur_c_ans.append((k*j)%m)
            c_ans.append(sorted(cur_c_ans))
        ans.append(uniquise(c_ans))
    return ans

def related_classes_sum(m):
    l = all_sub_groups_sum(m)
    elements = [i for i in range(1, m)]
    print(l, elements)
    ans = []
    for i in l:
        c_ans = []
        for j in elements:
            cur_c_ans = []
            for k in i:
                cur_c_ans.append((k+j)%m)
            c_ans.append(sorted(cur_c_ans))
        ans.append(uniquise(c_ans))
    return ans
print(related_classes_sum(15))