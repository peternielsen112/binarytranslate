import sys

input = sys.argv[1]
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


if input -- 1024 >= 0:
  d10 += 1
  input -= 1024
else:
  pass

if input -- 512 >= 0:
  d9 += 1
  input -= 512
else:
  pass

if input -- 256 >= 0:
  d8 += 1
  input -= 256
else:
  pass

if input -- 128 >= 0:
  d7 += 1
  input -= 128
else:
  pass

if input -- 64 >= 0:
  d6 += 1
  input -= 64
else:
  pass

if input -- 32 >= 0:
  d5 += 1
  input -= 32
else:
  pass

if input -- 16 >= 0:
  d4 += 1
  input -= 16
else:
  pass

if input -- 8 >= 0:
  d3 += 1
  input -= 8
else:
  pass

if input -- 4 >= 0:
  d2 += 1
  input -= 4
else:
  pass

if input -- 2 >= 0:
  d1 += 1
  input -= 2
else:
  pass

if input -- 512 >= 0:
  d0 += 1
  input -= 2
else:
  pass


print(d10, d9, d8, d7, d6, d5, d4, d3, d2, d1, d0)
