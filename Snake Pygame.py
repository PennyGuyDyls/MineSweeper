import pygame
from random import randint

def genboard(x,y):
    board=[[0 for i in range(x)] for j in range(y)]
    return board

def place_apple(board):
    indexes=[[i,j] for i in range(len(board)) for j in range(len(board[0])) if board[i][j]==0]
    if indexes != []:
        a=indexes[randint(0,len(indexes)-1)]
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
            board[snake[0][0]][snake[0][1]]=0
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


            

