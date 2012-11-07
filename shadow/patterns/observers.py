# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
class ObserverCenter(object):
  def __init__(self):
    self.watching = {}

  def _do_hash(self, sender, dispatch_id=None):
    return id(dispatch_id or sender)

  def connect(self, receiver, sender, dispatch_id=None):
    hash_id = self._do_hash(sender, dispatch_id)
    if self.watching.has_key(hash_id):
      self.watching[hash_id].append(receiver)
    else:
      self.watching[hash_id] = [receiver, ]

  def send(self, sender, dispatch_id=None, **kwargs):
    hash_id = self._do_hash(sender, dispatch_id)
    responses = []
    for receiver in self.watching.get(hash_id, []):
      responses.append((receiver, receiver(sender=sender, **kwargs)))
    return responses

center = ObserverCenter()

class NotifyList(list):
  def append(self, p_object):
    super(NotifyList, self).append(p_object)
    center.send(sender=self.append, say_what=p_object)

def test():
  def print_after_append(sender, say_what=""):
    print(say_what)

  center.connect(receiver=print_after_append, sender=NotifyList.append)
  ls = NotifyList()
  ls.append("a")
  ls.append("b")

if __name__ == '__main__':
  test()