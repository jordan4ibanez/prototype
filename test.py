import pygame
from random import randint
pygame.init()
screen = pygame.display.set_mode((900, 500))
pygame.display.set_caption("Action RPG with guns")

image = pygame.image.load("grass.png")
image = pygame.transform.scale(image, (64,64))
image = image.convert()

game = True

alpha = 0

map_size = (10,10)
map_list = {}
for x in range(map_size[0]):
	map_list[x] = {}
	for y in range(map_size[1]):
		map_list[x][y] = {}
		map_list[x][y]["alpha"] = 0
	
light = [0,0]

def light_update():
	#Reset all alphas (light update)
	for x in range(map_size[0]):
		for y in range(map_size[1]):
			map_list[x][y]["alpha"] = 0
def spread_light():
	#spread light
	for x in range(map_size[0]):
		for y in range(map_size[1]):
			if (x == light[0] and y == light[1]):
				map_list[x][y]["alpha"] = 255
				
			if x + 1 <= map_size[0] - 1:
				if map_list[x + 1][y]["alpha"] < map_list[x][y]["alpha"]:
					map_list[x + 1][y]["alpha"] = map_list[x][y]["alpha"] - 40
			

			if y + 1 <= map_size[1] - 1:
				if map_list[x][y + 1]["alpha"] < map_list[x][y]["alpha"]:
					map_list[x][y + 1]["alpha"] = map_list[x][y]["alpha"] - 40
	
	for x in reversed(range(map_size[0])):
		for y in reversed(range(map_size[1])):
			if (x == light[0] and y == light[1]):
				map_list[x][y]["alpha"] = 255
			if x - 1 >= 0:
				if map_list[x - 1][y]["alpha"] < map_list[x][y]["alpha"]:
					map_list[x - 1][y]["alpha"] = map_list[x][y]["alpha"] - 40	
			if y - 1 >= 0:
				if map_list[x][y - 1]["alpha"] < map_list[x][y]["alpha"]:
					map_list[x][y - 1]["alpha"] = map_list[x][y]["alpha"] - 40
def physical():
	light_update()
	spread_light()

while game == True:
	screen.fill((0, 0, 0))
	physical()
	events = pygame.event.get()
	
	for event in events:
		if event.type == pygame.QUIT:
			game = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				light[0] -= 1
			if event.key == pygame.K_RIGHT:
				light[0] += 1
			if event.key == pygame.K_UP:
				light[1] -= 1
			if event.key == pygame.K_DOWN:
				light[1] += 1
			
				
	#draw the world
	for x in range(map_size[0]):
		for y in range(map_size[1]):
			image.set_alpha(map_list[x][y]["alpha"])
			screen.blit(image,(x*64,y*64))
			
	pygame.display.flip()
