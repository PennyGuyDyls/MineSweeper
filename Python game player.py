import pygame
from random import randint as ran

def menu():
    display = pygame.display.set_mode((1000,1000))

    connect4_orig = pygame.image.load("connect_4_display.png")
    connect4_img = pygame.transform.scale(connect4_orig, (150,150))
    minesweeper_orig = pygame.image.load("Mine_sweeper_display.png")
    minesweeper_img = pygame.transform.scale(minesweeper_orig, (150,150))
    snake_orig = pygame.image.load("Snake_display.png")
    snake_img = pygame.transform.scale(snake_orig, (150,150))
    games_orig = [connect4_orig,minesweeper_orig,snake_orig]
    games = [connect4_img, minesweeper_img, snake_img]
    base_locations=[[i*games[i].get_width()*4/3+games[i].get_width()*1/3, 50] for i in range(3)]
    locations=base_locations.copy()
    pygame.display.flip()
    while True:
        display.fill((0,0,0))
        for i in range(len(games)):
            display.blit(games[i], locations[i])
        pygame.display.flip()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return 'exit'

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx,my=pygame.mouse.get_pos()
                if locations[0][0]<=mx<=locations[0][0]+games[0].get_width() and locations[0][1]<=my<=locations[0][1]+games[0].get_height():
                    return 'connect4'
                elif locations[1][0]<=mx<=locations[1][0]+games[1].get_width() and locations[1][1]<=my<=locations[1][1]+games[1].get_height():
                    return 'minesweeper'
                elif locations[2][0]<=mx<=locations[2][0]+games[2].get_width() and locations[2][1]<=my<=locations[2][1]+games[2].get_height():
                    return 'snake'
                
            elif event.type == pygame.MOUSEMOTION:
                mx,my=pygame.mouse.get_pos()
                click=None
                if locations[0][0]<=mx<=locations[0][0]+games[0].get_width() and locations[0][1]<=my<=locations[0][1]+games[0].get_height():
                    click=0
                elif locations[1][0]<=mx<=locations[1][0]+games[1].get_width() and locations[1][1]<=my<=locations[1][1]+games[1].get_height():
                    click=1
                elif locations[2][0]<=mx<=locations[2][0]+games[2].get_width() and locations[2][1]<=my<=locations[2][1]+games[2].get_height():
                    click=2
                for i in range(len(games)):
                    if i == click:
                        games[i]=pygame.transform.scale(games_orig[i], (180,180))
                        display.blit(games[i], (500,500))
                        locations[i]=(base_locations[i][0]-15, 35)
                    else:
                        games[i]=pygame.transform.scale(games_orig[i], (150,150))
                        locations[i]=(base_locations[i])

                

def minesweeper():
    w=(255,255,255)
    g=(0,255,0)
    b=(0,0,255)
    r=(255,0,0)

    numcolours=[(200,200,200),(0,0,255),(0,128,0),(255,0,0),(0,0,128),(128,0,0),(0,128,128),(0,0,0),(128,128,128)]

    def gen(density,x,y):
        board=[[' ' for j in range(x)] for i in range(y)]
        indexes=[[i,j] for i in range(y) for j in range(x)]

        mines=x*y*density//100

        while mines>0:
            a=indexes[ran(0,len(indexes)-1)]
            board[a[0]][a[1]]=-1
            mines-=1
            indexes.remove(a)
        return board

    def numbers(board,x,y):
        for i in range(y):
            for j in range(x):
                if board[i][j]==-1:
                    pass
                else:
                    num=0
                    for k in range(-1,2):
                        for l in range(-1,2):
                            if 0<=i+k<y and 0<=j+l<x:
                                if board[i+k][j+l]==-1:
                                    num+=1
                    board[i][j]=num
        return board

    def genvis(board,x,y):
        vis=[[w for j in range(x)] for i in range(y)]

        for i in range(9):
            indexes=[[k,j] for j in range(x) for k in range(y) if board[k][j]==i]
            
            if indexes != []:
                break

        if indexes != []:
            a=indexes[ran(0,len(indexes)-1)]
            vis[a[0]][a[1]]=g
        return vis

    def time(set):
        global l
        mins=int((pygame.time.get_ticks()-set)/60000)
        if mins<10:
            mins='0'+str(mins)

        secs=int(((pygame.time.get_ticks()-set)/1000)%60)
        if secs<10:
            secs='0'+str(secs)

        return font.render(f'{mins}:{secs}', True, (w))

    def show(vis,lives,l):

        screen.blit(time(level_st), (l*40-100,10))

        for i in range(lives):
            screen.blit(heart_r, (i*60+10,3))
        for i in range(3-lives):
            screen.blit(heart_g, ((i+lives)*60+10,3))
        for i in range(len(vis)):
            for j in range(len(vis[i])):
                
                if vis[i][j] == -1 or vis[i][j] == -2:
                    pygame.draw.rect(screen, (200,200,200), (j*40+10,i*40+50,39,39))
                    screen.blit(explosion, (j*40,i*40+38))
                
                elif str(vis[i][j]) in "012345678":
                    pygame.draw.rect(screen, (200,200,200), (j*40+10,i*40+50,39,39))
                    text=font.render(str(vis[i][j]), True, (numcolours[vis[i][j]]))
                    screen.blit(text, (j*40+20,i*40+55))

                elif vis[i][j]=='f':
                    pygame.draw.rect(screen, (w), (j*40+10,i*40+50,39,39))
                    screen.blit(flag, (j*40+10,i*40+50))

                else:
                    pygame.draw.rect(screen, vis[i][j], (j*40+10,i*40+50,39,39))
        
    def reveal(board,vis,lives,m,x,y,l,h):
        if m == 'r':
            if vis[y][x] == w or vis[y][x] == g:
                vis[y][x]=board[y][x]

            if vis[y][x]==0:
                check=[]
                while True:
                    if vis==check:
                        break
            
                    check=[i.copy() for i in vis]
                    screen.fill((0,0,0))
                    show(vis,lives,l)
                    pygame.display.flip()
                    clock.tick(20)
                    for y1 in range(h):
                        for x1 in range(l):
                            if check[y1][x1]==0:
                                for i in range(-1,2):
                                    for j in range(-1,2):
                                        a=y1+j
                                        b=x1+i
                                        if 0<=b<l and 0<=a<h:
                                            vis[a][b]=board[a][b]
                        
            elif vis[y][x]==-1:
                vis[y][x]=-2
                lives-=1

        else:
            if vis[y][x]==w:
                vis[y][x]='f'
            elif vis[y][x]=='f':
                vis[y][x]=w

        return vis,lives

    def check(board,vis,x,y,lives):
        z=0
        for i in range(y):
            for j in range(x):
                if board[i][j]==-1:
                    pass
                else:
                    if board[i][j]!=vis[i][j]:
                        z=1
                    break
            if z:
                break
        if z==0:
            return [False,True]
        if lives>0:
            return [True,lives]
        else:
            return [False,False]
    
    lives=3
    total_time=0
    font = pygame.font.SysFont(None, 48)
    clock = pygame.time.Clock()
    q=False 

    for i in range(3):
        try:
            pygame.event.clear(pygame.MOUSEBUTTONDOWN)
            total_time+=int((pygame.time.get_ticks()-level_st)//1000)
        except:pass
        if i == 0:
            l=10
            h=10
            d=11
        elif i == 1:
            l=15
            h=11
            d=15
        else:
            l=20
            h=20
            d=20

        screen = pygame.display.set_mode((l*40+20,h*40+60))

        screen.fill((0,0,0))
        text=font.render(f'Level {i+1}', True, (255,255,255))
        screen.blit(text, (l*20+10-text.get_width()//2,h*20+30-text.get_height()//2))
        pygame.display.flip()
        pygame.time.wait(3000)

        flag = pygame.image.load("flag.png").convert_alpha()
        flag = pygame.transform.scale(flag, (40,40))
        explosion = pygame.image.load("explosion.png").convert_alpha()
        explosion = pygame.transform.scale(explosion, (60,60))
        heart_r= pygame.image.load("heart_r.png").convert_alpha()
        heart_r = pygame.transform.scale(heart_r, (43,43))
        heart_g= pygame.image.load("heart_g.png").convert_alpha()
        heart_g = pygame.transform.scale(heart_g, (43,43))

        board=gen(d,l,h)
        board=numbers(board,l,h)
        vis=genvis(board,l,h)
        c=check(board,vis,l,h,lives)

        level_st=pygame.time.get_ticks()

        
        while c[0]:
            screen.fill((0,0,0))
            show(vis,lives,l)
            pygame.display.flip()
            z=1
            lives=c[1]
            for event in pygame.event.get():
            
                if event.type == pygame.QUIT:
                    c=[False,False]
                    q=True
                    break

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx,my=pygame.mouse.get_pos()
                    mx=(mx-10)//40
                    my=(my-50)//40
                    if 0<=mx<l and 0<=my<h:
                        if event.button == 1:
                            m='r'
                        else:
                            m='f'
                    vis,lives=reveal(board,vis,lives,m,mx,my,l,h)
                    c=check(board,vis,l,h,lives)
        if not c[1]:
            break


    if not q:
        screen.fill((0,0,0))
        show(vis,lives,l)
        pygame.display.flip()
        pygame.time.wait(3000)

        total_time+=int((pygame.time.get_ticks()-level_st)//1000)

        if check(board,vis,l,h,lives)[1]:
            screen.fill((0,0,0))
            text=font.render(f'Victory!', True, (0,255,0))
            screen.blit(text, (l*20+10-text.get_width()//2,h*20+30-text.get_height()//2))

        else:
            screen.fill((0,0,0))
            text=font.render(f'Defeat!', True, (255,0,0))
            screen.blit(text, (l*20+10-text.get_width()//2,h*20+30-text.get_height()//2))
        pygame.display.flip()
        pygame.time.wait(2000)
        text=font.render(f'In {total_time//60} minutes {int(total_time%60)} seconds', True, (255,255,255))
        screen.blit(text, (l*20+10-text.get_width()//2,h*20+text.get_height()//2+40))
        pygame.display.flip()
        pygame.time.wait(3000)

def connect4():
    w=(30,30,30)
    r=(255,20,20)
    b=(0,150,255)

    def swap(t):
        if t==r:
            t=b
        else:
            t=r
        return t

    def show(board):
        for i in range(8):
            pygame.draw.rect(screen, (220,220,220), (i*120+58, 40, 4, 750))
        for i in range(1,8):
            for j in range(1,7):
                pygame.draw.circle(screen, board[j-1][i-1], (i*120, j*120),40)

    def hover(t,mx):
        column = (mx+60)//120
        if 1<=column<=7:
            pycol=(column)*120
            screen.fill((0,0,0))
            show(board)
            pygame.draw.circle(screen, t, (pycol, 1),40)
            pygame.display.flip()

    def move(t,board,column):
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
                show(board)
                pygame.draw.circle(screen, w, (pycol, pyrow),40)
                pygame.draw.circle(screen, t, (pycol, i),40)
                pygame.display.flip()
                clock.tick(500)
            return True
    
        print("Column full!")
        return False

    def check_h(board):
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

    def check_v(board):

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

    def check_dr(board):
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

    def check_dl(board):
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
    q=False
    while running and not (h[0] or v[0] or d1[0] or d2[0]):
        h=check_h(board)
        v=check_v(board)
        d1=check_dr(board)
        d2=check_dl(board)
        show(board)
        pygame.display.flip()
        for event in pygame.event.get():
                
            if event.type == pygame.QUIT:
                running=0
                q=True
                break
                
            if event.type == pygame.MOUSEBUTTONDOWN:         
                mx, my = pygame.mouse.get_pos()
                if move(t,board,(mx+60)//120-1):
                    t=swap(t)
                pygame.event.clear(pygame.MOUSEBUTTONDOWN)

            if event.type == pygame.MOUSEMOTION:
                mx, my = pygame.mouse.get_pos()
                hover(t,mx)

    if not q:
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

def snake():

    def genboard(x,y):
        board=[[0 for i in range(x)] for j in range(y)]
        return board

    def place_apple(board):
        indexes=[[i,j] for i in range(len(board)) for j in range(len(board[0])) if board[i][j]==0]
        if indexes != []:
            a=indexes[ran(0,len(indexes)-1)]
            board[a[0]][a[1]]=1
        return board

    def show(board,cw,ch):
        screen.fill((0,0,0))
        colour=(150,255,150)
        swap=True
        for i in range(len(board)):
            if len(board[i]) % 2 == 0:
                swap=False
            for j in range(len(board[i])):
                if swap:
                    if colour==(150,255,150):
                        colour=(100,255,100)
                    else:
                        colour=(150,255,150)
                swap=True
                
                pygame.draw.rect(screen,colour,(j*cw,i*ch,cw,ch))

                if board[i][j]==1:
                    screen.blit(apple,((j+0.1)*cw,(i+0.1)*ch))

                if board[i][j]==2:
                    pygame.draw.rect(screen,(255,0,0),((j+0.1)*cw,(i+0.1)*ch,cw*0.8,ch*0.8))
                    for k in range(1,len(snake)):
                        if snake[k][0]>snake[k-1][0]:
                            pygame.draw.rect(screen,(255,0,0),((snake[k][1]+0.1)*cw,(snake[k][0]-0.3)*ch,cw*0.8,ch))
                        elif snake[k][0]<snake[k-1][0]:
                            pygame.draw.rect(screen,(255,0,0),((snake[k][1]+0.1)*cw,(snake[k][0]+0.3)*ch,cw*0.8,ch))
                        elif snake[k][1]>snake[k-1][1]:
                            pygame.draw.rect(screen,(255,0,0),((snake[k][1]-0.3)*cw,(snake[k][0]+0.1)*ch,cw,ch*0.8))
                        else:
                            pygame.draw.rect(screen,(255,0,0),((snake[k][1]+0.3)*cw,(snake[k][0]+0.1)*ch,cw,ch*0.8))
                        
    def move(board, snake, direction):
        head=snake[-1]
        new_head=[head[0]+direction[0], head[1]+direction[1]]

        if new_head == snake[-2]:
            direction=(-direction[0], -direction[1])
            new_head=[head[0]+direction[0], head[1]+direction[1]]

        if new_head == snake[0]:
            snake.append(new_head)
            snake.pop(0)
            return True,board,snake
        
        if 0<=new_head[0]<len(board) and 0<=new_head[1]<len(board[0]) and board[new_head[0]][new_head[1]]!=2:
            snake.append(new_head)
            if board[new_head[0]][new_head[1]]==1:
                for i in snake:
                    board[i[0]][i[1]]=2
                place_apple(board)
            else:
                board[snake[0][0]][snake[0][1]]=0
                snake.pop(0)
            for i in snake:
                board[i[0]][i[1]]=2
            return True,board,snake
        return False,None,None

    width=10
    height=10
    cell_w=100
    cell_h=100
    pygame.init()

    screen=pygame.display.set_mode((width*cell_w,height*cell_h))
    apple=pygame.image.load('apple.png').convert_alpha()
    apple=pygame.transform.scale(apple,(cell_w*0.8,cell_h*0.8))
    clock=pygame.time.Clock()

    lost=True
    running=True
    while running:
        clock.tick(7)

        if lost:

            direction=(0,1)
            start=True
            font=pygame.font.SysFont(None, 100)

            board=genboard(width,height)
            board=place_apple(board)

            snake=[[5,i] for i in range(1,4)]

            for i in range(3,0,-1):
                screen.fill((0,0,0))
                text = font.render(f"Starting in {i}", True, (255,255,255))
                screen.blit(text, (width*cell_w//2-text.get_width()//2,height*cell_h//2-text.get_height()//2))
                pygame.display.flip()
                pygame.time.wait(1000)

            lost=False

        
        
        for event in pygame.event.get():

            if event.type==pygame.QUIT:
                running=False
            
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    direction=(0,1)
                elif event.key==pygame.K_LEFT:
                    direction=(0,-1)
                elif event.key==pygame.K_UP:
                    direction=(-1,0)
                elif event.key==pygame.K_DOWN:
                    direction=(1,0)

        running,board,snake=move(board, snake, direction)
        if running:
            show(board,cell_w,cell_h)
            pygame.display.flip()
        else:
            lost=True
            screen.fill((0,0,0))
            text = font.render("Game Over", True, (255,0,0))
            screen.blit(text, (width*cell_w//2-text.get_width()//2,height*cell_h//2-text.get_height()//2))
            pygame.display.flip()
            pygame.time.wait(2000)
            font=pygame.font.SysFont(None, 40)
            pygame.draw.rect(screen,(0,255,0),(width*cell_w//4-150,height*cell_h//4*3-50,300,100))
            text = font.render("Play Again", True, (0,0,0))
            screen.blit(text, (width*cell_w//4-text.get_width()//2,height*cell_h//4*3-text.get_height()//2))
            pygame.draw.rect(screen,(255,0,0),(width*cell_w//4*3-150,height*cell_h//4*3-50,300,100))
            text = font.render("Exit", True, (0,0,0))
            screen.blit(text, (width*cell_w//4*3-text.get_width()//2,height*cell_h//4*3-text.get_height()//2))
            pygame.display.flip()
            waiting=True
            while waiting:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        waiting=False
                        running=False

                    elif event.type==pygame.MOUSEBUTTONDOWN:
                        mx, my = pygame.mouse.get_pos()
                        if width*cell_w//4-150<=mx<=width*cell_w//4+150 and height*cell_h//4*3-50<=my<=height*cell_h//4*3+50:
                            running=True
                            waiting=False
                        elif width*cell_w//4*3-150<=mx<=width*cell_w//4*3+150 and height*cell_h//4*3-50<=my<=height*cell_h//4*3+50:
                            running=False
                            waiting=False


pygame.init()

play=True
while play:
    game=menu()

    if game=='connect4':
        connect4()
    elif game=='minesweeper':
        minesweeper()
    elif game=='snake':
        snake()
    elif game=='exit':
        play=False