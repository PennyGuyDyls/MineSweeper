import pygame


def menu():
    display = pygame.display.set_mode((1000,1000))

    IMG_DIR='Arcade/display_Images/'
    connect4_orig = pygame.image.load(IMG_DIR+"connect_4_display.png")
    connect4_img = pygame.transform.scale(connect4_orig, (150,150))
    minesweeper_orig = pygame.image.load(IMG_DIR+"Mine_sweeper_display.png")
    minesweeper_img = pygame.transform.scale(minesweeper_orig, (150,150))
    snake_orig = pygame.image.load(IMG_DIR+"Snake_display.png")
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

            


pygame.init()

play=True
while play:
    game=menu()

    if game=='connect4':
        from Connect_4.Connect_4_pygame import run
        run()
    elif game=='minesweeper':
        from Mine_sweeper.Minesweeper_pygame import run
        run()
    elif game=='snake':
        from Snake.Snake_Pygame import run
        run()
    elif game=='exit':
        play=False