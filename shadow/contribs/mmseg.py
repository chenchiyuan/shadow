# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from max_match import Segment as NewSegment

# TODO 算法有点小瑕疵，仔细思考下。
SAFE_END = u'絅'

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

class Word(object):
  def __init__(self):
    self.words = WordDict()
    self.stack = []

  def push(self, word):
    self.stack.insert(0, word)

  def clean(self):
    self.stack = []

  def get_word(self):
    if not self.stack:
      result = ''
    else:
      result = self.stack[0]
    self.clean()
    return result

  def add(self, words):
    if not words:
      self.words[SAFE_END] = True
      return

    exists = self.words.has_key(words[0])
    if exists:
      child = self.words[words[0]]
      child.add(words[1:])
    else:
      new_word = Word()
      self.words[words[0]] = new_word
      new_word.add(words[1:])

  def find(self, words, num=0):
    if num >= len(words):
      self.clean()
      return 1

    word = words[num]
    if self.words.has_key(SAFE_END):
      self.push(word[:num])

    if self.words.has_key(word):
      child = self.words.get(word, self)
      if child == self:
        self.push(word[:num])
        
      return child.find(words, num+1)
    else:
      if self.words.has_key(SAFE_END):
        return num or 1
      else:
        return len(self.get_word()) or 1

class SegmentDummy(object):
  def __init__(self):
    self.word = Word()

  def add(self, words):
    if isinstance(words, basestring):
      words = [words, ]
    for word in words:
      self.word.add(word)

  def find(self, words):
    num = self.word.find(words)
    return words[:num], num

  def seg_text(self, words):
    words += SAFE_END
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
  seg = NewSegment()
  seg.add([word1, word2, word3, word4])
  for i in seg.seg_text(u'伊斯坦布尔位于土耳其伊斯坦堡'):
    if len(i) > 1:
      print(i)

Segment = NewSegment