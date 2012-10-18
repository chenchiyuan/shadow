# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function

TOTAL_LENGTH = 6 #ids count is 503284375 = count ** (TOTAL_LENGTH - 1)
alphabet = 'IjC2xBeqkfnAMD7XLFbSsJg31haUpWumENGvQc5izPH9ZwlK486doV'
flag = ['T', 'Y', 'R', 'r', 't', 'y']
count = len(alphabet)
PATCH_0 = 'TYRrty'
PATCH_1 = 'ytrRYT'

class HashID(str):
  def __int__(self):
    try:
      s = str(self)
      return int(s)
    except ValueError:
      return decode(self)
    except Exception:
      return decode(self)

def ljust(encoded_data):
  length = len(encoded_data)
  index = alphabet.index(encoded_data[-1])
  excursion = index - length if index > length else length - index
  alpha = list(alphabet[excursion:] + alphabet[:excursion])
  remain = TOTAL_LENGTH - length - 1

  pop_data = ''
  while remain:
    _, position = divmod((TOTAL_LENGTH - remain) * index, remain)
    pop_data = pop_data + alpha.pop(position)
    remain -= 1 # pop_data length based on remain, and data based on excursion, which based on index.

  separate = flag[index%len(flag)] #base 54, so remainder is based on index( X * (54 ** 0))
  return pop_data + separate + encoded_data

def _encode(item):
  assert isinstance(item, (int, long))
  if not item:
    return PATCH_0 # item ==0 , return PATCH_0
  elif item == -1:
    return PATCH_1

  base = ''
  while item:
    item, i = divmod(item, count)
    base = alphabet[i] + base #TO base 54

  h = ljust(base) #ljust item , enforce length = 6
  return HashID(h)

def _decode(item):
  if item == PATCH_0: #patch item 0
    return 0
  elif item == PATCH_1: #patch item -1
    return -1

  index = alphabet.index(item[-1])
  separate = flag[index%len(flag)]
  position = item.index(separate)
  real = 0
  for multi, char in enumerate(item[:position:-1]):
    order = count ** multi
    real += alphabet.index(char) * order
  return real

def _dummy_encode(item):
  return item

def _dummy_decode(item):
  return item

# temporarily set this so that api will not fail
encode = _encode
decode = _decode

if __name__ == '__main__':
  print(encode(123))