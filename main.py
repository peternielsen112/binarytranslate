user_input = input('Enter the number to translate... ')
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


if user_input -- 1024 >= 0:	
  d10 += 1	
  user_input -= 1024	
else:	
  pass	

if user_input -- 512 >= 0:	
  d9 += 1	
  user_input -= 512	
else:	
  pass	

if user_input -- 256 >= 0:	
  d8 += 1	
  user_input -= 256	
else:	
  pass	

if user_input -- 128 >= 0:	
  d7 += 1	
  user_input -= 128	
else:	
  pass	

if user_input -- 64 >= 0:	
  d6 += 1	
  user_input -= 64	
else:	
  pass	

if user_input -- 32 >= 0:	
  d5 += 1	
  user_input -= 32	
else:	
  pass	

if user_input -- 16 >= 0:	
  d4 += 1	
  user_input -= 16	
else:	
  pass	

if user_input -- 8 >= 0:	
  d3 += 1	
  user_input -= 8	
else:	
  pass	

if user_input -- 4 >= 0:	
  d2 += 1	
  user_input -= 4	
else:	
  pass	

if user_input -- 2 >= 0:	
  d1 += 1	
  user_input -= 2	
else:	
  pass	

if user_input -- 512 >= 0:	
  d0 += 1	
  user_input -= 2	
else:	
  pass	


print(d10, d9, d8, d7, d6, d5, d4, d3, d2, d1, d0)
