import pygame
dark=(150,255,150)
light=(100,255,100)
black=(0,0,0)
white=(255,255,255)
grey=(0,0,0,150)

class game():
    def __init__(self):
        self.backboard = [[dark if (row + col) % 2 == 0 else light for col in range(8)] for row in range(8)]

        top_bottom=[[rook(i),
                     knight(i,1,(0 if i else 7)),
                     bishop(i),
                     queen(i),
                     king(i,4,(0 if i else 7)),
                     bishop(i),
                     knight(i,6,(0 if i else 7)),
                     rook(i)]
                       for i in range(2)]
        self.board = [top_bottom[1],[pawn(1,i,1) for i in range(8)]]

        for row in range(4):
            self.board.append([0 for col in range(8)])

        self.board.append([pawn(0,i,6) for i in range(8)])
        self.board.append(top_bottom[0])
        
        for i in range(8):
            for j in range(8):
                if self.board[i][j]!=0:
                    self.board[i][j].rect.center=(j*100+50,i*100+50)

        self.dots=[]
        self.action_piece=None

    def select(self,row,col):
        if [col,row] in self.dots:
            self.board=self.action_piece.move(self.board,row,col)
            self.dots=[]
        elif self.board[row][col] == 0:
            self.dots=[]
        elif isinstance(self.board[row][col],Piece):
            self.action_piece=self.board[row][col]
            self.dots=self.board[row][col].check_possible_moves(self.board)


class Piece(pygame.sprite.Sprite):

    def check_valid_location(self,board,x,y,piece):
        if not (0<=x<8 and 0<=y<8):
            return False
        
        if board[y][x]==0:
            if piece=='PAWN':
                return False
            return True
        
        if isinstance(board[y][x],Piece) and board[y][x].colour==self.oppcolour:
            return True

    def move(self,board,y,x):
        self.move2=False
        board[self.posy][self.posx]=0
        self.posx,self.posy=x,y
        self.rect.center = (x*100+50,y*100+50)
        board[y][x]=self
        return board
    


class pawn(Piece):
    def __init__(self, colour,x,y):
        super().__init__()
        self.colour=colour
        self.posx,self.posy=x,y
        self.image=pieces[colour][0]
        self.rect = self.image.get_rect()
        self.rect.center = (x*100+50,y*100+50)
        self.move2=True

        if self.colour == 1:
            self.oppcolour=0
            self.mod=1
        else:
            self.oppcolour=1
            self.mod=-1

    def check_possible_moves(self,board):
        dots=[]
        newx=self.posx
        newy=self.posy+self.mod
        if board[newy][newx]==0:
            dots.append([self.posx,self.posy+self.mod])
            newy+=self.mod
            if self.move2 and board[newy][newx]==0:
                dots.append([newx,newy])

        newx=self.posx-1
        newy=self.posy+self.mod
        if self.check_valid_location(board,newx,newy,'PAWN'):
            dots.append([newx,newy])
        newx=self.posx+1
        if self.check_valid_location(board,newx,newy,'PAWN'):
            dots.append([newx,newy])
        return dots
    
        

class knight(Piece):
    def __init__(self, colour,x,y):
        super().__init__()
        self.colour=colour
        self.posx,self.posy=x,y
        self.image=pieces[colour][1]
        self.rect = self.image.get_rect()
        self.rect.center = (x*100+50,y*100+50)

        if self.colour == 1:
            self.oppcolour=0
        else:
            self.oppcolour=1

    def check_possible_moves(self,board):
        dots=[]
        mods=[[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1]]
        for i in mods:
            newx=self.posx+i[0]
            newy=self.posy+i[1]
            if self.check_valid_location(board,newx,newy,'KNIGHT'):
                dots.append([newx,newy])
        return dots
    
class bishop(Piece):
    def __init__(self, colour):
        super().__init__()
        self.colour=colour
        self.image=pieces[colour][2]
        self.rect = self.image.get_rect()

class rook(Piece):
    def __init__(self, colour):
        super().__init__()
        self.colour=colour
        self.image=pieces[colour][3]
        self.rect = self.image.get_rect()

class queen(Piece):
    def __init__(self, colour):
        super().__init__()
        self.colour=colour
        self.image=pieces[colour][4]
        self.rect = self.image.get_rect()

class king(Piece):
    def __init__(self, colour,x,y):
        super().__init__()
        self.colour=colour
        self.posx,self.posy=x,y
        self.image=pieces[colour][5]
        self.rect = self.image.get_rect()
        self.rect.center = (x*100+50,y*100+50)

        if self.colour == 1:
            self.oppcolour=0
        else:
            self.oppcolour=1

    def check_possible_moves(self,board):
        dots=[]
        for i in range(-1,2):
            for j in range(-1,2):
                newx=self.posx+i
                newy=self.posy+j
                if self.check_valid_location(board,newx,newy):
                    dots.append([newx,newy])
        return dots
        

def show():
    for i in range(8):
        for j in range(8):
            pygame.draw.rect(screen,chess.backboard[i][j],(j*100,i*100 , 100, 100))

            if chess.board[i][j]==0:
                pass
            else:
                screen.blit(chess.board[i][j].image,chess.board[i][j].rect)

    for i in chess.dots:
        draw_dot(i[0],i[1])


def draw_dot(x,y):
    surf = pygame.Surface((100, 100), pygame.SRCALPHA)
    pygame.draw.circle(surf, (grey), (50,50), 20)
    screen.blit(surf, (x*100,y*100))

IMG_DIR='Chess_game/Images/'
pieces_orig=[[pygame.image.load(f'{IMG_DIR}Piece{i}.{j}.png') for i in range(1,7)] for j in range(1,3)]
pieces=[[pygame.transform.scale(j,(80,85)) for j in i] for i in pieces_orig]
for i in range(2):
    pieces[i][0]=pygame.transform.scale(pieces_orig[i][0],(60,70))

pygame.init()
chess=game()
screen=pygame.display.set_mode((800,800))




running=True
while running:
    show()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx,my = pygame.mouse.get_pos()
            row,col=my//100,mx//100
            chess.select(row,col)
            
