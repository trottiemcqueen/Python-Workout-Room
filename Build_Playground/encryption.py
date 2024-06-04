sentenceKey = '3love6computers2dogs4cats1I5you'
key = '1I 3love 6computers'


def encode(message):
  result = ''
  
  for char in message:
    loc = sentence.find(char)
    result += key(loc)
    
  return result