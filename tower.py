def move(n, a, b, c):
    if n==1:
        print(a,'-->',c)
    if n==2:
        print(a,'-->',b)
        print(a,'-->',c)
        print(b,'-->',c)
    if n>2:
        move(n-1,a,c,b)
        print(a,'-->',c)
        move(n-1,b,a,c)
    return
# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
move(3, 'A', 'B', 'C')