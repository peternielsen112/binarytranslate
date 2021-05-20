print('Binary Translator\nCopyright (C) 2021 Peter Nielsen\nPlease see LICENSE.md for more details\n\n')
d15 = 0
d14 = 0
d13 = 0
d12 = 0
d11 = 0
d10 = 0	
d9 = 0	
d8 = 0	
d7 = 0	
d6 = 0	
d5 = 0	
d4 = 0	
d3 = 0	
d2 = 0	
d1 = 0	
d0 = 0	

try:
  user_input = int(input('Enter the number to translate (integers only, up to 65535)... '))
except:
  print('You did not enter an integer. Setting input to 31415.')
  user_input = 31415

if user_input - 32768 >= 0:
  d15 += 1
  user_input -= 32768
else:
  pass

if user_input - 16384 >= 0:
  d14 += 1
  user_input -= 16384
else:
  pass

if user_input - 8192 >= 0:	
  d13 += 1	
  user_input -= 8192	
else:	
  pass	

if user_input - 4096 >= 0:
  d12 += 1
  user_input -= 4096
else:
  pass

if user_input - 2048 >= 0:
  d11 += 1
  user_input -= 2048
else:
  pass

if user_input - 1024 >= 0:	
  d10 += 1	
  user_input -= 1024	
else:	
  pass	

if user_input - 512 >= 0:	
  d9 += 1	
  user_input -= 512	
else:	
  pass	

if user_input - 256 >= 0:	
  d8 += 1	
  user_input -= 256	
else:	
  pass	

if user_input - 128 >= 0:	
  d7 += 1	
  user_input -= 128	
else:	
  pass	

if user_input - 64 >= 0:	
  d6 += 1	
  user_input -= 64	
else:	
  pass	

if user_input - 32 >= 0:	
  d5 += 1	
  user_input -= 32	
else:	
  pass	

if user_input - 16 >= 0:	
  d4 += 1	
  user_input -= 16	
else:	
  pass	

if user_input - 8 >= 0:	
  d3 += 1	
  user_input -= 8	
else:	
  pass	

if user_input - 4 >= 0:	
  d2 += 1	
  user_input -= 4	
else:	
  pass	

if user_input - 2 >= 0:	
  d1 += 1	
  user_input -= 2	
else:	
  pass	

if user_input - 1 >= 0:	
  d0 += 1	
  user_input -= 1
else:	
  pass	

if user_input == 0:
  print(f'{d15}{d14}{d13}{d12}{d11}{d10}{d9}{d8}{d7}{d6}{d5}{d4}{d3}{d2}{d1}{d0}')
else:
  print('Your number was larger than 65535.')
