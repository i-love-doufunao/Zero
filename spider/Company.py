# -*- coding: utf-8 -*-

"""
公司概括
org_industry是网站对公司的分类
industry是程序修正后的分类
"""


class Company:
    name = ''
    industry = ''
    # 所在城市
    locate = ''
    # 链接
    locateUrl = ''
    keyword = ''
    # 行业
    org_industry = ''
    # 地址
    address = ''

    def __init__(self, _name, _industry, _locate, url, org_ind):
        name = _name
        industry = _industry
        locate = _locate
        locateUrl = url
        org_industry = org_ind
