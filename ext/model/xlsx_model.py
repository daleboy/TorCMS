# -*- coding:utf-8 -*-

'''
Model for Posts.
'''



from torcms.model.abc_model import Mabc



class MXlsx(Mabc):
    '''
    Model for catalog list.
    '''

    def __init__(self):
        super(MXlsx, self).__init__()



    @staticmethod
    def query_all():
        '''
        查询全部记录
        '''

        # recs = ext_xlsx.select().where()
        # return recs
