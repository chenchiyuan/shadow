# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function

from xlwt import Workbook
from xlrd import open_workbook

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

class ExcelWriter(object):
  def __init__(self, filename, encoding='utf-8', sheets=[]):
    self.filename = filename
    self.sheets = sheets
    self.encoding = encoding

  def draw(self):
    workbook = Workbook(encoding=self.encoding)
    for sheet in self.sheets:
      sheet.draw(workbook)

    workbook.save(self.filename)

class ExcelReader(object):
  def __init__(self, filename, callback,
               encoding='utf-8', ignore_first=True):
    self.filename = filename
    self.encoding = encoding
    self.ignore_first = ignore_first
    self.callback = callback

  def read(self):
    workbook = open_workbook(self.filename)
    for sheet in workbook.sheets():
      print("Sheet %s" % sheet.name)
      rows = range(sheet.nrows) if not self.ignore_first else range(1, sheet.nrows)
      for row in rows:
        values = []
        for col in range(sheet.ncols):
          values.append(sheet.cell(row, col).value)
        self.callback(values)

def write_example():
  content = u'我爱\t北京\t天安门\n你爱\t高鹏\t韩国人\n'

  def callback(content):
    lines = content.split('\n')
    for line in lines:
      yield line.split('\t')

  sheet = ExcelSheet(sheet_name='test', data=content, callback=callback,
                     rows=[u'一', u'二', u'三'])
  excel = ExcelWriter(filename='first.xls', sheets=[sheet])
  excel.draw()

def reader_example():
  def callback(content_list):
    name, city, place = content_list
    print(name, city, place)

  reader = ExcelReader(filename='first.xls', callback=callback)
  reader.read()