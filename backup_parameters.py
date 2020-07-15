"""
測試儲存參數
"""



from botlib import *



def saveParameters(saveFilename):
  import re
  pattern = re.compile(r'R21 P([0-9]+) V([0-9]+) Q.*')
  lines = bot.gcodes("F20")
  with open(saveFilename, 'w') as f:
    for line in lines:
      print('response: ', line)
      line = line.rstrip()
      matched = pattern.match(line)
      if matched:
        print(matched[1], matched[2])
        f.write('{}:{}\n'.format(matched[1], matched[2]))
  print('所有參數已儲存到 {}'.format(saveFilename))

  
  
if __name__ == "__main__":
  try:
    bot.connect()
    saveParameters('params.txt')
  finally:
    bot.close()