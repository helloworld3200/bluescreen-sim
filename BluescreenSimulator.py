import pygame
from pygame.locals import *

pygame.init()

def drawtext(size, text, pos, colour=(0, 0, 0)):
  win = pygame.display.get_surface()
  font = pygame.SysFont("Calibri", size)
  ready_text = font.render(text, True, colour)
  rendered_text = win.blit(ready_text, pos)
  return rendered_text

def runmain():
  win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
  blue = (0, 0, 255)
  running = True
  text_x = 0
  pygame.mouse.set_visible(False)
  while running:
    pygame.display.update()
    win.fill(blue)
    for event in pygame.event.get():
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_ESCAPE:
            running = False
  pygame.display.quit()
  pygame.quit()

if __name__ == "__main__":
  runmain()
