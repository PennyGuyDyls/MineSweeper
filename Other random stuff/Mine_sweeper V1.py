from random import randint as r

from time import sleep as s

import os

from time import time

 

# NOTES:

# Minesweeper game!

# l = length of board

# h = width of board

# d = density of mines

# x = x axis

# y = y axis

# z = variable always True/False

# vis = board player sees

# board = pre-generated board before game start

# i = first priority for loop variable

# j = second priority for loop variable

# k = third priority for loop variable

 

nums=['0️⃣ ','1️⃣ ','2️⃣ ','3️⃣ ','4️⃣ ','5️⃣ ','6️⃣ ','7️⃣ ','8️⃣ ','9️⃣ ','🔟']

 

def gen(density,x,y):

  board=[]

  indexes=[]

  for i in range(y):

    board.append([])

    for j in range(x):

      board[i].append(' ')

      indexes.append([i,j])

 

  mines=x*y*density//100

 

  while mines>0:

    a=indexes[r(0,len(indexes)-1)]

    board[a[0]][a[1]]='💣'

    mines-=1

    indexes.remove(a)

  return board

 

def numbers(x,y):

  global board

  for i in range(y):

    for j in range(x):

      if board[i][j]=='💣':

        pass

      else:

        num=0

        for k in range(-1,2):

          for l in range(-1,2):

            if 0<=i+k<y and 0<=j+l<x:

              if board[i+k][j+l]=='💣':

                num+=1

        board[i][j]=nums[num]

  return board

 

def genvis(x,y):

  global board

  vis=[]

  for i in range(y):

    vis.append([])

    for j in range(x):

      vis[i].append('⬜')

     

  for i in range(9):

    indexes=[]

    for j in range(x):

      for k in range(y):

        if board[k][j]==nums[i]:

          indexes.append([k,j])

    if indexes != []:

      break

    print(indexes)

    s(5)

  if indexes != []:

    while True:

      a=indexes[r(0,len(indexes)-1)]

      vis[a[0]][a[1]]='🟩'  

      break

  return vis

 

def reveal(m,x,y):

  global board

  global vis

  global l

  global h

  global lives

  global score

  z=1

  if m == 'r':

    if vis[y][x] in '⬜🟩':

      vis[y][x]=board[y][x]

      score+=10

      if vis[y][x]==nums[0]:

        score+=40

        check=[]

        while True:

          if vis==check:

            break

          check=[]

          for i in vis:

            check.append(i.copy())

          for y1 in range(h):

            for x1 in range(l):

              if vis[y1][x1]==nums[0]:

                for i in range(-1,2):

                  for j in range(-1,2):

                    a=y1+j

                    b=x1+i

                    if 0<=b<l and 0<=a<h:

                      vis[a][b]=board[a][b]

 

      elif vis[y][x]=='💣':

        score-=10

        vis[y][x]='💥'

        board[y][x]='💥'

        for i in reversed(range(3)):

          if lives[i]=='❤️':

            lives[i]='🖤'

            break

 

  else:

    if vis[y][x]=='⬜':

      vis[y][x]='🚩'

    elif vis[y][x]=='🚩':

      vis[y][x]='⬜'

 

  return [vis,z]

 

def show():

  global vis

  global l

  global h

  global lives

  global score

  x='▪️'

  if l <= 10:

    if h>10:

      print(x,end=' ')

    print(x,' 🅧',''.join(nums[1:l+1]))

 

  else:

    if h>10:

      print(x,end=' ')

    print(x,' 🅧',end=' ')

    for i in range(l//10+1):

      if i == l//10:

        print((nums[i])*(l%10+1))

      elif i == 0:

        print((nums[i])*9, end='')

      else:

        print((nums[i])*10,end='')

    if h>10:

      print(x,end=' ')

    print(x,' 🅧',''.join(nums[1:10]),end='')

    print((''.join(nums[:10])+' ')*(l//10-1),end='')

    print(''.join(nums[:l%10+1]))

 

  if h<=10:

    print(' 🅨︎ '+ (x+' ') * (l+1))

    for i in range(h):

      if i+1==h//3:

        print(nums[i+1],x,''.join(vis[i]), end='')

        print('   lives:', *lives)

      elif i+1==2*h//3:

        print(nums[i+1],x,''.join(vis[i]), end='')

        print('   score:',nums[score//1000],nums[(score%1000)//100],nums[((score%1000)%100)//10],nums[0])

      else:

        print(nums[i+1],x,''.join(vis[i]))

 

  else:

    print(' 🅨︎ 🅨︎ '+ (x+' ') * (l+1))

    for i in range(h):

      i+=1

      if i+1==h//3:

        print(nums[i//10]+nums[i%10],x,''.join(vis[i-1]),end='')

        print('   lives:', *lives)

      elif i+1==2*h//3:

        print(nums[i//10]+nums[i%10],x,''.join(vis[i-1]),end='')

        print('   score:', nums[score//1000],nums[(score%1000)//100],nums[((score%1000)%100)//10],nums[0])

      else:

        print(nums[i//10]+nums[i%10],x,''.join(vis[i-1]))
 

def check(x,y):

  global vis

  global lives

  z=0

  for i in range(y):

    for j in range(x):

      if board[i][j]=='💣':

        pass

      else:

        if board[i][j]!=vis[i][j]:

          z=1

          break

    if z:

      break

  if z==0:

    return [False,True]

  if '❤️ ' in lives:

    return [True,lives]

  else:

    return [False,False]

 

lives=['❤️ ','❤️ ','❤️ ']

score=0

 

start=time()

 

for i in range(3):
  i=1
  level_st=time()

  if i == 0:

    l=10

    h=8

    d=10

  elif i == 1:

    l=15

    h=11

    d=15

  else:

    l=20

    h=20

    d=20

  board=gen(d,l,h)

  board=numbers(l,h)

  vis=genvis(l,h)

  c=check(l,h)

  while c[0]:

    z=1

    lives=c[1]

    while z:

      os.system('cls')

      show()

      mode=input('reveal mode (r) or flag mode (f): ')

      if mode in 'frFR':

        try:

          reveal(mode.lower(),int(input('enter x coordinate (1-'+str(l)+'): '))-1,int(input('enter y coordinate (1-'+str(h)+'): '))-1)

          z=0

          c=check(l,h)

        except:pass

  if c[1]:

    os.system('cls')

    show()

    print(f'level {i+1} completed in a time of: {(time()-level_st)//60} minutes and {(time()-level_st)%60} seconds')

    s(3)

  if not c[1]:

    break

 

os.system('cls')

show()

s(1)

os.system('cls')

if check(l,h)[1]:

  show()

  print()

  print('VICTORY')

  print(f'you took a total time of {(time()-level_st)//60} minutes and {(time()-level_st)%60} to beat the game and got a score of {score}.')

else:

  for i in range(h):

    for j in range(l):

      if board[i][j]=='💣':

        vis[i][j]='💣'

  show()

  print()

  print('DEFEAT')

 