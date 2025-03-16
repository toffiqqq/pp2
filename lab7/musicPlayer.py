import pygame
import os

pygame.init()

WIDTH, HEIGHT = 400, 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Music player')

pygame.mixer.init()

music_folder = 'music'  
music_files = [f for f in os.listdir(music_folder) if f.endswith('.mp3')]

current_track = 0

def play_music():
    pygame.mixer.music.load(os.path.join(music_folder, music_files[current_track]))
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global current_track
    current_track = (current_track + 1) % len(music_files)
    play_music()

def prev_track():
    global current_track
    current_track = (current_track - 1) % len(music_files)
    play_music()

font = pygame.font.SysFont(None, 30)
def draw_interface():
    screen.fill((255, 255, 255))  

    track_name = music_files[current_track]
    text = font.render(f'Current music: {track_name}', True, (0, 0, 0))
    screen.blit(text, (20, 50))

    pygame.display.flip()

running = True
playing = False
while running:
    draw_interface()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_p]:  
        if not playing:
            play_music()
            playing = True
    if keys[pygame.K_s]:  
        stop_music()
        playing = False
    if keys[pygame.K_n]:  
        next_track()
    if keys[pygame.K_b]:  
        prev_track()

    pygame.time.Clock().tick(30)  


pygame.quit()