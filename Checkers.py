import pygame

dark=(150,255,150)
light=(100,255,100)
black=(0,0,0)
white=(255,255,255)
grey=(130,200,130)
class game():
    def __init__(self):
        self.backboard = [[dark if (row + col) % 2 == 0 else light for col in range(8)] for row in range(8)]
        self.board = [[piece(black,col,row) if (row + col) % 2 == 0 else 0 for col in range(8)] for row in range(3)]
        for row in range(2):
            self.board.append([0 for col in range(8)])
        for row in range(5,8):
            self.board.append([piece(white,col,row) if (row + col) % 2 == 0 else 0 for col in range(8)])
        self.turn=white
        self.action_piece=None
        self.piece_lock=False

    def select(self,row,col):
        if self.piece_lock and self.board[row][col]!=1:
            return None
        
        if self.board[row][col]==0:
            self.clear_grey()
        elif self.board[row][col]==1:
            self.board,check = self.action_piece.move(self.board,row,col)
            if check[0]:
                self.piece_lock=True
                for i in check[1]:
                    self.board[i[0]][i[1]]=1
            else:
                self.piece_lock=False
                self.swap_turn()

        elif self.board[row][col].colour==self.turn:
            moves = self.board[row][col].check_possible_moves(self.board)[0]
            self.action_piece=self.board[row][col]
            self.clear_grey()
            for i in moves:
                self.board[i[0]][i[1]]=1

    def clear_grey(self):
        for i in range(8):
                for j in range(8):
                    if self.board[i][j]==1:
                        self.board[i][j]=0

    def swap_turn(self):
        if self.turn==white:
            self.turn=black
        elif self.turn==black:
            self.turn=white


class piece(pygame.sprite.Sprite):
    def __init__(self,colour,x,y):
        super().__init__()
        self.colour=colour
        self.posx,self.posy=x,y
        self.image=self.image = pygame.Surface((70,70),pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = (x*100+50,y*100+50)
        pygame.draw.circle(self.image, self.colour, (35,35), 35)
        
        if self.colour == white:
            self.mod=-1
            self.oppcolour=black
        else:
            self.mod=1
            self.oppcolour=white



    def check_possible_moves(self,board):
        
        moves=[]
        jumps=[]
        if self.posx>0 and 0<=self.posy+self.mod<8 and board[self.posy+self.mod][self.posx-1] in [0,1]:
            moves.append([self.posy+self.mod,self.posx-1])
        elif self.posx>1 and 0<=self.posy+self.mod*2<8 and board[self.posy+self.mod*2][self.posx-2] in [0,1] and board[self.posy+self.mod][self.posx-1].colour==self.oppcolour:
            moves.append([self.posy+self.mod*2,self.posx-2])
            jumps.append([self.posy+self.mod*2,self.posx-2])
        if self.posx<7 and 0<=self.posy+self.mod<8 and board[self.posy+self.mod][self.posx+1] in [0,1]:
            moves.append([self.posy+self.mod,self.posx+1])
        elif self.posx<6 and 0<=self.posy+self.mod*2<8 and board[self.posy+self.mod*2][self.posx+2] in [0,1] and board[self.posy+self.mod][self.posx+1].colour==self.oppcolour:
            moves.append([self.posy+self.mod*2,self.posx+2])
            jumps.append([self.posy+self.mod*2,self.posx+2])


        return [moves,jumps]

    def move(self,board,row,col):
        jump=False
        if row-self.posy in [2,-2]:
            jump=True
            if col-self.posx==2:
                board[row-self.mod][col-1]=0
            else:
                board[row-self.mod][col+1]=0
        board[self.posy][self.posx]=0
        self.posx,self.posy=col,row
        self.rect.center = (self.posx*100+50,self.posy*100+50)
        board[self.posy][self.posx]=self
        for i in range(8):
            for j in range(8):
                if board[i][j]==1:
                    board[i][j]=0
        if jump:
            moves=self.check_possible_moves(board)[1]
            if moves != []:
                return board,[True,moves]
        return board,[False]

def show():
    for i in range(len(checkers.backboard)):
        for j in range(len(checkers.backboard[i])):
            pygame.draw.rect(screen,checkers.backboard[i][j],(j*100,i*100 , 100, 100))
            if checkers.board[i][j]==0:
                pass
            elif checkers.board[i][j]==1:
                pygame.draw.circle(screen,grey,(j*100+50,i*100+50),20)
            else:
                screen.blit(checkers.board[i][j].image,checkers.board[i][j].rect)




checkers=game()
pygame.init()
screen=pygame.display.set_mode((800,800))
show()
pygame.display.flip()
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx,my = pygame.mouse.get_pos()
            row,col=my//100,mx//100
            checkers.select(row,col)
            show()
            pygame.display.flip()
            