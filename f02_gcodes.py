"""
簡易的 gcodes 示範


"""

"""
只要操作到硬體，也就是使用到 fbot 的命令，就必須 import botlib 內的所有東西進來。
而且後面還要 connect()
"""
from botlib import *


try:
  # 由於是透過 TCP，所以要連線。
  # 而且 bot.connect() 與 bot.close() 成對。
  # 放在 try..finally 內的目的是為了避免 script 寫錯導致直接離開而沒關閉連線
  bot.connect()

  # 每行送出一個 gcode
  bot.gcodes('G00 X5')
  
  # 每行送出一個 gcode
  bot.gcodes('G00 Y5')

  # 也可以多個 gcodes，一樣會循序執行
  bot.gcodes('G00 Z5', 'G00 X0 Y0 Z0')  

  # 也可以把 gcodes 的執行輸出結果顯示出來
  print(bot.gcodes('F41 P9 V1 M0', 'F41 P9 V0 M0'))

finally:
  bot.close()

  