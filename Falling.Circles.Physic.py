import os, sys, math, pygame, pygame.mixer, random
from pygame.locals import *

BLACK = 0,0,0
WHITE = 255,255,255
RED = 255,0,0
GREEN = 0,255,0
BLUE = 0,0,255
COLORS = [BLACK, RED, GREEN, BLUE]
FPS_LIMIT = 60
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 680,480
INITIAL_VELOCITY = 150
GRAVITY = pygame.math.Vector2(0.0,80.0)
DRAG = 0.1

class Circle:
	def __init__(self, 
				position, 
				size = 1, 
				color = (0,69,255),
				width = 0, 
				velocity = pygame.math.Vector2(0,0), 
				acceleration = pygame.math.Vector2(0,0)):
		self.position = position
		self.size = size #radius
		self.color = color
		self.width = width #of line
		self.velocity = velocity
		self.acceleration = acceleration

	def display(self):
		rx, ry = int(self.position.x), int(self.position.y)
		pygame.draw.circle(screen, self.color, (rx,ry), self.size, self.width)

	def move(self):
		self.position += self.velocity * dtime +0.5*(self.acceleration * (dtime ** 2))
		self.velocity += self.acceleration * dtime 
		self.velocity -= self.velocity * DRAG * dtime
		self.bounce()

	def change_velocity(self, velocity):
		self.velocity = velocity

	def bounce(self):
		if self.position.x <= self.size:
			self.position.x = 2*self.size - self.position.x
			self.velocity = self.velocity.reflect(pygame.math.Vector2(1,0))
		elif self.position.x >= 2*(SCREEN_WIDTH - self.size) - self.position.x:
			self.velocity = self.velocity.reflect(pygame.math.Vector2(1,0))

		if self.position.y <= self.size:
			self.position.y = 2*self.size - self.position.y
			self.velocity = self.velocity.reflect(pygame.math.Vector2(0,1))
		elif self.position.y >= 2*(SCREEN_HEIGHT - self.size) - self.position.y:
			self.velocity = self.velocity.reflect(pygame.math.Vector2(0,1))

	def surface_distance (self, other_circle, time):
		radiiAB = self.size + other_circle.size
		pos_A = self.position + self.velocity * time + 0.5*(self.acceleration * (time**2))
		pos_B = other_circle.position + other_circle.velocity * time + 0.5*(self.acceleration * (time**2))
		pos_AB = pos_A.distance_to(pos_B)
		return  pos_AB - radiiAB
		
	def collide (self, other):
		if self.surface_distance(other, dtime) <= 0:
			collision_vector = self.position - other.position
			collision_vector.normalize()
			self.velocity = self.velocity.reflect(collision_vector)
			other.velocity = other.velocity.reflect(collision_vector)


def get_random_velocity():
	new_angle = random.uniform(0, math.pi*2)
	new_x = math.sin(new_angle)
	new_y = math.cos(new_angle)
	new_vector = pygame.math.Vector2(new_x,new_y)
	new_vector.normalize()
	new_vector *= INITIAL_VELOCITY
	return new_vector

def define_new_velocity(x,y):
	new_angle = math.atan2(y,x) + 0.5*math.pi
	new_x = math.sin(new_angle)
	new_y = math.cos(new_angle)
	new_vector = pygame.math.Vector2(new_x,new_y)
	new_vector.normalize()
	print(new_vector)
	new_vector *= new_vector.length() * 0.1
	print(new_vector)
	print('----')
	return new_vector

def find_circle(list_of_circles, x, y):
	for each in list_of_circles:
		if (each.position - [x,y]).length() <= each.size:
			return each
	return None

def spawn_circle(num_of_time):
	circle_list = []
	for each in range(num_of_time):
		size = random.randint(10,20)
		x = random.randint(size, SCREEN_WIDTH-size)
		y = random.randint(size, SCREEN_HEIGHT-size)
		color = random.choice(COLORS)
		width = random.randint(0,10)
		velocity = get_random_velocity()
		circle_list.append(Circle(pygame.math.Vector2(x,y),size,color,width,velocity,GRAVITY))
	return circle_list

if __name__ == '__main__':

	screen = pygame.display.set_mode(SCREEN_SIZE)
	clock = pygame.time.Clock()
	pygame.display.set_caption('Physic')
	run_me = True

	num_of_circle = 10
	circles = spawn_circle(num_of_circle)
	clicked_circle = None
	direction_tick = 0.0

	while run_me:
		dtime_ms = clock.tick(FPS_LIMIT)
		dtime = dtime_ms / 1000.0
		screen.fill(WHITE)

		#direction_tick += dtime
		#if (direction_tick > 1.0):
		#	direction_tick = 0.0
		#	random_circle = random.choice(circles)
		#	new_velocity = get_random_velocity()
		#	random_circle.change_velocity(new_velocity)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run_me = False

			if event.type == pygame.MOUSEBUTTONDOWN:
				(mouse_X, mouse_Y) = pygame.mouse.get_pos()
				clicked_circle = find_circle(circles,mouse_X,mouse_Y)

			elif event.type == pygame.MOUSEBUTTONUP:
				clicked_circle = None

		for i, each in enumerate(circles):
			if each != clicked_circle:
				each.move()
			for other_circle2 in circles[i+1:]:
				each.collide(other_circle2)
			each.display()

		if clicked_circle:
			(mouse_X, mouse_Y) = pygame.mouse.get_pos()
			dx = mouse_X - clicked_circle.position[0] 
			dy = mouse_Y - clicked_circle.position[1] 
			clicked_circle.position = pygame.math.Vector2(mouse_X, mouse_Y)
			clicked_circle.velocity = define_new_velocity(dx,dy)
			

		pygame.display.flip()


	pygame.quit()
	sys.exit()