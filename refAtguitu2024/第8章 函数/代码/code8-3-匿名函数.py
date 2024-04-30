# fun = lambda a,b:a+b
# result = fun(5,2)
# print(result)

a = [1,2,3,4,5]
result = map(lambda x:x**3, a)  # 映射
print(list(result))

#  reduce  累积
from functools import reduce
result = reduce(lambda x,y:x*y,a)
print(result)

# filter 过滤
result = filter(lambda x:x%2,a)
print(list(result))



a = [1,2,3,40,5,6,0,6,0,5]  # 12340560605
result = filter(lambda x:x!=0,a)
print(list(result))

result = 0
mul = 1
for i in a[::-1]:
    result = result + i*mul
    mul = mul*10**len(str(i))
print(result)

result = reduce(lambda x,y:x*10**len(str(y))+y,a)
print(result)








