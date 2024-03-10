#!/usr/bin/env python3

import re

class MyString:
  def __init__(self, value=""):
    self.value = value
    
  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    return True if self.value.endswith(".") else False

  def is_question(self):
    return True if self.value.endswith("?") else False

  def is_exclamation(self):
    return True if self.value.endswith("!") else False
  
  def count_sentences(self):
    splitted = re.split(r'[!.?]+',self.value)
    splitted = [i for i in splitted if i]
    return len(splitted)

complex_string = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")
print(complex_string.count_sentences())