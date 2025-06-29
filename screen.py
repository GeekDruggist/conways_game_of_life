import pygame


class Screen:
    LIGHTGREY = (70, 70, 70)
    DARKGREY = (55, 55, 55)
    GREEN = (160, 255, 60)
    TITLE = "Game of Life"
    ICON = pygame.image.load("./assets/bacterium-solid.svg")
    IMG = pygame.image.load("./assets/bacterium-solid-green.svg")

    WIDTH, HEIGHT = 800, 800
    TILE_SIZE = 20
    GRID_WIDTH = WIDTH // TILE_SIZE
    GRID_HEIGHT = HEIGHT // TILE_SIZE

    IMG = pygame.transform.scale(IMG, (TILE_SIZE, TILE_SIZE))

    FPS = 60

    screen = pygame.display.set_mode(size = (WIDTH, HEIGHT))
    pygame.display.set_icon(ICON)
    clock = pygame.time.Clock()