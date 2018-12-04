# -*- coding:utf-8 -*-

'''
Log handler.
'''

from concurrent.futures import ThreadPoolExecutor

from torcms.core.base_handler import BaseHandler

from torcms.core import tools
from torcms.model.log_model import MLog
from config import CMS_CFG


class LogHandler(BaseHandler):
    '''
    Log handler.
    '''
    executor = ThreadPoolExecutor(2)

    def initialize(self, **kwargs):
        super(LogHandler, self).initialize()

    def get(self, *args, **kwargs):

        url_str = args[0]

        url_arr = self.parse_url(url_str)

        if url_str == '':
            self.list()
        elif len(url_arr) == 1:
            self.list(url_arr[0])
        elif len(url_arr) == 2:
            self.user_log_list(url_arr[0], url_arr[1])
        else:
            self.render('misc/html/404.html', userinfo=self.userinfo, kwd={})

    def list(self, cur_p=''):
        '''
        View the list of the Log.
        '''

        if cur_p == '':
            current_page_number = 1
        else:
            current_page_number = int(cur_p)

        current_page_number = 1 if current_page_number < 1 else current_page_number

        pager_num = int(MLog.total_number() / CMS_CFG['list_num'])
        kwd = {
            'pager': '',
            'title': '',
            'current_page': current_page_number,
        }

        if self.is_p:
            self.render('admin/log_ajax/user_list.html',
                        kwd=kwd,

                        user_list=MLog.query_all_user(),
                        format_date=tools.format_date,
                        userinfo=self.userinfo)
        else:
            self.render('misc/log/user_list.html',
                        kwd=kwd,

                        user_list=MLog.query_all_user(),
                        format_date=tools.format_date,
                        userinfo=self.userinfo)

    def user_log_list(self, userid, cur_p=''):
        '''
        View the list of the Log.
        '''

        if cur_p == '':
            current_page_number = 1
        else:
            current_page_number = int(cur_p)

        current_page_number = 1 if current_page_number < 1 else current_page_number

        pager_num = int(MLog.total_number() / CMS_CFG['list_num'])
        kwd = {
            'pager': '',
            'title': '',
            'current_page': current_page_number,
            'user_id': userid,
        }

        if self.is_p:
            self.render('admin/log_ajax/user_log_list.html',
                        kwd=kwd,
                        infos=MLog.query_pager_by_user(userid,
                                                       current_page_num=current_page_number),

                        format_date=tools.format_date,
                        userinfo=self.userinfo)
        else:
            self.render('misc/log/user_log_list.html',
                        kwd=kwd,
                        infos=MLog.query_pager_by_user(userid,
                                                       current_page_num=current_page_number),

                        format_date=tools.format_date,
                        userinfo=self.userinfo)


class LogPartialHandler(LogHandler):
    '''
    Partially render for user handler.
    '''

    def initialize(self, **kwargs):
        super(LogPartialHandler, self).initialize()
        self.is_p = True
