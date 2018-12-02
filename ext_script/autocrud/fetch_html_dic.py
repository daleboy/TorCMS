# -*- coding: utf-8


import os
import sys

from openpyxl.reader.excel import load_workbook
from .base_crud import XLSX_FILE, FILTER_COLUMNS, INPUT_ARR

if os.path.exists(XLSX_FILE):
    WORK_BOOK = load_workbook(filename=XLSX_FILE)
else:
    print('There must be at least one XLSX file.')
    sys.exit(0)


def __write_filter_dic(wk_sheet, column):
    '''
    return filter dic for certain column
    '''
    row1_val = wk_sheet['{0}1'.format(column)].value
    row2_val = wk_sheet['{0}2'.format(column)].value
    row3_val = wk_sheet['{0}3'.format(column)].value
    row4_val = wk_sheet['{0}4'.format(column)].value

    if row1_val and row1_val.strip() != '':
        row2_val = row2_val.strip()

        slug_name = row1_val.strip()
        c_name = row2_val.strip()

        tags1 = [x.strip() for x in row3_val.split(',')]
        tags_dic = {}

        #  if only one tag,
        if len(tags1) == 1:
            xx_1 = row2_val.split(':')  # 'text'  # HTML text input control.

            if xx_1[0].lower() in INPUT_ARR:
                xx_1[0] = xx_1[0].lower()
            else:
                xx_1[0] = 'text'

            if len(xx_1) == 2:
                ctr_type, unit = xx_1
            else:
                ctr_type = xx_1[0]
                unit = ''
            tags_dic[1] = unit

        else:
            ctr_type = 'select'  # HTML selectiom control.
            for index, tag_val in enumerate(tags1):
                # the index of tags_dic starts from 1.
                tags_dic[index + 1] = tag_val.strip()

        outkey = 'html_{0}'.format(slug_name)
        outval = {
            'en': slug_name,
            'zh': c_name,
            'dic': tags_dic,
            'type': ctr_type,
            'display': row4_val,
        }
        return (outkey, outval)
    else:
        return (None, None)


def gen_html_dic():
    '''
    生成 Filter .
    '''

    if WORK_BOOK:
        pass
    else:
        return False

    html_dics = {}
    for wk_sheet in WORK_BOOK:
        for column in FILTER_COLUMNS:
            kkey, kval = __write_filter_dic(wk_sheet, column)
            if kkey:
                html_dics[kkey] = kval

    return html_dics


def gen_array_crud():
    if WORK_BOOK:
        pass
    else:
        return False

    switch_dics = {}
    u_dic = []

    for work_sheet in WORK_BOOK:

        for col_num in FILTER_COLUMNS:

            cell_val = work_sheet['{0}1'.format(col_num)].value

            if cell_val != None:
                u_dic.append(cell_val)
                switch_dics['dic_{0}'.format(col_num)] = u_dic

    return (switch_dics)
