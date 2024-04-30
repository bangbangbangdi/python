# 10阶楼梯，每次上1个台阶或者上2个台阶，问一共有多少种走法
# 3
# 1 1 1
# 1 2
# 2 1
# f(n) = f(n-1) + f(n-2)
# n=0,f(n)=0
# n=1,f(n)=1
# n=2,f(n)=2
def f(n):  # 计算出n阶楼梯，一共有多少种走法
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 2
    return f(n-1)+f(n-2)

print('楼梯有%d阶的时候，有%d种走法'%(5,f(5)))

a = [0,1,2]
for i in range(3,11):
    a.append( a[i-1] + a[i-2])
    print('楼梯有%d阶的时候，有%d种走法' % (i, a[-1]))
