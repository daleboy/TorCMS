# -*- coding:utf-8 -*-
'''
Index for the application.
'''
import config
from torcms.core.base_handler import BaseHandler

from config import CMS_CFG


class ExtExcelHandler(BaseHandler):
    '''
    Index for the application.
    '''

    def initialize(self, **kwargs):
        super(ExtExcelHandler, self).initialize()

    def get(self, *args, **kwargs):
        url_str = args[0]
        url_arr = self.parse_url(url_str)

        if args[0] == 'list':
            self.list()
        elif len(url_arr) == 1:

            self.view(url_str)
        else:
            self.render('misc/html/404.html', kwd={}, userinfo=self.userinfo)

    def index(self):
        '''
        Index funtion.
        '''

        self.render('ext_excel/index.html',
                    userinfo=self.userinfo,

                    cfg=CMS_CFG,
                    kwd={}, )

    def list(self):

        kwd = {}
        stg_table_name = 'ext_xlsx'

        select_stg_sql = "SELECT * from  %s;" % (stg_table_name)

        conn = config.DB_CON
        cur = conn.cursor()
        cur.execute(select_stg_sql)
        postinfo = cur.fetchall()

        index = cur.description

        result = []
        for res in postinfo:

            row = {}
            for i in range(len(index) - 1):
                row[index[i][0]] = res[i]
            result.append(row)

        conn.commit()
        conn.close()
        self.render('ext_excel/list.html',
                    userinfo=self.userinfo,
                    result=result,
                    postinfo=postinfo,
                    kwd=kwd,
                    )

    def view(self, uid):

        kwd = {'uid': uid}
        stg_table_name = 'ext_xlsx'

        select_stg_sql = "SELECT * from  %s WHERE id = '%s';" % (stg_table_name, uid)

        conn = config.DB_CON
        cur = conn.cursor()
        cur.execute(select_stg_sql)
        postinfo = cur.fetchall()
        index = cur.description

        result = []
        for res in postinfo:

            row = {}
            for i in range(len(index) - 1):
                row[index[i][0]] = res[i]
            result.append(row)

        conn.commit()
        conn.close()

        self.render('ext_excel/view.html',
                    userinfo=self.userinfo,
                    postinfo=postinfo,
                    result=result,
                    kwd=kwd,
                    )
