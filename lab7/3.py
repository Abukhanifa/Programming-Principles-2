import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
done = True
x, y = 25, 25

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        if event.type == pygame.KEYDOWN:
            if y<600-25 and event.key == pygame.K_DOWN:
                y+=20
            if y>25 and event.key == pygame.K_UP:
                y-=20
            if x<600-25 and event.key == pygame.K_RIGHT:
                x+=20
            if x>25 and event.key == pygame.K_LEFT:
                x-=20
                
        screen.fill((0,0,0))
        color = (255, 0, 0)
        pygame.draw.circle(screen, color, (x,y), 25)
        
        pygame.display.flip()
        clock.tick(60)
        
            