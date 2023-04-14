import pygame
import time


pygame.init()
screen = pygame.display.set_mode((800, 800))
done = False
pygame.display.set_caption("Mickey clock")
pygame.display.set_icon(pygame.image.load("images/icon.png"))
clock = pygame.time.Clock()


clocks = pygame.image.load('images/clock.png')
rhand = pygame.image.load('images/right.png')
lhand = pygame.image.load('images/left.png')

w, h = rhand.get_size()
l, e = lhand.get_size()

def blitRotate(surf, image, pos, originPos, angle):
    image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    rotated_offset = offset_center_to_pivot.rotate(-angle)
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)
    surf.blit(rotated_image, rotated_image_rect)

while not done:
    screen.fill((0, 0, 0))
    screen.blit(clocks, (0, 0))
    pos = (screen.get_width() / 2, screen.get_height() / 2)
    blitRotate(screen, rhand, pos, (w / 2, h / 2), -time.time() % 3600 / 10)
    blitRotate(screen, lhand, pos, (l / 2, e / 2), -time.time() % 60 * 6)
    pygame.draw.circle(screen, 'Black', (400,400), 40)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
    clock.tick(144)