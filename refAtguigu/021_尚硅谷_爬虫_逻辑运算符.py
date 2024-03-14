# 逻辑运算符  and 与  or 或  not 非

# and 与
# and两边的数据 必须全部都是true的时候 才会返回true 只要有一端返回的是false 那么就返回false
# and两端都是false的时候 返回的是false
print(10 > 20 and 10 > 11)
# and一端是true 一端是false 返回的是false
print(10 > 5 and 10 >11)
# and一端返回的是false 一端返回的是true  返回的是false
print(10 > 11 and 10 > 5)
# and 两端返回的都是true则返回的是的true
print(10 > 5 and 10 > 6)

# or 或者
# or的两端只要有一端是true 那么结果就是true
# or的两端都是false 则返回的是false
print(10 > 20 or 10 > 21)
# or的两端前面的是true  后面的是false 那么返回的是true
print(10 > 5 or 10 > 20)
# or的两端 前面的是false 后面的是true  那么返回的是true
print(10 > 20 or 10 > 5)
# or的两端都是true  那么返回的是true
print(10 > 5 or 10 > 6)

# not  非  取反
print(not True)
print(not False)
print(not (10 > 20))
