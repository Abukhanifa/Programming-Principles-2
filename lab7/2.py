import pygame
import os

def song_player(command, path, state=True):
    if os.path.exists(path):
        if command == "play\\stop":
            if state == True:
                pygame.mixer.music.load(path)
                pygame.mixer.music.play(0)
            else:
                pygame.mixer.music.stop()
        elif command == "change":
            pygame.mixer.music.load(path)
            pygame.mixer.music.play(0)
            
            
path = os.path.join(os.getcwd(), "music")
songs = os.listdir(path)      
            
pygame.init()
screen = pygame.display.set_mode((900, 700))
clock = pygame.time.Clock()
state = False
done = True
i=0

font = pygame.font.SysFont("times new roman", 28)

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done= False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                state = not state
                song_player("play\\stop", path + "\\" + songs[i], state)
                
            if event.key == pygame.K_LEFT:
                i+=1
                i = i % len(songs)
                song_player("change", path + "\\" + songs[i])
                
            if event.key == pygame.K_RIGHT:
                i-=1
                i = i % len(songs)
                song_player("change", path + "\\" + songs[i])
                
                
    screen.fill((0,0,0))
    song_name = font.render(songs[i], True, (255, 255, 255))
    screen.blit(song_name, (0, 0))

    pygame.display.flip()
    clock.tick(60)

                
            
        
            
    