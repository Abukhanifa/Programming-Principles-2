import pygame
from datetime import datetime

    
def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Paint")
    font = pygame.font.SysFont("Verdana", 15)
    WHITE = (255,255,255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    radius = 15
    x = 0
    y = 0
    mode = 'BLUE'
    points = []
    screen.fill((0, 0, 0))
    while True:
        now = datetime.now()
        pressed = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()

        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                if event.key == pygame.K_r:
                    mode = 'RED'
                elif event.key == pygame.K_g:
                    mode = 'GREEN'
                elif event.key == pygame.K_b:
                    mode = 'BLUE'
                elif event.key == pygame.K_e:
                    mode = 'BLACK'
                elif event.key == pygame.K_t:
                    position = pygame.mouse.get_pos()
                    pygame.draw.polygon(screen, mode, ((position[0]-radius, position[1]+radius),
                                                       (position[0]+radius, position[1]+radius),
                                                       (position[0]-radius, position[1]-radius)))
                elif event.key == pygame.K_q:
                    position = pygame.mouse.get_pos()
                    pygame.draw.polygon(screen, mode, ((position[0], position[1]-radius),
                                                       (position[0]+radius, position[1]+radius),
                                                       (position[0]-radius, position[1]+radius)))
                elif event.key == pygame.K_h:
                    position = pygame.mouse.get_pos()
                    pygame.draw.polygon(screen, mode, ((position[0], position[1]-radius),
                                                       (position[0]+radius, position[1]),
                                                       (position[0], position[1] + radius),
                                                       (position[0]-radius, position[1])))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    radius = min(200, radius + 1)
                elif event.button == 5:
                    radius = max(1, radius - 1)
                elif event.button == 2:
                    position = event.pos
                    pygame.draw.circle(screen, mode, position, radius+20)
                elif event.button == 1:
                    if 6 <= mouse[0] <= 76 and 40 <= mouse[1] <= 65:
                        pygame.image.save(screen, f'{now.strftime("%Y.%m.%d-%H.%M.%S")}.jpeg')


                elif event.button == 3:
                    position = event.pos
                    pygame.draw.rect(screen, mode, (position[0] - radius*1.5, position[1] - radius*1.5, radius*3+10, radius*3+10))

            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                pygame.draw.circle(screen, mode, position, radius)

        pygame.display.flip()

        clock.tick(1000)


main()