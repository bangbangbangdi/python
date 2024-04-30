# 字典的创建
d = {
    'name':'mia',  # 键值对
    'gender':False,
    'name':'jack'  # 键重复的话，会覆盖掉之前的值
}
print(d)
print(type(d))
# d = {}
# print(d)
# print(type(d))
# d = dict()
# print(d,type(d))
# 新增键值对
d['height'] = 170
print(d)
# 获取键值对
print(d['name'])
# 修改键值对
d['gender'] = True
print(d)
# del d
# print(d)
# in
print('name' in d)

# 字典的遍历
for i in d:
    print(i,d[i])
print('-'*30)
print(d.items())
for k,v in d.items():
    print(k,v)
for k in d.keys():
    print(k)
for v in d.values():
    print(v)

# 字典的常用方法
d.pop('name')
print(d)
a = d.copy()
print('a的键值对',a)
print(d.get('gender'))
d.popitem()
d.popitem()
print('pop',d)
d.update({'age':18})
print('update',d)
d.clear()
print(d)