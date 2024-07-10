import pygame
pygame.init()
screen= pygame.display.set_mode((600,600))
screen.fill((255,255,255))
blue = (0,0,255)
pygame.display.update()


class Circle():
    def __init__(self,color,x,y,radius):
        self.circle_color = color
        self.x = x
        self.y = y
        self.circle_pos = (self.x,self.y)
        self.circle_radius = radius      
        self.circle_surface = screen
        
    def draw(self):
        pygame.draw.circle(self.circle_surface, self.circle_color, self.circle_pos, self.circle_radius)

    def grow(self):
        self.circle_radius = self.circle_radius + 5
        pygame.draw.circle(self.circle_surface, self.circle_color, self.circle_pos, self.circle_radius)
    def moveup(self):
        self.y -= 5
        self.circle_pos = (self.x,self.y)
        pygame.draw.circle(self.circle_surface, self.circle_color, self.circle_pos, self.circle_radius)
    def movedown(self):
        self.y += 5
        self.circle_pos = (self.x,self.y)
        pygame.draw.circle(self.circle_surface, self.circle_color, self.circle_pos, self.circle_radius)
circle=Circle(blue,300,300,25)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            circle.draw()
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONUP:
            circle.grow()
            pygame.display.update()
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            print(pos)
            c1 = Circle("red",pos[0],pos[1],10)
            c1.draw()
            pygame.display.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                screen.fill("white")
                print("up")
                circle.moveup()
                pygame.display.update()
            if event.key == pygame.K_DOWN:
                screen.fill("white")
                print("down")
                circle.movedown()
                pygame.display.update()
        
    
    
        