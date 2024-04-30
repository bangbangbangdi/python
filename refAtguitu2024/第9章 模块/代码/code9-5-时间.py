import time
t = time.time()  # 时间戳：1970年
print(t)
t = time.localtime()  # 结构化的时间
print(t)
print(t.tm_year,type(t.tm_year)) # 获取
s = time.strftime('%Y-%m-%d %H:%M:%S',t)
print(s)
from  my_package import my_tools
print(my_tools.get_time())