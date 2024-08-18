# 列表生成式

# -------------- 栗子: 不带条件的列表生成式 --------------
# 前置知识:x的n次方的写法是 x**n  例如 3的四次方 -> 3**4
print(3 ** 4)

# 生成0到9的平方
squares = [x ** 2 for x in range(10)]
print(squares)

# 练习1
# 生成10到20到立方

# 练习2
# 将字符串Tin拆分为 单个字符  Tin -> 'T','i','n'

# 练习3
# 将字符串Tin拆分为单个字符到基础上左右添加 -  ; Tin -> '-T-','-i-','-n-'

# -------------- 栗子: 带条件的列表生成式 --------------
# 生成偶数的平方
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares)

# 练习1
# 生成奇数的平方


# 练习2
# 将Tin.txt、Tin.jpg...从众多列表项目中挑出来
li = ['Tin.txt', 'Tin.jpg', 'Tin.png', 'kino.txt', 'kino.jpg', 'erms.txt', 'erms.png', 'shibo.txt', 'shibo.jpg']

# -------------- 栗子: 多重循环的列表生成式 --------------
# 生成笛卡尔积
cartesian_product = [(x, y) for x in range(3) for y in range(3)]
print(cartesian_product)
# 输出: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# 练习1
# 将以下两个列表组合生成新的列表
# ['kino.jpg', 'kino.txt', 'kino.gif', 'mokuzu.jpg', 'mokuzu.txt', 'mokuzu.gif', 'yamada.jpg', 'yamada.txt', 'yamada.gif', 'tomohiko.jpg', 'tomohiko.txt', 'tomohiko.gif']
l1 = ['kino', 'mokuzu', 'yamada', 'tomohiko']
l2 = ['jpg', 'txt', 'gif']

# -------------- 栗子: 嵌套列表解析 --------------
# 展平二维列表
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [num for row in matrix for num in row]
print(flat_list)
# 输出: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 练习
# 将下列而为列表中的偶数挑出来
matrix = [[134, 4521, 1232], [2341, 8785, 995], [88117, 81123, 911232]]
