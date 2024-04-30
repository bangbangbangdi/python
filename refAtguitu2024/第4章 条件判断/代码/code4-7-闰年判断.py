year = int(input('请输入年份：'))
if (not year % 4  and year % 100 ) or not year % 400:
    print('是闰年')
else:
    print('不是闰年')