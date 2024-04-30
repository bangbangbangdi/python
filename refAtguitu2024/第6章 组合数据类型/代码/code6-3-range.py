# range(start, end, step)
print(list(range(10)))  # end
print(list(range(2,10)))  # start,end
print(list(range(2,10,3))) # start,end,step

for i in range(3):
    print('hello')

# 高斯求和
total = 0
for i in range(1001, 10001, 2):
    total += i
print(total)

# 水仙花数：三位数，每一位数字的立方和 = 三位数本身
# 123   1^3+2^3+3^3 = 123
for i in range(100,1000):
    # a = i % 10  # 个位
    # b = i % 100 // 10  # 十位
    # c = i // 100  # 百位
    t = str(i)
    a = int(t[2])
    b = int(t[1])
    c = int(t[0])
    if a**3+b**3+c**3 == i:
        print(i)


