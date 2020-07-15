from botlib import *



def restoreParameters(filename):
  import os
  import sys
  import re
  
  if not os.path.exists(filename):
    print('檔案 {} 不存在'.format(filename))
    return
  
  pattern = re.compile(r'([0-9]+):([0-9]+)')
  with open(filename, 'r') as f:
    for line in f:
      line = line.rstrip()
      matched = pattern.match(line)
      if matched:
        param = matched[1]
        gcode = 'F22 P{} V{}'.format(param, matched[2])
        print('run gcode:', gcode)
        bot.gcodes(gcode)


if __name__ == "__main__":
  try:
    bot.connect()
    restoreParameters('params.txt')
  finally:
    bot.close()
  
  
  