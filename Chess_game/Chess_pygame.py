import pygame
dark=(150,255,150)
light=(100,255,100)
black=(0,0,0)
white=(255,255,255)
grey=(0,0,0,150)

class game():
    def __init__(self):
        self.backboard = [[dark if (row + col) % 2 == 0 else light for col in range(8)] for row in range(8)]

        top_bottom=[[rook(i),knight(i),bishop(i),queen(i),king(i,(7 if i else 0),4),bishop(i),knight(i),rook(i)] for i in range(2)]
        self.board = [top_bottom[1],[pawn(1,i,1) for i in range(8)]]

        for row in range(4):
            self.board.append([0 for col in range(8)])

        self.board.append([pawn(0,i,6) for i in range(8)])
        self.board.append(top_bottom[0])
        
        for i in range(8):
            for j in range(8):
                if self.board[i][j]!=0:
                    self.board[i][j].rect.center=(j*100+50,i*100+50)
        for i in self.board:
            print(i)
        self.dots=self.board[6][0].check_possible_moves(self.board)


class pawn(pygame.sprite.Sprite):
    def __init__(self, colour,x,y):
        super().__init__()
        self.colour=colour
        self.posx,self.posy=x,y
        self.image=pieces[colour][0]
        self.rect = self.image.get_rect()
        self.rect.center = (x*100+50,y*100+50)
        self.move2=True

        if self.colour == white:
            self.oppcolour=black
            self.mod=1
        else:
            self.oppcolour=white
            self.mod=-1

    def check_possible_moves(self,board):
        dots=[]
        if board[self.posy+self.mod][self.posx]==0:
            dots.append([self.posx,self.posy+self.mod])
            if self.move2 and board[self.posy+self.mod*2][self.posx]==0:
                dots.append([self.posx,self.posy+self.mod*2])

        if self.posx-1>=0 and board[self.posy+self.mod][self.posx-1]!=0 and board[self.posy+self.mod][self.posx-1].colour==self.oppcolour:
            dots.append([self.posx-1,self.posy+self.mod])
        if self.posx+1<8 and board[self.posy+self.mod][self.posx+1]!=0 and board[self.posy+self.mod][self.posx+1].colour==self.oppcolour:
            dots.append([self.posx+1,self.posy+self.mod])
        return dots

class knight(pygame.sprite.Sprite):
    def __init__(self, colour):
        super().__init__()
        self.image=pieces[colour][1]
        self.rect = self.image.get_rect()

class bishop(pygame.sprite.Sprite):
    def __init__(self, colour):
        super().__init__()
        self.image=pieces[colour][2]
        self.rect = self.image.get_rect()

class rook(pygame.sprite.Sprite):
    def __init__(self, colour):
        super().__init__()
        self.image=pieces[colour][3]
        self.rect = self.image.get_rect()

class queen(pygame.sprite.Sprite):
    def __init__(self, colour):
        super().__init__()
        self.image=pieces[colour][4]
        self.rect = self.image.get_rect()

class king(pygame.sprite.Sprite):
    def __init__(self, colour,x,y):
        super().__init__()
        self.colour=colour
        self.posx,self.posy=x,y
        self.image=pieces[colour][5]
        self.rect = self.image.get_rect()
        self.rect.center = (x*100+50,y*100+50)

        if self.colour == white:
            self.oppcolour=black
        else:
            self.oppcolour=white

    def check_possible_moves(self,board):
        dots=[]
        for i in range(-1,2):
            for j in range(-1,2):
                if 0<=self.posx+i<8 and 0<=self.posy+j<8:
                    if board[self.posy+j][self.posx+i] == 0 or (board[self.posy+j][self.posx+i].colour==self.oppcolour):
                        dots.append([self.posx+i,self.posy+j])
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


pygame.init()
chess=game()
screen=pygame.display.set_mode((800,800))


show()

pygame.display.flip()

pygame.time.wait(3000)
