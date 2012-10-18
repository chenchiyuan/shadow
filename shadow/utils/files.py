# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from xlwt import Workbook

class ExcelSheet(object):
  def __init__(self, sheet_name, data, callback, rows=[]):
    self.sheet_name = sheet_name
    self.callback = callback
    self.rows = rows
    self.data = data

  def draw(self, workbook):
    # Draw rows
    sheet = workbook.add_sheet(self.sheet_name)
    for i, row in enumerate(self.rows):
      sheet.write(0, i, row)

    for i, seq in enumerate(self.callback(self.data)):
      for j, info in enumerate(seq):
        sheet.row(i+1).write(j, info)
      sheet.flush_row_data()

class Excel(object):
  def __init__(self, filename, encoding='utf-8', sheets=[]):
    self.filename = filename
    self.sheets = sheets
    self.encoding = encoding

  def draw(self):
    workbook = Workbook(encoding=self.encoding)
    for sheet in self.sheets:
      sheet.draw(workbook)

    workbook.save(self.filename)

def test():
  content = u'我爱\t北京\t天安门\n你爱\t高鹏\t韩国人\n'

  def callback(content):
    lines = content.split('\n')
    for line in lines:
      yield line.split('\t')

  sheet = ExcelSheet(sheet_name='test', data=content, callback=callback,
                     rows=[u'一', u'二', u'三'])
  excel = Excel(filename='first.xls', sheets=[sheet])
  excel.draw()
  