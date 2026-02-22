import pygame
dark=(150,255,150)
light=(100,255,100)
black=(0,0,0)
class game():
    def __init__(self):
        self.backboard = [[dark if (row + col) % 2 == 0 else light for col in range(8)] for row in range(8)]

        top_bottom=[[rook(i),knight(i),bishop(i),queen(i),king(i),bishop(i),knight(i),rook(i)] for i in range(2)]
        self.board = [top_bottom[1],[pawn(1) for i in range(8)]]

        for row in range(4):
            self.board.append([0 for col in range(8)])

        self.board.append([pawn(0) for i in range(8)])
        self.board.append(top_bottom[0])
        
        for i in range(8):
            for j in range(8):
                if self.board[i][j]!=0:
                    self.board[i][j].rect.center=(j*100+50,i*100+50)


class pawn(pygame.sprite.Sprite):
    def __init__(self, colour):
        super().__init__()
        self.image=pieces[colour][0]
        self.rect = self.image.get_rect()

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
    def __init__(self, colour):
        super().__init__()
        self.image=pieces[colour][5]
        self.rect = self.image.get_rect()

def show():
    for i in range(8):
        for j in range(8):
            pygame.draw.rect(screen,chess.backboard[i][j],(j*100,i*100 , 100, 100))

            if chess.board[i][j]!=0:
                screen.blit(chess.board[i][j].image,chess.board[i][j].rect)

IMG_DIR='Chess_game/Images/'
pieces_orig=[[pygame.image.load(f'{IMG_DIR}Piece{i}.{j}.png') for i in range(1,7)] for j in range(1,3)]
pieces=[[pygame.transform.scale(j,(80,85)) for j in i] for i in pieces_orig]


pygame.init()
chess=game()
screen=pygame.display.set_mode((800,800))

show()
pygame.display.flip()

pygame.time.wait(3000)
