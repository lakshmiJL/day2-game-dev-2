import pygame


pygame.init()

screen=pygame.display.set_mode((600, 600))


rocket = pygame.image.load("Lesson5/rocket.png")
rocket_x = 100
rocket_y = 200


#main loop
run = True
while run:
    screen.fill("white")
    #quit event to close the screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and rocket_y > 0:
                print("up")
                rocket_y -= 20
                pygame.display.update()
            if event.key == pygame.K_s and rocket_y < 450:
                print("down")
                rocket_y += 20
                pygame.display.update()
            if event.key == pygame.K_a:
                print("up")
                rocket_x -= 20
                pygame.display.update()
            if event.key == pygame.K_d:
                print("down")
                rocket_x += 20
                pygame.display.update()
    screen.blit(rocket,(rocket_x,rocket_y))
    #update the display
    pygame.display.update()