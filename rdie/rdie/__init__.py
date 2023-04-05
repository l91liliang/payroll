'''
Author: l91liliang l91liliang@gmail.com
Date: 2023-04-04 17:29:47
LastEditors: l91liliang l91liliang@gmail.com
LastEditTime: 2023-04-04 17:38:18
FilePath: /payroll/rdie/rdie/__init__.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import pymysql
pymysql.version_info = (1, 4, 3, "final", 0)
pymysql.install_as_MySQLdb()

# (1, 4, 0, "final", 0)是为了快速解决这个报错：django.core.exceptions.ImproperlyConfigured: mysqlclient 1.4.0 or newer is required; you have 0.10.1.