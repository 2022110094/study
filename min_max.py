def findMinAndMax(L):
    if not L:
        return None,None
    n = L[0]
    m = L[0]
    for x in L:
        if n >= x:
            n=x
        if m <= x:
            m=x
    return n,m
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')