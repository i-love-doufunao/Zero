# -*- coding: utf-8 -*-

"""
职位
"""


class Job:
    name = ''
    publishTime = ''
    company = ''
    salary = ''
    url = ''
    locate = ''

    def __init__(self, _name, _publishTime, _locate, _url, _company, _salary):
        self.name = _name
        self.publishTime = _publishTime
        self.locate = _locate
        self.url = _url
        self.company = _company
        self.salary = _salary