import pygame
from screen import Screen as sc
from neighbours import Neighbours as nb


class Grid:
    def draw_grid(positions):
        for position in positions:
            col, row = position
            top_left = (col * sc.TILE_SIZE, row * sc.TILE_SIZE)
            rect = pygame.draw.rect(sc.screen, sc.DARKGREY, (*top_left, sc.TILE_SIZE, sc.TILE_SIZE))
            sc.screen.blit(sc.IMG, rect)
        

        for row in range(sc.GRID_HEIGHT):
            pygame.draw.line(surface = sc.screen, color = sc.LIGHTGREY, start_pos = (0, row * sc.TILE_SIZE), end_pos = (sc.WIDTH, row * sc.TILE_SIZE), width=1)

        for col in range(sc.GRID_WIDTH):
            pygame.draw.line(surface = sc.screen, color = sc.LIGHTGREY, start_pos = (col * sc.TILE_SIZE, 0), end_pos = (col * sc.TILE_SIZE, sc.HEIGHT), width=1)

    def adjust_grid(positions):
        all_neighbours = set()
        updated_positions = set()

        for position in positions:
            neighbours = nb.get_neighbours(position)
            all_neighbours.update(neighbours)
            neighbours = list(filter(lambda x: x in positions, neighbours))

            if len(neighbours) in [2, 3]:
                updated_positions.add(position)

        for position in all_neighbours:
            neighbours = nb.get_neighbours(position)
            neighbours = list(filter(lambda x: x in positions, neighbours))  

            if len(neighbours) == 3:
                updated_positions.add(position)

        return updated_positions