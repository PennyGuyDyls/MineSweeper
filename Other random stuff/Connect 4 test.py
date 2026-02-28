import os
from pynput.mouse import Listener
from time import sleep as s


def on_click(x, y, button, pressed):
    global mx
    global my
    global click
    if pressed:
        click=1
        mx = x
        my = y


 

def show():

  print('|'.join(['1️⃣ ','2️⃣ ','3️⃣ ','4️⃣ ','5️⃣ ','6️⃣ ','7️⃣ ']))

  x='▪️ |'

  print(x*6+'▪️')

  for i in board:

    print('|'.join(i))

 

def swap(t):

  if t=='🔴':

    t='🔵'

  else:

    t='🔴'

  return t

 

def move():

  global board
  global mx
  global click
  global t

  while not click:
    s(0.01)
  if 440<=mx<=640:
    mx%=440
    print(mx)
    count=0
    for i in range(-5,205,30):
      count+=1
      if i<=mx<i+30:
        column=count
        break

    for i in reversed(board):
        if i[column-1] == '⚪':
          i[column-1]=t
          break

  click=0
 

def check_h():

  global board

  x=0

  y=0

  z=False

  for i in board:

    if x == 4 or y == 4:

      break

    x=0

    y=0

    for j in i:

      if j=='🔴':

        y=0

        x+=1

      elif j=='🔵':

        x=0

        y+=1

      else:

        x=0

        y=0

      if x==4 or y==4:

        z=True

        break

  if x==4:

    return [z,'red']

  elif y==4:

    return [z,'blue']

  else:

    return [z]

 

def check_v():

  global board

  x=0

  y=0

  z=False

  for i in range(7):

    if x == 4 or y == 4:

      z=True

      break

    x=0

    y=0

    for j in board:

      if j[i]=='🔴':

        y=0

        x+=1

      elif j[i]=='🔵':

        x=0

        y+=1

      else:

        x=0

        y=0

      if x==4 or y==4:

        break

  if x==4:

    return [z,'red']

  elif y==4:

    return [z,'blue']

  else:

    return [z]

       

def check_dr():

  global board

  x=0

  y=0

  z=0

  for i in range(-7,7):

    if x == 4 or y == 4:

      z=True

      break

    x=0

    y=0

    for j in range(7):

      if 0<=j+i<=6:

        try:

          if board[j][j+i] == '🔴':

            x+=1

            y=0

          elif board[j][j+i] == '🔵':

            x=0

            y+=1

          else:

            x=0

            y=0

          if x==4 or y==4:

            z=True

            break

        except: pass

  if x==4:

    return [z,'red']

  elif y==4:

    return [z,'blue']

  else:

    return [z]

 

def check_dl():

  global board

  x=0

  y=0

  z=0

  for i in range(-7,7):

    if x == 4 or y == 4:

      z=True

      break

    x=0

    y=0  

    for j in range(7):

      if 0<=j+i<=6:

        try:

          if board[j][i-j] == '🔴':

            x+=1

            y=0

          elif board[j][i-j] == '🔵':

            x=0

            y+=1

          else:

            x=0

            y=0

          if x==4 or y==4:

            z=True

            break

        except: pass

  if x==4:

    return [z,'red']

  elif y==4:

    return [z,'blue']

  else:

    return [z]

listener = Listener(on_click=on_click)
listener.start()

mx=0
my=0
click=0
t='🔴'

board=[['⚪','⚪','⚪','⚪','⚪','⚪','⚪'],

 ['⚪','⚪','⚪','⚪','⚪','⚪','⚪'],

 ['⚪','⚪','⚪','⚪','⚪','⚪','⚪'],

 ['⚪','⚪','⚪','⚪','⚪','⚪','⚪'],

 ['⚪','⚪','⚪','⚪','⚪','⚪','⚪'],

 ['⚪','⚪','⚪','⚪','⚪','⚪','⚪'],

 ['⚪','⚪','⚪','⚪','⚪','⚪','⚪']]

h=[0]

v=[0]

d1=[0]

d2=[0]

while not(h[0] or v[0] or d1[0] or d2[0]):

  t=swap(t)

  os.system('cls')

  show()

  move()

  h=check_h()

  v=check_v()

  d1=check_dr()

  d2=check_dl()

os.system('cls')

show()

if h[0]:

  print(h[1],'wins!')

elif v[0]:

  print(v[1], 'wins!')

elif d1[0]:

  print(d1[1], 'wins!')

elif d2[0]:

  print(d2[1], 'wins!')