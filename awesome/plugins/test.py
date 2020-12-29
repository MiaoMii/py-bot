#  -*- coding: GBK -*
# UTF - 8
import os
import xlrd

# print(os.path.dirname(__file__))
# excel路径
# os.path.join 把目录和文件名合成一个路径
# os.path.dirname(name) 返回文件所在路径
# excel_path = os.path.join(os.path.dirname(__file__), 'cityCode.xlsx')

# 使用 x l r d 创建一个工作薄对象
# workbook = xlrd.open_workbook(excel_path)
# print(data)
# 根据工作表的名称创建表格对象
# sheet = workbook.sheet_by_name('sheet1')
# 获取总行数
# print(sheet.nrows)      # 结果：4
# file = open('./cityCode.xlsx', 'rb')
# file = file.decode("utf-8")
# xlrd.Book.encoding = "gbk"
data = xlrd.open_workbook(r'./cityCode.xls', encoding_overwrite='utf-8')
index = data.sheet_names()[0]
sheet2 = data.sheet_by_name(index)

# 遍历
nrows = sheet2.nrows
for i in range(nrows):
    print(sheet2.row_values(i))
