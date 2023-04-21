import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    x = 0
    y = 0
    mode = 'BLUE'
    points = []
    screen.fill((0, 0, 0))
    while True:

        pressed = pygame.key.get_pressed()

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

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    radius = min(200, radius + 1)
                elif event.button == 5:
                    radius = max(1, radius - 1)
                elif event.button == 1:
                    position = event.pos
                    pygame.draw.circle(screen, mode, position, radius+20)
                elif event.button == 3:
                    position = event.pos
                    pygame.draw.rect(screen, mode, (position[0] - radius*1.5, position[1] - radius*1.5, radius*3+10, radius*3+10))

            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                pygame.draw.circle(screen, mode, position, radius)

        pygame.display.flip()

        clock.tick(1000)


main()