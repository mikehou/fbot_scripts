"""
使用高階的 bot.pos 控制 fbot 的位置
"""


from botlib import *
from datetime import datetime
import time

# 也可以把其他寫好的 scripts 拿進來用
# 這裡用 f03_測試LED.py 內的 blinkLED（）
from f03_測試LED import *

def move():
  print(datetime.now())  # 顯示目前時間

  bot.pos = 290,0,0
  print(datetime.now())  
  bot.pos = 290,150,0  
  print(datetime.now())  
  bot.pos = 0,150,0  
  print(datetime.now())  
  bot.pos = 0,0,0
  print(datetime.now())  
  bot.pos = 0,0,280
  print(datetime.now())  
  bot.pos = 0,0,0  
  print(datetime.now())
  print('花費時間 =', time.time() - now, "秒")
  
  blinkLED() # 來自 f02_測試LED.py

try:
  now = time.time()
  bot.connect()
  move()

finally:
  bot.close()
