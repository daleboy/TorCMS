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

        if len(args) == 0 or args[0] == 'index':
            self.index()
        elif len(url_arr) == 1:
            self.view(url_str)
        else:
            self.render('misc/html/404.html', kwd={}, userinfo=self.userinfo)

    def index(self):
        '''
        Index funtion.
        '''


        stg_table_name = 'ext_xlsx'
        conn = config.DB_CON
        cur = conn.cursor()
        select_stg_sql = "SELECT  *  from %s;" % (stg_table_name)
        cur.execute(select_stg_sql)

        recs = cur.fetchall()

        conn.close()

        self.render('ext_excel/index.html',
                    userinfo=self.userinfo,
                    recs = recs,
                    cfg=CMS_CFG,
                    kwd={}, )

    def view(self, uid):
        '''
        View the page.
        '''
        kwd = {
            'pager': '',
        }

        stg_table_name = 'ext_xlsx'
        conn = config.DB_CON
        cur = conn.cursor()
        select_stg_sql = "SELECT  *  from %s WHERE id = %s;" % (stg_table_name,uid)
        cur.execute(select_stg_sql)

        recs = cur.fetchall()

        conn.close()


        self.render('ext_xlsx/ext_view.html',
                    postinfo=recs,


                    cfg=CMS_CFG)