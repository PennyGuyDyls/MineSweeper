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
        self.image = pygame.Surface((6,25))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (1000,800)
        self.state = 'LOADED'

    def shoot(self):
        self.rect.centery-=10
        self.state = 'FIRING'

    def follow(self, player):
        self.rect.center = (player.rect.centerx-3,player.rect.centery)

    def reload(self):
        self.state = 'LOADED'

class alien1(pygame.sprite.Sprite):
    def __init__(self,i,x):
        super().__init__()
        self.image = alien1_img_1
        self.rect = self.image.get_rect()
        self.rect.center = (i*120+60,x)
        self.state='ALIVE'
        self.stage=1

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

    def die(self):
        self.image=pygame.Surface((100,100),pygame.SRCALPHA)
        self.state='DEAD'

class alien2(pygame.sprite.Sprite):
    def __init__(self,i,x):
        super().__init__()
        self.image = alien2_img_1
        self.rect = self.image.get_rect()
        self.rect.center = (i*120+60,x)
        self.state='ALIVE'
        self.stage=1

    def animate(self):
        if self.state=='ALIVE':
            self.stage*=-1
            if self.stage == -1:
                self.image = alien2_img_1
                cen=self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center=cen
            else:
                self.image = alien2_img_2
                cen=self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center=cen          

    def die(self):
        self.image=pygame.Surface((100,100),pygame.SRCALPHA)
        self.state='DEAD'

def show(aliens,player,bullet):
    for i in aliens:  
        for j in range(len(i)):  
            screen.blit(i[j].image,i[j].rect)
    screen.blit(player.image,player.rect)
    screen.blit(bullet.image,bullet.rect)

def check(aliens):
    for i in reversed(aliens):
        for j in range(len(i)):
            if i[j].state=='ALIVE' and i[j].rect.centery>=800:
                return False
    return True

pygame.init()
screen=pygame.display.set_mode((1500,1000))
clock=pygame.time.Clock()
font=pygame.font.SysFont(None, 100)


alien1_img_1 = pygame.image.load("Alien 1 state 1.png").convert_alpha()
alien1_img_1 = pygame.transform.scale(alien1_img_1, (75,85))
alien1_img_2 = pygame.image.load("Alien 1 state 2.png").convert_alpha()
alien1_img_2 = pygame.transform.scale(alien1_img_2, (62,85))
alien2_img_1 = pygame.image.load("Alien 2 state 1.png").convert_alpha()
alien2_img_1 = pygame.transform.scale(alien2_img_1, (61,100))
alien2_img_2 = pygame.image.load("Alien 2 state 2.png").convert_alpha()
alien2_img_2 = pygame.transform.scale(alien2_img_2, (80,100))

cannon1 = pygame.image.load("Cannon_loaded.png").convert_alpha()
cannon1 = pygame.transform.scale(cannon1, (200,200))
cannon2 = pygame.image.load("Cannon_empty.png").convert_alpha()
cannon2 = pygame.transform.scale(cannon2, (200,200))



player=cannon()
direction=0

bullet=shot()

aliens1=[alien1(i,500) for i in range(10)]
aliens2=[alien1(i,400) for i in range(10)]
aliens3=[alien2(i,300) for i in range(10)]
aliens4=[alien2(i,200) for i in range(10)]
aliens=[aliens1,aliens2,aliens3,aliens4]
aldirection=(40,0)
down=False

animtime=pygame.time.get_ticks()
movtime=pygame.time.get_ticks()

running=True

while running and check(aliens):
    clock.tick(100)

    if pygame.time.get_ticks()-animtime>=300:
        for i in aliens:
            for j in range(len(aliens1)):
               i[j].animate()
            animtime=pygame.time.get_ticks()

    if pygame.time.get_ticks()-movtime>=500:
        left=aliens1[0].rect.centerx
        right=aliens1[-1].rect.centerx
        if down:
            down=False
            if left < 60:
                aldirection = (20,0)
            elif right > 1440:
                aldirection = (-20,0)
        else:
            if left<60 or right>1440:
                aldirection = (0,50  )
                down=True
        for i in aliens:
            for j in range(len(i)):
                i[j].rect.centerx+=aldirection[0]
                i[j].rect.centery+=aldirection[1]

        movtime=pygame.time.get_ticks()


    player.move(direction)
    if player.state == 'LOADED':
        bullet.follow(player)
    else:      
        bullet.shoot()

    for i in range(len(aliens)):
        for j in range(len(aliens1)):
            if bullet.rect.colliderect(aliens[i][j].rect) and aliens[i][j].state == 'ALIVE':
                aliens[i][j].die()
                player.reload()
                bullet.reload()
                break
        if bullet.rect.centery<0:
            player.reload()
            bullet.reload()


    screen.fill((0,0,0))
    show(aliens,player,bullet)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            break

        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                direction = 6
            elif event.key==pygame.K_LEFT:
                direction = -6
            elif event.key==pygame.K_SPACE and player.state == 'LOADED':
                bullet.follow(player)
                player.shoot()

        elif event.type==pygame.KEYUP:
            if event.key in (pygame.K_RIGHT,pygame.K_LEFT):
                direction = 0
