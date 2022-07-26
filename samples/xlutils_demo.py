#!/usr/bin/env python
# encoding: utf-8
# @author:Yuchengyu
# @time: 2022/7/25 0025 18:30
# import xlutils
import xlrd2
import os
from xlutils.copy import copy


excel_path=os.path.join( os.path.dirname(__file__),'data/excel_data.xls')
wb=xlrd2.open_workbook(excel_path,formatting_info=True)
index_num=wb.sheet_names().index('Sheet1')
# sheet1=wb.sheet_by_index(0)
# print(sheet1.cell_value(0,0))
new_wb=copy(wb) # 已经变成可写 xlwt对象
sheet=new_wb.get_sheet(index_num)
sheet.write(2,3,60)
new_wb.save(excel_path)



