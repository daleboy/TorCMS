# -*- coding: utf-8 -*-

'''
script for initialization.
'''



from .script_gen_xlsx import gen_xlsx_table
from .script_gen_xlsx_info import gen_xlsx_table_info


def run_init(*args):
    '''
    running init.
    '''
    gen_xlsx_table()

    gen_xlsx_table_info()



