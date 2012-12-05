# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function

END = '絅'

class WordDict(dict):
  _special = {
    '#': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
  }
  def has_key(self, k):
    exists = super(WordDict, self).has_key(k)
    extras = []
    for special in self._special:
      if super(WordDict, self).has_key(special):
        extra = k in self._special[special]
        extras.append(extra)
    return any(extras) or exists

class Chunk():
  stack = []

  def __init__(self):
    self.chunks = WordDict()

  def add(self, words):
    if not words:
      self.chunks[END] = True
      return

    exists = self.chunks.has_key(words[0])
    if exists:
      child = self.chunks[words[0]]
      child.add(words[1:])
    else:
      new_word = Chunk()
      self.chunks[words[0]] = new_word
      new_word.add(words[1:])

  def push(self, word):
    self.stack.insert(0, word)

  def find(self, words):
    self.clean() # 确保stack 为空
    position = self._find(words, 0)
    return words[:position], position

  def _find(self, words, position):
    if self.chunks.has_key(END): # 如果全匹配了，记录之
      self.push(words[:position])
    if position >= len(words):
      # 匹配到顶了，两种情况
      # 1. pop出stack里的最大匹配字
      # 2. 没有任何字，返回位置 1
      result = self.pop()
      return len(result) or 1

    word = words[position]
    if self.chunks.has_key(word):
      child = self.chunks.get(word, self)
      if child == self: # 特殊匹配
        self.push(words[:position+1])
      return child._find(words, position+1)
    else:
      # chunks到顶了 没有匹配成功
      result = self.pop()
      return len(result) or 1

  def clean(self):
    self.stack = []

  def pop(self):
    if not self.stack:
      result = ''
    else:
      result = self.stack[0]
    return result

class Segment():
  def __init__(self):
    self.chunks = Chunk()

  def add(self, words):
    if isinstance(words, basestring):
      words = [words, ]
    for word in words:
      self.chunks.add(word)

  def find(self, words):
    return self.chunks.find(words)

  def seg_text(self, words):
    word = True
    while word:
      word, num = self.find(words)
      words = words[num:]
      yield word

def test():
  word1 = u"土耳其"
  word2 = u'伊斯坦布尔'
  word3 = u'土耳其伊斯兰教'
  word4 = u'伊斯兰'
  seg = Segment()
  seg.add([word1, word2, word3, word4])
  for i in seg.seg_text(u'伊斯坦布尔位于土耳其伊斯坦堡'):
    if len(i) > 1:
      print(i)