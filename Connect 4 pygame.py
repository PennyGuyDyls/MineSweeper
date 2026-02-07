import pygame

w=(30,30,30)
r=(255,20,20)
b=(0,150,255)

def swap(t):
  if t==r:
    t=b
  else:
    t=r
  return t

def show():
  global board
  for i in range(8):
      pygame.draw.rect(screen, (220,220,220), (i*120+58, 40, 4, 750))
  for i in range(1,8):
      for j in range(1,7):
        pygame.draw.circle(screen, board[j-1][i-1], (i*120, j*120),40)

def hover():
  global t
  global mx
  column = (mx+60)//120
  if 1<=column<=7:
    pycol=(column)*120
    screen.fill((0,0,0))
    show()
    pygame.draw.circle(screen, t, (pycol, 1),40)
    pygame.display.flip()

def move(column):
  global t
  global board
  global screen
  z=0
  if 0<=column<=6:
    pycol=(column+1)*120
    count=7
    for i in reversed(board):
      count-=1
      if i[column] == w:
        pyrow=(count)*120
        i[column]=t
        z=1
        break
          
  if z:
    for i in range(pyrow+1):
      screen.fill((0,0,0))
      show()
      pygame.draw.circle(screen, w, (pycol, pyrow),40)
      pygame.draw.circle(screen, t, (pycol, i),40)
      pygame.display.flip()
      clock.tick(500)
    return True
  
  print("Column full!")
  return False

def check_h():
  global board
  x=0
  y=0
  ry=0
  for i in board:
    rx=0
    ry+=1
    x=0
    y=0
    for j in i:
      rx+=1
      if j==r:
        y=0
        x+=1
      elif j==b:
        x=0
        y+=1
      else:
        x=0
        y=0
      if x==4:
        return [True,'Red',r,rx,ry]
      elif y==4:
        return [True,'Blue',b,rx,ry]
  return [False]

def check_v():
  global board

  for i in range(7):
    x=0
    y=0
    ry=0
    for j in board:
      ry+=1
      if j[i]==r:
        y=0
        x+=1
      elif j[i]==b:
        x=0
        y+=1
      else:
        x=0
        y=0
      if x==4:
        return [True,'Red',r,i+1,ry]
      elif y==4:
        return [True,'Blue',b,i+1,ry]
  return [False]

def check_dr():
  global board
  x=0
  y=0
  z=0
  for i in range(-7,7):
    x=0
    y=0
    for j in range(6):
      if 0<=j+i<=6:
        if board[j][j+i] == r:
          x+=1
          y=0
        elif board[j][j+i] == b:
          x=0
          y+=1
        else:
          x=0
          y=0
        if x==4:
          return [True,'Red',r,j+i+1,j+1]
        elif y==4:
          return [True,'Blue',b,j+i+1,j+1]
  return [False]

def check_dl():
  global board
  x=0
  y=0
  z=0
  for i in range(-7,7):
    x=0
    y=0
    for j in range(6):
      if 0<=7-i-j<=6:
        if board[j][7-i-j] == r:
          x+=1
          y=0
        elif board[j][7-i-j] == b:
          x=0
          y+=1
        else:
          x=0
          y=0
        if x==4:
          return [True,'Red',r,8-i-j,j+1]
        elif y==4:
          return [True,'Blue',b,8-i-j,j+1]
  return [False]

pygame.init()

screen = pygame.display.set_mode((975,850))
font = pygame.font.SysFont(None, 48)
clock = pygame.time.Clock()

board = [
    [w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w]
    ]

t=r
h=[0]
v=[0]
d1=[0]
d2=[0]


running = 1
while running and not (h[0] or v[0] or d1[0] or d2[0]):
  h=check_h()
  v=check_v()
  d1=check_dr()
  d2=check_dl()
  show()
  pygame.display.flip()
  for event in pygame.event.get():
          
    if event.type == pygame.QUIT:
      running=0
      break
          
    if event.type == pygame.MOUSEBUTTONDOWN:         
      mx, my = pygame.mouse.get_pos()
      if move((mx+60)//120-1):
        t=swap(t)

        pygame.event.clear(pygame.MOUSEBUTTONDOWN)
    if event.type == pygame.MOUSEMOTION:
      mx, my = pygame.mouse.get_pos()
      hover()


if h[0]:
    text= font.render((h[1]+" wins!"), True, h[2])
    screen.blit(text, (400, 400))
    startx,starty=(h[3]*120+50, h[4]*120)
    endx,endy=(startx-460, starty)
    pygame.draw.line(screen, h[2], (startx, starty), (endx, endy), 10)

elif v[0]:
    text= font.render((v[1]+" wins!"), True, v[2])
    screen.blit(text, (400, 400))
    startx,starty=(v[3]*120, v[4]*120+50)
    endx,endy=(startx, starty-460)
    pygame.draw.line(screen, v[2], (startx, starty), (endx, endy), 10)

elif d1[0]:
    text= font.render((d1[1]+" wins!"), True, d1[2])
    screen.blit(text, (400, 400))
    startx,starty=(d1[3]*120+50, d1[4]*120+50)
    endx,endy=(startx-460, starty-460)
    pygame.draw.line(screen, d1[2], (startx, starty), (endx, endy), 10)

elif d2[0]:
    text= font.render((d2[1]+" wins!"), True, d2[2])
    screen.blit(text, (400, 400))
    startx,starty=(d2[3]*120-50, d2[4]*120+50)
    endx,endy=(startx+460, starty-460)
    pygame.draw.line(screen, d2[2], (startx, starty), (endx, endy), 10)

pygame.display.flip()
pygame.time.wait(5000)


            


