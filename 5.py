import math


# представим битовый вид числа как полином в {0,1}
# например 7 = 101 = 1+0*x+1*x^2
def power(polynom):
    return -1 if polynom == 0 else int(math.log2(float(polynom)))


def st(poly):
    if power(poly) == -1:
        return "0"
    else:
        return "+".join([(f'x^{n}') for n in range(power(poly) + 1) if ((poly >> n) & 1)])


def divide(left, right):
    num = 0
    reminder = 0
    if power(left) >= power(right):
        new_left = left ^ (right * (2 ** (power(left) - power(right))))
        num += (2 ** (power(left) - power(right)))
        sub_num, reminder = divide(new_left, right)
        num += sub_num
    else:
        reminder = left
    print(st(left), '/', st(right), '=', st(num), 'with', st(reminder))
    return num, reminder


def multiply(left, right):
    left_bit = [(left >> n) & 1 for n in range(power(left) + 1)]
    right_bit = [(right >> n) & 1 for n in range(power(right) + 1)]
    total = [0 for i in range(power(left) + power(right) + 1)]
    for i in range(power(left) + 1):
        for j in range(power(right) + 1):
            total[i + j] = total[i + j] ^ (left_bit[i] * right_bit[j])
    ans = 0
    for pow, bit in enumerate(total):
        ans += bit * (2 ** pow)
    return ans


left = 2  # polynom_1
right = 2  # polynom_2
print(st(multiply(left, right)))


def NOD_splits(left, right):
    if left < right:
        left, right = right, left
    left_split = [1, 0]
    right_split = [0, 1]
    bl = left
    br = right
    while (left != 0 and right != 0):
        left, num, right = right, *divide(left, right)
        new_split = [left_split[i] ^ multiply(right_split[i], num) for i in range(2)]
        left_split, right_split = right_split, new_split
    print("NOD", st(left), f"\nsplit ({st(left_split[0])})*({st(bl)})+({st(left_split[1])})*({st(br)})")
    print("check: ", st(multiply(left_split[0], bl) ^ multiply(left_split[1], br)))


l = 12
r = 7
print("left:", st(l))
print('right:', st(r))
NOD_splits(l, r)