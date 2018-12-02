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

        if args[0] == 'index':
            self.index()
        elif args[0] == 'list':
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

        kwd = { }

        self.render('ext_autogen/list/list.html',
                    userinfo=self.userinfo,
                    kwd=kwd,
                    )
