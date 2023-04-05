'''
Author: l91liliang l91liliang@gmail.com
Date: 2023-04-04 22:18:16
LastEditors: l91liliang l91liliang@gmail.com
LastEditTime: 2023-04-05 17:41:15
FilePath: /payroll/rdie/accounting/form.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# from django import forms
# from .models import HistoryRecord

# class HistoryRecordForm(forms.ModelForm):
#     class Meta:
#         model = HistoryRecord
#         exclude = ['created_date', 'updated_date']
from django import forms
from .models import HistoryRecord, TransferRecord


class HistoryRecordForm(forms.ModelForm):
    class Meta:
        model = HistoryRecord
        # fields = '__all__'
        exclude = ['created_date', 'updated_date']


class TransferRecordForm(forms.ModelForm):
    class Meta:
        model = TransferRecord
        exclude = ['created_date', 'updated_date', 'currency']