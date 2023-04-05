'''
Author: l91liliang l91liliang@gmail.com
Date: 2023-04-04 17:30:18
LastEditors: l91liliang l91liliang@gmail.com
LastEditTime: 2023-04-04 18:28:24
FilePath: /payroll/rdie/accounting/admin.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from django.contrib import admin
from .models import *

admin.site.register(Currency)
admin.site.register(Account)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(HistoryRecord)