import pygame
import pygame.locals
import os

def loadTileTable(filename, width, height):
    image = pygame.image.load(filename).convert()
    imageWidth, imageHeight = image.get_size()
    tileTable = []
    for tileX in range(0, imageWidth/width):
        line = []
        tileTable.append(line)
        for tileY in range(0, imageHeight/height):
            rect = (tileX * width, tileY * height, width, height)
            line.append(image.subsurface(rect))
        return tileTable

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((128, 98))
    screen.fill((255,255,255))
    table = loadTileTable("ground.png", 24, 16)
    for x, row in enumerate(table):
        for y, tile in enumerate(row):
            screen.blit(tile, (x * 32, y * 24))
    pygame.display.flip()
    while pygame.event.wait().type != pygame.locals.QUIT:
        pass



