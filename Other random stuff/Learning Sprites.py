import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (300, 300)

    def update(self):
        self.rect.centerx+=1

pygame.init()
screen=pygame.display.set_mode((1000,1000))
clock=pygame.time.Clock()
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
while True:
    screen.fill((0,0,0))
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(14)

