# for i in range(10):
#     print('hello')
#     print(i)

# 高斯求和
# result = 0
# for i in range(101):
#     result += i
# print(result)

# 1!+2!+3!..+n!
# result2 = 0
# for n in range(20):
#     if n>0:
#         result = 1
#         for i in range(n+1):
#             if i>0:
#                 result *= i
#         print(result)
#         result2 += result
# print(result2)

# 1!+2!+3!..+n!
result2 = 0
n = 1
while n<=4:
    result = 1
    m = 1
    while m<=n:
        result *= m
        m += 1
    result2 += result
    n +=1
print(result2)



