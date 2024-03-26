# -------------------- CSV操作 --------------------
import csv
import random


# -------------------- write --------------------
# 我们可以调用csv模块当中的writerow方法对输入进行写入
def csv_write():
    with open('./testFile/CsvTest.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # 设置表头
        header = ['姓名', '力量', '敏捷', '耐力', '幸运', '成长', '财富']
        writer.writerow(header)
        # 设置每一行的姓名
        names = ['kino', 'kirii', 'erms', 'shibo', 'kuroniko', 'kaiba']
        for name in names:
            # 随机生成5个1~100的整数作为每个人的各项数值
            row = [random.randint(1, 100) for _ in range(5)]
            # 随机生成每个人的财富,并格式化为 123123 -> 123,123
            account = format(random.randint(1000, 999999), ',')
            # 将名字插入到索引为0的位置
            row.insert(0, name)
            # 将财富添加到列表中(添加到最后)
            row.append(account)
            writer.writerow(row)


# -------------------- read --------------------
def csv_read(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        # 此时的reader中存着整个csv文件的所有数据
        reader = csv.reader(file, delimiter=',')
        # 遍历reader,此时的row中存的是每一行数据
        for row in reader:
            # 遍历row,此时item中存的就是每一个单独的数据项了
            # print(row)
            for item in row:
                print(item, end=' ')
            print()


# -------------------- Practice --------------------
# ABang在项目中真实出现过的需求 -> 将123,123类型的数据格式化成123123
# 很简单的需求~让我们用上面的知识来实现一下
def csv_practice(file_name):
    # 保存整个csv数据的列表
    rows = []
    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',')
        count = 0
        for row in reader:
            count += 1
            # 表头直接添加到列表中
            if count == 1:
                rows.append(row)
                continue
            size = len(row)
            # 获取除了最后一列的所有数据
            new_row = row[0:size - 1]
            # 将最后一列的数据中的 , 删除
            af_format = row[size - 1].replace(',', '')
            new_row.append(af_format)
            rows.append(new_row)

    # 到这里我们的rows里面存的就是需要的数据了,接下来只需要将列表中的数据写到csv文件中即可
    with open('./testFile/CsvTest2.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow(row)


def main():
    # csv_write()
    # csv_read('./testFile/CsvTest.csv')
    csv_practice('./testFile/CsvTest.csv')
    # print('123,123,123'.replace(',',''))
    pass


if __name__ == '__main__':
    main()
