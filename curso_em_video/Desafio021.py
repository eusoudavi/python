import pygame

pygame.init()
pygame.mixer.music.load('energy.mp3')
pygame.mixer.music.play()
pygame.display.init()
pygame.event.wait()
a = input('Digite algo para parar a música')
print('FIM')
