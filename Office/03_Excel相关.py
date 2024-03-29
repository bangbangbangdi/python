# -------------------- excel操作 --------------------
# 对excel文件进行读写操作需要用到 openpyxl 的第三方库
import datetime
import random

import openpyxl


# -------------------- 读操作 --------------------
def read_excel():
    # 加载一个工作簿(整个Excel文件)
    wb = openpyxl.load_workbook('./testFile/2020年销售数据.xlsx')

    # 获取所有工作表的名字(所有的sheet)
    print(wb.sheetnames)

    # 获取第一个sheet
    sheet = wb.worksheets[0]
    # 获取单元格的范围
    print(sheet.dimensions)
    # 获取单元格的最大行、最大列
    print(sheet.max_row, sheet.max_column)

    # 通过cell获取指定单元格的数据
    print(sheet.cell(3, 3).value)
    # 通过指定单元格坐标获取对应单元格
    print(sheet['D1'].value)

    print('-------获取多个单元格----------')
    # 获取多个单元格
    print(sheet['A1:G2'])

    print('-------读取多个单元格的数据----------')
    # 读取多个单元格的数据
    for cells in sheet['A1:G2']:
        for cell in cells:
            print(cell.value, end=',')
        print()

    print('-------读取所有单元格的数据----------')
    # 按行遍历所有数据
    # for i in range(1, sheet.max_row + 1):
    for i in range(1, 10):
        for j in range(1, sheet.max_column + 1):
            cell = sheet.cell(row=i, column=j)
            print(cell.value, end='\t')

            # 格式化数据
            # print(cell.data_type, end=';')
            # print(type(cell), end=';')
            # if j == 1 and cell.data_type != 'd':
            #     print(f'{cell.value:<10}', end='\t')
            # elif j == 1:
            #     fm_val = cell.value.strftime('%Y/%m/%d')
            #     print(f'{fm_val:<10}', end='\t')
            # elif j == 3:
            #     print(f'{cell.value:<6}', end='\t')
            # elif j == 6:
            #     print(f'{cell.value:<6}', end='\t')
            # else:
            #     print(cell.value, end='\t')
        print()


# -------------------- 写操作 --------------------
def write_excel():
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = 'characters'
    titles = ('姓名', '力量', '敏捷', '耐力', '幸运', '成长', '财富')
    for col_index, title in enumerate(titles):
        sheet.cell(row=1, column=col_index + 1, value=title)

    names = ('kino', 'kirii', 'erms', 'shibo', 'kuroniko', 'kaiba')
    for row_index, name in enumerate(names):
        row = row_index + 2
        for col in range(1, 1 + len(titles)):
            sheet.cell(row=row, column=col, value=name if col == 1 else random.randint(1, 101))

    wb.save('./testFile/ExcelTest1.xlsx')


# -------------------- main --------------------

def main():
    # read_excel()
    write_excel()


if __name__ == '__main__':
    main()
