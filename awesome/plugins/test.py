#  -*- coding: GBK -*
# UTF - 8
import os
import xlrd

# print(os.path.dirname(__file__))
# excel·��
# os.path.join ��Ŀ¼���ļ����ϳ�һ��·��
# os.path.dirname(name) �����ļ�����·��
# excel_path = os.path.join(os.path.dirname(__file__), 'cityCode.xlsx')

# ʹ�� x l r d ����һ������������
# workbook = xlrd.open_workbook(excel_path)
# print(data)
# ���ݹ���������ƴ���������
# sheet = workbook.sheet_by_name('sheet1')
# ��ȡ������
# print(sheet.nrows)      # �����4
# file = open('./cityCode.xlsx', 'rb')
# file = file.decode("utf-8")
# xlrd.Book.encoding = "gbk"
data = xlrd.open_workbook(r'./cityCode.xls', encoding_overwrite='utf-8')
index = data.sheet_names()[0]
sheet2 = data.sheet_by_name(index)

# ����
nrows = sheet2.nrows
for i in range(nrows):
    print(sheet2.row_values(i))
