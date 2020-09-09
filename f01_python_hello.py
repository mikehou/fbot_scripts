"""
  若當作一般的 python interpreter，沒操作到硬體，則不用 botlib 也可以
"""

import sys


for i in range(1, 5):
  print(i)

print(sys.argv)

line = '1234'
print(line)
print(line)

line = 'abcd\n'
print(line)
print(line)
