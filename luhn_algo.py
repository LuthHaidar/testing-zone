def luhn(n):
    a = list(str(n))
    b = []
    c = a[-2 :: -2]
    d = a[:: -2]
    d = [int (n) for n in d]
    b = [int(n) for n in c]
    c = [int(n) * 2 for n in c]
    e = c
    for el in c:
        sum_res = 0
        if el > 9:
            id = c.index(el)
            e.pop(id)
            while el:
                rem = el % 10
                sum_res += rem
                el = el // 10 
            e.insert(id, sum_res)
    c_sum = sum(e)
    d_sum = sum(d)
    f_sum = c_sum + d_sum
    if f_sum % 10 == 0:
        return True
    return False
