import pygame
import os
import grid

os.environ["SDL_VIDEO_CENTERED"]='1'

width, height =1920, 1080
size = (width, height)

pygame.init()
pygame.display.set_caption("Conway game of life")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

black = (0, 0, 0)
blue = (0, 14, 71)
white = (255, 255, 255)

scaler = 20
offset = 1

Grid = grid.Grid(width, height, scaler,offset)
Grid.random2d_array()
run = True
while run:
    clock.tick(fps)
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    Grid.Conway(off_color=white, on_color=blue, surface=screen)
    pygame.display.update()
pygame.quit()