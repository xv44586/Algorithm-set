def count_inverse(num):
    count = 0
    _n = str(num)
    for i, n in enumerate(_n):
        l = sorted(num[i:])
        c = l.index(n)
        count += c

    print(count)