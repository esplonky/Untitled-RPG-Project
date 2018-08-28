import pygame
import tileset
from tileset import tile_init
import os

if __name__ == '__main__':

    pygame.init()

    #Method needed to get a list of files
    def getTilesetFileList(tilesetFile):

        for groundFile in os.listdir('tilesetFile'):
            if groundFile.endswith(".png"):
                print groundFile
                return groundFile


    while 1:
        tilesetFileList = getTilesetFileList('tileset')
        for tilesetFile in tilesetFileList:
            tileset.tile_init.loadTileTable(tilesetFile)

