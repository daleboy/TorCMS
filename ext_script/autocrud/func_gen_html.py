# -*- coding:utf-8 -*-

'''
The functions for generating add, edit, view HTML file.
for each item.
'''
from .html_tpl import HTML_TPL_DICT




def gen_input_view(sig_dic):
    '''
    Viewing the HTML text.
    '''

    html_str = HTML_TPL_DICT['input_view'].format(
        sig_dic['en'],
        sig_dic['zh'],
        sig_dic['dic'][1],
    )
    return html_str





def gen_radio_view(sig_dic):
    '''
    for checkbox
    '''
    view_zuoxiang = '''
    <div class="col-sm-4"><span class="des">{0}</span></div>
    <div class="col-sm-8">
    '''.format(sig_dic['zh'])

    dic_tmp = sig_dic['dic']
    for key in dic_tmp.keys():
        tmp_str = '''<span class="input_text">
         {{% if  '{0}' in postinfo.extinfo and postinfo.extinfo['{0}'] == "{1}" %}}
         {2}
         {{% end %}}
         </span>'''.format(sig_dic['en'], key, dic_tmp[key])
        view_zuoxiang += tmp_str

    view_zuoxiang += '''</div>'''
    return view_zuoxiang



def gen_checkbox_view(sig_dic):
    '''
    for checkbox
    '''
    view_zuoxiang = '''
    <div class="col-sm-4"><span class="des">{0}</span></div>
    <div class="col-sm-8">
    '''.format(sig_dic['zh'])

    dic_tmp = sig_dic['dic']
    for key in dic_tmp.keys():
        tmp_str = '''
         <span>
         {{% if "{0}" in postinfo.extinfo["{1}"] %}}
         {2}
         {{% end %}}
         </span>
         '''.format(key, sig_dic['en'], dic_tmp[key])
        view_zuoxiang += tmp_str

    view_zuoxiang += '''</div>'''
    return view_zuoxiang



def gen_select_view(sig_dic):
    '''
    HTML view, for selection.
    '''
    option_str = ''
    dic_tmp = sig_dic['dic']
    for key, val in dic_tmp.items():
        tmp_str = '''
         {{% if '{sig_en}' in postinfo.extinfo %}}
          {{% set tmp_var = postinfo.extinfo["{sig_en}"] %}}
          {{% if tmp_var == "{sig_key}" %}}
          {sig_dic}
          {{% end %}}
          {{% end %}}
         '''.format(sig_en=sig_dic['en'], sig_key=key, sig_dic=val)
        option_str += tmp_str

    return '''
    <div class="row">
    <div class="col-sm-4"><span class="des"><strong>{sig_zh}</strong></span></div>
    <div class="col-sm-8">
    {option_str}
    </div></div>
    '''.format(sig_zh=sig_dic['zh'], option_str=option_str)



def gen_file_view(sig_dic):
    '''
    for file viewing.
    '''
    _ = sig_dic
    view_html = ''
    return view_html


def gen_input_list(sig_dic):
    '''
    For generating List view HTML file for INPUT.
    for each item.
    '''
    out_str = '''
    <div class="col-sm-4"><span class="des">{1}</span></div>
    <div class="col-sm-8">
    <span class="iga_pd_val">{{{{ postinfo.extinfo['{0}'][0] }}}} {2}</span>
    </div>
    '''.format(sig_dic['en'], sig_dic['zh'], sig_dic['dic'][1])
    return out_str


def gen_radio_list(sig_dic):
    '''
    For generating List view HTML file for RADIO.
    for each item.
    '''
    view_zuoxiang = '''<span class="iga_pd_val">'''

    dic_tmp = sig_dic['dic']
    for key in dic_tmp.keys():
        tmp_str = '''{{% if postinfo.extinfo['{0}'][0] == "{1}" %}} {2} {{% end %}}
        '''.format(sig_dic['en'], key, dic_tmp[key])
        view_zuoxiang += tmp_str

    view_zuoxiang += '''</span>'''
    return view_zuoxiang


def gen_checkbox_list(sig_dic):
    '''
    For generating List view HTML file for CHECKBOX.
    for each item.
    '''
    view_zuoxiang = '''<span class="iga_pd_val">'''

    dic_tmp = sig_dic['dic']
    for key in dic_tmp.keys():
        tmp_str = '''{{% if "{0}" in postinfo.extinfo["{1}"] %}} {2}  {{% end %}}
        '''.format(key, sig_dic['en'], dic_tmp[key])
        view_zuoxiang += tmp_str

    view_zuoxiang += '''</span>'''
    return view_zuoxiang


def gen_select_list(sig_dic):
    '''
    For generating List view HTML file for SELECT.
    for each item.
    '''
    view_jushi = '''<span class="label label-primary" style="margin-right:10px">'''

    dic_tmp = sig_dic['dic']
    for key in dic_tmp.keys():
        tmp_str = '''{{% if '{0}' in postinfo.extinfo and postinfo.extinfo["{0}"][0] == "{1}" %}}
         {2} {{% end %}}'''.format(sig_dic['en'], key, dic_tmp[key])
        view_jushi += tmp_str

    view_jushi += '''</span>'''
    return view_jushi
