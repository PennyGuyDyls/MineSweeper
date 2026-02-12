import pygame

class cannon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = cannon1
        self.rect = self.image.get_rect()
        self.rect.center = (1400,800)
        self.state = 'LOADED'

    def move(self,direction):
        self.rect.centerx+=direction

    def shoot(self):
        self.state = 'EMPTY'
        self.image = cannon2

    def reload(self):
        self.image = cannon1
        self.state = 'LOADED'

class shot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((8,30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (1000,800)
        self.state = 'LOADED'

    def shoot(self):
        self.rect.centery-=5
        self.state = 'FIRING'

    def follow(self, player):
        self.rect.center = (player.rect.centerx-3,player.rect.centery)

    def reload(self):
        self.state = 'LOADED'


class alien1(pygame.sprite.Sprite):
    def __init__(self,i):
        super().__init__()
        self.image = alien1_img_1
        self.rect = self.image.get_rect()
        self.rect.center = (i*120+60,300)
        self.state='ALIVE'
        self.stage=1
        self.direction=(40,0)
        self.moved=True

    def animate(self):
        if self.state=='ALIVE':
            self.stage*=-1
            if self.stage == -1:
                self.image = alien1_img_1
                cen=self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center=cen
            else:
                self.image = alien1_img_2
                cen=self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center=cen

    def move(self,aliens1):
        print(aliens1[-1].rect.centerx,aliens1[0].rect.centerx)
        if (aliens1[-1].rect.centerx>=1450 or aliens1[0].rect.centerx<=50) and self.direction!=(0,100):
            self.direction = (0,100)
        elif aliens1[-1].rect.centerx>=1450:
            self.direction = (-40,0)
        elif aliens1[0].rect.centerx<=50:
            self.direction = (40,0)
        self.rect.centerx+=self.direction[0]
        self.rect.centery+=self.direction[1]

            

    def die(self):
        self.image=pygame.Surface((100,100),pygame.SRCALPHA)
        self.state='DEAD'



def show(aliens1,player,bullet):
    for i in range(len(aliens1)):  
        screen.blit(aliens1[i].image,aliens1[i].rect)
    screen.blit(player.image,player.rect)
    screen.blit(bullet.image,bullet.rect)

pygame.init()
screen=pygame.display.set_mode((1500,1000))
clock=pygame.time.Clock()
font=pygame.font.SysFont(None, 100)


alien1_img_1 = pygame.image.load("Alien 1 state 1.png").convert_alpha()
alien1_img_1 = pygame.transform.scale(alien1_img_1, (85,95))
alien1_img_2 = pygame.image.load("Alien 1 state 2.png").convert_alpha()
alien1_img_2 = pygame.transform.scale(alien1_img_2, (73,96))

cannon1 = pygame.image.load("Cannon_loaded.png").convert_alpha()
cannon1 = pygame.transform.scale(cannon1, (200,200))
cannon2 = pygame.image.load("Cannon_empty.png").convert_alpha()
cannon2 = pygame.transform.scale(cannon2, (200,200))


player=cannon()
bullet=shot()
aliens1=[alien1(i) for i in range(10)]

animtime=pygame.time.get_ticks()
movtime=pygame.time.get_ticks()
direction=0
running=True

while running:
    clock.tick(50)

    if pygame.time.get_ticks()-animtime>=1000:
        for i in range(len(aliens1)):
            aliens1[i].animate()
        animtime=pygame.time.get_ticks()

    if pygame.time.get_ticks()-movtime>=5500:
        for i in range(len(aliens1)):
            aliens1[i].move(aliens1)
        movtime=pygame.time.get_ticks()


    player.move(direction)
    if player.state == 'LOADED':
        bullet.follow(player)
    else:      
        bullet.shoot()

    
    for i in range(len(aliens1)):
        if bullet.rect.colliderect(aliens1[i].rect) and aliens1[i].state == 'ALIVE':
            aliens1[i].die()
            player.reload()
            bullet.reload()
            break
    if bullet.rect.centery<0:
        player.reload()
        bullet.reload()


    screen.fill((0,0,0))
    show(aliens1,player,bullet)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            break

        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                direction = 4
            elif event.key==pygame.K_LEFT:
                direction = -4
            elif event.key==pygame.K_SPACE and player.state == 'LOADED':
                bullet.follow(player)
                player.shoot()
        elif event.type==pygame.KEYUP:
            if event.key in (pygame.K_RIGHT,pygame.K_LEFT):
                direction = 0
            