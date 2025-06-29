import pygame
import random
from screen import Screen as sc
from grid import Grid as gd
from populate import Populate as pl


pygame.init()

def main():
    running = True
    playing = False
    count = 0
    update_freq = 60
    positions = set()


    while running:
        pygame.display.set_caption(f"{sc.TITLE} - playing" if playing else f"{sc.TITLE} - paused")
        sc.clock.tick(sc.FPS)
        sc.screen.fill(sc.DARKGREY)
        gd.draw_grid(positions)
        pygame.display.flip()

        if playing:
            count += 1
        if count >= update_freq:
            count = 0
            positions = gd.adjust_grid(positions)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // sc.TILE_SIZE
                row = y // sc.TILE_SIZE
                position = (col, row)

                if position in positions:
                    positions.remove(position)
                else:
                    positions.add(position)
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                if event.key == pygame.K_SPACE:
                    playing = not playing

                if event.key == pygame.K_c:
                    positions = set()
                    playing = False
                    count = 0

                if event.key == pygame.K_g:
                    positions = pl.gen(random.randrange(4, 10) * sc.GRID_WIDTH) 

                
    pygame.quit()


if __name__ == "__main__":
    main()