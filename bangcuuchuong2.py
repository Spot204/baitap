i = 0
while i < 10:
  j= 0
  i += 1
  while j < 10:
      j += 1
      if j != 10:
        print(i,'x',j,'=',j*i,end='\t|')
      else:
        print(i,'x',j,'=',j*i)