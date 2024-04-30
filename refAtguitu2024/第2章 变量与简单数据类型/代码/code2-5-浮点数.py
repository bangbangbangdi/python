# 浮点数的计算
n1 = 2.1
n2 = 15.256
print(n1 + n2)

# 四舍五入round
n3 =round(n1+n2, 2)
print(n3)

import math
# 向上取整 ceil
n4 = math.ceil(n1+n2)
print("向上取整的结果是", n4)
# 向下取整 floor
n5 = math.floor(n1+n2)
print("向下取整的结果是", n5)