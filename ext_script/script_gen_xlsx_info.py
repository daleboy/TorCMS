# -*- coding: utf-8


import os
import config
from openpyxl.reader.excel import load_workbook
from xlrd import open_workbook


def gen_xlsx_table_info():
    '''
    向表中插入数据
    '''

    XLSX_FILE = './database/esheet/20180811.xlsx'
    if os.path.exists(XLSX_FILE):
        pass
    else:
        return

    RAW_LIST = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    FILTER_COLUMNS = RAW_LIST + ["A" + x for x in RAW_LIST] + \
                     ["B" + x for x in RAW_LIST] + \
                     ["C" + x for x in RAW_LIST] + \
                     ["D" + x for x in RAW_LIST]

    tvalue = []

    file_d = open_workbook(XLSX_FILE)
    # 获得第一个页签对象


    x = 0
    for sheet_ranges in load_workbook(filename=XLSX_FILE):

        select_sheet = file_d.sheets()[x]

        # 获取总共的行数
        rows_num = select_sheet.nrows + 1

        for row_num in range(6, rows_num):
            tvalue = []
            for xr in FILTER_COLUMNS:

                row1_val = sheet_ranges[xr + '1'].value
                row4_val = sheet_ranges[xr + '{0}'.format(row_num)].value

                if row1_val:
                    if row4_val == None:
                        row4_val = ''
                    tvalue.append(row4_val)

            insert_tab(tvalue)
        x = x + 1
    print("成功插入 " + str(rows_num - 6) + " 行数据")


def insert_tab(tvalue):
    ttvalue = str(tvalue)[1:-1]
    stg_table_name = 'ext_xlsx'

    insert_stg_sql = "INSERT INTO %s VALUES (\n%s );" % (stg_table_name, ttvalue)

    conn = config.DB_CON
    cur = conn.cursor()
    cur.execute(insert_stg_sql)

    conn.commit()
    conn.close()


if __name__ == '__main__':
    gen_xlsx_table_info()
