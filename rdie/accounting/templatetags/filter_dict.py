'''
Author: l91liliang l91liliang@gmail.com
Date: 2023-04-04 23:22:15
LastEditors: l91liliang l91liliang@gmail.com
LastEditTime: 2023-04-04 23:22:26
FilePath: /payroll/rdie/accounting/templatetags/filter_dict.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from django import template

register = template.Library()

@register.filter('get_dict_value')
def get_dict_value(d, key):
    return d[key]