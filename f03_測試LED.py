"""
這範例利用了 python 的 sys.argv，可以在
下方的 arguments 內填入一個整數，表示LED要閃幾次
"""

from botlib import *
import sys
import time
from datetime import datetime


def blinkLED(count = 1, delay = 0):
  """
  閃爍LED  
  """
  for i in range(count):
    bot.dpin[9]=1
    time.sleep(delay)
    bot.dpin[9]=0
    time.sleep(delay)



if __name__ == "__main__":
  try:
    bot.connect()
    if len(sys.argv)==2:
      count = int(sys.argv[1])
    else:
      count = 1
    blinkLED(count,0.5)    

  finally:
    bot.close()
    
    
    