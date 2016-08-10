#collision detection test

import pygame
from random import randint
pygame.init()
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("Action RPG with guns")

image = pygame.image.load("grass.png")
image = pygame.transform.scale(image, (64,64))
image2 = pygame.image.load("grass.png")
image2 = pygame.transform.scale(image, (64,64))
image = image.convert()

game  = True
objects = {
"player":{"physical":True,"pos":[10,10],"size":[20,20],"inertia":[0,1]},
}

map_size = (10,10)
map_list = {}
for x in range(map_size[0]):
	map_list[x] = {}
	for y in range(map_size[1]):
		map_list[x][y] = {}
		if y == 9:
			map_list[x][y]["tile"] = 1
		else:
			map_list[x][y]["tile"] = 0

while game == True:
	screen.fill((0, 0, 0))
	
	for i, val in enumerate(objects):
		print(val)
		size_x = objects[val]["size"][0]
		size_y = objects[val]["size"][1]
		pos_x  = objects[val]["pos"][0]
		pos_y  = objects[val]["pos"][1]
		inertia_x = objects[val]["inertia"][0]
		inertia_y = objects[val]["inertia"][1]
	
		# do this specifically for - or + inertia (to avoid clipping	
		if map_list[(pos_x+(size_x/2))/64][pos_y/64]["tile"] == 0 and map_list[(pos_x-(size_x/2))/64][pos_y/64]["tile"] == 0:
			objects[val]["pos"][0] = pos_x + inertia_x
			
		if map_list[pos_x/64][(pos_y+(size_y/2))/64]["tile"] == 0 and map_list[pos_x/64][(pos_y-(size_y/2))/64]["tile"] == 0:
			objects[val]["pos"][1] = pos_y + inertia_y
	
		
		
		#objects["player"]["pos"][1] = objects["player"]["pos"][1] + objects["player"]["inertia"][1]
	for i, val in enumerate(objects):
		image = pygame.transform.scale(image, objects[val]["size"])
		screen.blit(image,(objects[val]["pos"][0]-(objects[val]["size"][0]/2),objects[val]["pos"][1]-(objects[val]["size"][1]/2)))
		
	#draw the world
	for x in range(map_size[0]):
		for y in range(map_size[1]):
			if map_list[x][y]["tile"] == 1:
				image2 = pygame.transform.scale(image, (64,64))
				screen.blit(image2,(x*64,y*64))
			
	pygame.display.flip()
