#!/usr/bin/env python
# encoding: utf-8
# @author:Yuchengyu
# @time: 2022/7/14 0014 14:05
import os
import xlrd2
from common.config_utils import read_config
from xlutils.copy import copy

dir_path = os.path.join(os.path.dirname(__file__), '..',read_config.get_case_data_path)
class ExcelUtils:
    def __init__(self,sheet_name,excel_path=dir_path):
        self.excel_path=excel_path
        self.sheet_name=sheet_name
        self.wb = xlrd2.open_workbook(self.excel_path,formatting_info=True)
        self.sheet=self.get_sheet()



    def get_sheet(self):
        sheet = self.wb.sheet_by_name(self.sheet_name)
        return sheet

    def get_row_count(self):
        return self.sheet.nrows

    def get_col_count(self):
        return self.sheet.ncols

    def get_cell_value(self,row_index, col_index):
        return self.sheet.cell_value(row_index, col_index)

    def get_merge_value(self,row_index, col_index):
        value = self.get_cell_value(row_index, col_index)
        for (rlow, rhign, clow, chigh) in self.sheet.merged_cells:
            if row_index >= rlow and row_index < rhign:
                if col_index >= clow and col_index < chigh:
                    value = self.get_cell_value(rlow, clow)
        return value

    def get_sheet_data_dict(self):
        all_data_list = []
        for i in range(1, self.get_row_count()):
            data_list = {}
            for j in range(self.get_col_count()):
                data_list[self.get_merge_value(0, j)] = self.get_merge_value(i, j)
            all_data_list.append(data_list)
        return  all_data_list

    def update_excel_data(self,row_id,col_id,content):
        self.wb = xlrd2.open_workbook(self.excel_path,formatting_info=True)
        new_wb = copy(self.wb)
        sheet = new_wb.get_sheet(self.wb.sheet_names().index(self.sheet_name))
        sheet.write(row_id, col_id, content)
        new_wb.save(self.excel_path)


if __name__=='__main__':
    excle_utils = ExcelUtils('Sheet1').get_sheet_data_dict()
    print(excle_utils)
    # str1=excle_utils.sheet.row(0)
    # print(str1)
    # dict1=excle_utils.get_sheet_data_dict()
    # print(dict1)