import pygame

class Paddle1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((8,200))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (100, 300)

    def update(self,d):
        if 100<self.rect.centery+d<900:
            self.rect.centery+=d

class Paddle2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((8,200))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (1400, 300)

    def update(self,d):
        if 100<self.rect.centery+d<900:
            self.rect.centery+=d

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50,50),pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (25,25), 25)
        self.rect = self.image.get_rect()
        self.rect.center = (750,500)

    def update(self,ang,speed):
        
        self.rect.centerx+=(10-ang)*speed
        self.rect.centery+=ang*speed

pygame.init()
screen=pygame.display.set_mode((1500,1000))
clock=pygame.time.Clock()
padSpr1=Paddle1()
paddle1 = pygame.sprite.Group()
paddle1.add(padSpr1)
padSpr2=Paddle2()
paddle2 = pygame.sprite.Group()
paddle2.add(padSpr2)
ballspr=Ball()
ball = pygame.sprite.Group()
ball.add(ballspr)
direction1,direction2 = 0,0
angle=0
speed=-1
running=True
while running:
    clock.tick(15)

    screen.fill((0,0,0))
    paddle1.update(direction1*-10)
    paddle1.draw(screen)
    paddle2.update(direction2*-10)
    paddle2.draw(screen)

    if 25>ballspr.rect.centery:
        angle*=-1
    elif ballspr.rect.centery>975:
        angle*=-1

    ball.update(angle,speed)
    ball.draw(screen)
    pygame.display.flip()

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            running=False

        elif event.type==pygame.KEYDOWN:
            if event.key == pygame.K_w:
                direction1=1
            elif event.key == pygame.K_s:
                direction1=-1
            elif event.key == pygame.K_UP:
                direction2=1
            elif event.key == pygame.K_DOWN:
                direction2=-1

        elif event.type==pygame.KEYUP:
            if event.key in (pygame.K_w,pygame.K_s):
                direction1=0
            elif event.key in (pygame.K_UP,pygame.K_DOWN):
                direction2=0

    if pygame.sprite.collide_rect(ballspr,padSpr1) or pygame.sprite.collide_rect(ballspr,padSpr2):
        if speed>0:
            speed+=0.1
        else:
            speed-=0.1
        speed*=-1

        angle=(ballspr.rect.centery - padSpr1.rect.centery)//11

            
            
            
            