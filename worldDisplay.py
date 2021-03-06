import worldGen
import terrain
import pygame
from pygame.locals import *

##worldsize = 64
window = (50, 50)
layers = {}

##display = pygame.display.set_mode((1250, 750))

##terrainImgDict = {0 : pygame.image.load('water.png'), 1 : pygame.image.load('grass.png'), 2 : pygame.image.load('plains.png'),
##               3 : pygame.image.load('hill.png'), 4 : pygame.image.load('mountain.png'), 5 : pygame.image.load('tundra.png'),
##               6 : pygame.image.load('desert.png'), 7 : pygame.image.load('forest.png'), 8 : pygame.image.load('jungle.png')}

def generateGridLayer(world):
    """
    Generates a grid layer on the map.
    """
    gridLayer = [[]]
    gridLayer.insert(0, False)
    for x in range(len(world)):
        gridLayer[1].append([])
        for y in range(len(world[x])):
            gridLayer[1][x].append(pygame.image.load('grid.png'))
    return gridLayer

def generateTerrainLayer(world):
    """
    Generates an image layer of the terrain of the world.
    Takes in a world to create an image layer from it.
    Returns an array of image objects to be displayed.
    """
##    world = worldGen.generateWorld(worldsize)
    terrainLayer = [[]]
    terrainLayer.insert(0, True)
    for x in range(len(world)):
        terrainLayer[1].append([])
        for y in range(len(world[x])):
            terrainLayer[1][x].append(world[x][y].image)
##            terrainLayer[x].append(terrain.terrainDict[world[x][y]])
    return terrainLayer

def displayLayer(layer, display):
    """
    Displays a layer onto the screen.
    Takes in a layer, generated by the generateLayer() functions.
    """
    for x in range(len(layer[1]) - window[0]):
        for y in range(len(layer[1][x]) - window[1]):
            display.blit(layer[1][x + window[0]][y + window[1]], (x * 50,y * 50))

##terrainLayer = generateTerrainLayer(world)


##    for event in pygame.event.get():
def displayEvent(event, window, layers, worldsize):
    """
    Goes through events that change the display, such as panning.
    Takes in an event, as determined by the main event loop.
    """
    if event.type == KEYDOWN:
        if event.key == K_DOWN and window[1] < worldsize:
            window = (window[0],window[1] + 1)
        elif event.key == K_UP and window[1] > 0:
            window = (window[0],window[1] - 1)
        if event.key == K_LEFT and window[0] > 0:
            window = (window[0] - 1,window[1])
        elif event.key == K_RIGHT and window[0] < worldsize:
            window = (window[0] + 1,window[1])
        if event.key == K_TAB:
            if not layers['grid'][0]:
                layers['grid'][0] = True
            elif layers['grid'][0]:
                layers['grid'][0] = False
    return window, layers

def display(layers, display):
    """
    Displays all layers onto the screen.
    Takes in a list of  layers to be displayed.
    """
    display.fill((150,25,50))
##    print(layers['grid'][0])
    if layers['terrain'][0]:
        displayLayer(layers['terrain'], display)
    if layers['grid'][0]:
        displayLayer(layers['grid'], display)
    pygame.display.update()            
##            display.blit(blits[world[window[0]+x][window[1]+y]], (x*50,y*50))
##            if x==10 and y==10:
##                display.blit(cityImg_b,(x*zoomsqrt,y*zoomsqrt))
##            if x==7 and y==9:
##                display.blit(townImg_b,(x*zoomsqrt,y*zoomsqrt))
