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
"player":{"physical":True,"pos":[72,72],"size":[128,45],"inertia":[0,0],"on_ground":False},
"obj1":{"physical":True,"pos":[566,556],"size":[56,56],"inertia":[0,0],"on_ground":False},
}

map_size = (10,10)
map_list = {}
for x in range(map_size[0]):
	map_list[x] = {}
	for y in range(map_size[1]):
		map_list[x][y] = {}
		if y == 9 or x == 9 or x == 0 or y == 0:
			map_list[x][y]["tile"] = 1
			map_list[x][y]["friction"] = 0.1
		else:
			map_list[x][y]["tile"] = 0
count_x = 0
count_y = 0
while game == True:
	screen.fill((0, 0, 0))
	key = pygame.key.get_pressed()
	if key[pygame.K_RIGHT]:
		count_x += 0.1
	if key[pygame.K_LEFT]:
		count_x -= 0.1
	if key[pygame.K_UP]:
		count_y -= 0.1
	if key[pygame.K_DOWN]:
		count_y += 0.1
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	#physics/collision detection with environment
	for i, val in enumerate(objects):
		
		size_x = objects[val]["size"][0]
		size_y = objects[val]["size"][1]
		pos_x  = int(round(objects[val]["pos"][0],0))
		pos_y  = int(round(objects[val]["pos"][1],0))
		inertia_x = objects[val]["inertia"][0] + count_x
		inertia_y = objects[val]["inertia"][1] + count_y
		#collide with environment
		# do this specifically for - or + inertia (to avoid clipping
		if (map_list[(pos_x+(size_x/2))/64][pos_y/64]["tile"] == 0 and inertia_x > 0) or (map_list[(pos_x-(size_x/2))/64][pos_y/64]["tile"] == 0 and inertia_x < 0):
			#if map_list[(pos_x+(size_x/2))/64][pos_y/64]["tile"] == 0: ---wrong quard
			#	objects[val]["on_ground"] = True
			objects[val]["pos"][0] = objects[val]["pos"][0] + inertia_x
			print("make this push a value to the end to move at the end")
		#else:
		#	objects[val]["inertia"][0] = 0
			
		if (map_list[pos_x/64][(pos_y+(size_y/2))/64]["tile"] == 0 and inertia_y > 0) or (map_list[pos_x/64][(pos_y-(size_y/2))/64]["tile"] == 0 and inertia_y < 0):
			objects[val]["pos"][1] = objects[val]["pos"][1] + inertia_y
		#else:
		#	if inertia_y > 0:
		#		if inertia_x > 0:
		#			objects[val]["inertia"][0] = objects[val]["inertia"][0] - map_list[pos_x/64][(pos_y+(size_y/2))/64]["friction"]
		#		if inertia_x < 0:
		#			objects[val]["inertia"][0] = objects[val]["inertia"][0] + map_list[pos_x/64][(pos_y+(size_y/2))/64]["friction"]
		#	objects[val]["inertia"][1] = 0
		#objects["player"]["pos"][1] = objects["player"]["pos"][1] + objects["player"]["inertia"][1]
		
		
		
		#collide with other objects
		for i, val2 in enumerate(objects):
			if val != val2:
				size_x = objects[val2]["size"][0]
				size_y = objects[val2]["size"][1]
				pos_x  = int(round(objects[val2]["pos"][0],0))
				pos_y  = int(round(objects[val2]["pos"][1],0))
				inertia_x = objects[val2]["inertia"][0] + count_x
				inertia_y = objects[val2]["inertia"][1] + count_y				
				
			
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
