import pygame
import random



def linspace(a, b, n):
    return [n * i + a  for i in range((b/10))]

def initial_menu():

    """Returns the option chosen (1)\n-1 means EXIT"""
    
    pygame.init()
    screen_width = 600 # need to be a multiple of 10 (both) for linspace and rand food
    screen_height = 460
    font = pygame.font.SysFont("comicsansms", 30)
    op_1=font.render("1-SINGLE PLAYER", True, (10, 128, 0))
    op_2=font.render("2-MULTIPLAYER", True, (10, 128, 0))
    op_3=font.render("ESC-Exit", True, (10, 128, 0))

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Snakey')

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return -1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                return 1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                return 2

        # CLEAR SCREEN
        screen.fill((255, 255, 255))
        screen.blit(op_1, (screen_width/2 - op_1.get_width() // 2, screen_height / 3 - op_1.get_height() // 2))
        screen.blit(op_2, (screen_width/2 - op_1.get_width() // 2, screen_height /2 - op_1.get_height() // 2))
        screen.blit(op_3, (screen_width/2 - op_3.get_width() // 2, screen_height * 2/3 - op_3.get_height() // 2))
        pygame.display.flip()
        clock.tick(60)


def game_over():

    """GAME OVER"""

    pygame.init()
    screen_width = 600 # need to be a multiple of 10 (both) for linspace and rand food
    screen_height = 460
    font = pygame.font.SysFont("comicsansms", 30)
    op_1=font.render("GAME OVER", True, (0, 128, 0))
    done=False
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    while not done:
        # CLEAR SCREEN
        screen.fill((255, 255, 255))
        screen.blit(op_1, (screen_width/2 - op_1.get_width() // 2, screen_height / 3 - op_1.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(1000)
        clock.tick(60)
        done=True

def game_over_single(score):

    """GAME OVER"""

    pygame.init()
    screen_width = 600 # need to be a multiple of 10 (both) for linspace and rand food
    screen_height = 460
    font = pygame.font.SysFont("comicsansms", 30)
    op_1=font.render("GAME OVER", True, (0, 128, 0))
    score_msg=font.render("Final score : "+str(score), True, (0, 128, 0))
    done=False
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    while not done:
        # CLEAR SCREEN
        screen.fill((255, 255, 255))
        screen.blit(op_1, (screen_width/2 - op_1.get_width() // 2, screen_height / 3 - op_1.get_height() // 2))
        screen.blit(score_msg, (screen_width/2 - op_1.get_width() // 2, screen_height *2/3 - op_1.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(1000)
        clock.tick(60)
        done=True

def multiplayer():
	"""Classic Snake based game"""

	pygame.init()
	screen_width = 600 # need to be a multiple of 10 (both) for linspace and rand food
	screen_height = 460

	food_limit_x=linspace(10,screen_width-20,10)
	food_limit_y=linspace(10,screen_height-20,10)

	screen = pygame.display.set_mode((screen_width,screen_height))
	clock = pygame.time.Clock()

	done = False
	game_start=False
	eating=False

	sbodyx_blue=[20,30,40]
	sbodyy_blue=[20,20,20]
	sbodyx_red=[20,30,40]
	sbodyy_red=[50,50,50]

	cnt=0
	blue_score=0
	red_score=0
	num_ticks = 0

	class Snake:
		def __init__ (self, x_head, y_head, body_x,body_y, size, direction,thickness):
			self.x_head = x_head
			self.y_head = y_head
			self.body_x=body_x
			self.body_y=body_y
			self.size = size
			self.direction = direction # 1 -> UP ; 2 -> DOWN ; 3 -> LEFT ; 4 -> RIGHT
			self.thickness = thickness

	class Food:
		def __init__ (self, x_food,y_food, thickness):
			self.x_food=x_food
			self.y_food=y_food
			self.thickness=thickness


	blue_snake = Snake(50, 20,sbodyx_blue,sbodyy_blue,4, 4,10)
	red_snake = Snake(50, 50,sbodyx_red,sbodyy_red,4, 4,10)

	food_test=Food(screen_width/2,screen_height/2,10)

	
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				done = True

			pressed = pygame.key.get_pressed()
			if pressed[pygame.K_UP]:
				if blue_snake.direction != 2:
					blue_snake.direction = 1
					game_start=True
			elif pressed[pygame.K_DOWN]:
				if blue_snake.direction != 1:
					blue_snake.direction = 2
					game_start=True
			elif pressed[pygame.K_LEFT]:
				if blue_snake.direction != 4:
					blue_snake.direction = 3
					game_start=True
			elif pressed[pygame.K_RIGHT]:
				if blue_snake.direction != 3:
					blue_snake.direction = 4
					game_start=True
			if pressed[pygame.K_w]:
				if red_snake.direction != 2:
					red_snake.direction = 1
					game_start=True
			elif pressed[pygame.K_s]:
				if red_snake.direction != 1:
					red_snake.direction = 2
					game_start=True
			elif pressed[pygame.K_a]:
				if red_snake.direction != 4:
					red_snake.direction = 3
					game_start=True
			elif pressed[pygame.K_d]:
				if red_snake.direction != 3:
					red_snake.direction = 4
					game_start=True

		# CLEAR SCREEN
		screen.fill((255, 255, 255))

		#MOVE BLUE SNAKE
		if (blue_snake.direction==1 or blue_snake.direction==2 or blue_snake.direction==3 or blue_snake.direction==4 ) and game_start :
			eating=False
			for i in range(0,blue_snake.size-1):
				if(i==blue_snake.size-2):
					blue_snake.body_x[i]=blue_snake.x_head
					blue_snake.body_y[i]=blue_snake.y_head
				else :
					blue_snake.body_x[i]=blue_snake.body_x[i+1]
					blue_snake.body_y[i]=blue_snake.body_y[i+1]

			if blue_snake.direction==2:
				blue_snake.y_head+=blue_snake.thickness
			elif blue_snake.direction==4:
				blue_snake.x_head+=blue_snake.thickness
			elif blue_snake.direction==1:
				blue_snake.y_head-=blue_snake.thickness
			elif blue_snake.direction==3:
				blue_snake.x_head-=blue_snake.thickness

		#MOVE RED SNAKE
		if (red_snake.direction==1 or red_snake.direction==2 or red_snake.direction==3 or red_snake.direction==4 ) and game_start :
			eating=False
			for i in range(0,red_snake.size-1):
				if(i==red_snake.size-2):
					red_snake.body_x[i]=red_snake.x_head
					red_snake.body_y[i]=red_snake.y_head
				else :
					red_snake.body_x[i]=red_snake.body_x[i+1]
					red_snake.body_y[i]=red_snake.body_y[i+1]

			if red_snake.direction==2:
				red_snake.y_head+=red_snake.thickness
			elif red_snake.direction==4:
				red_snake.x_head+=red_snake.thickness
			elif red_snake.direction==1:
				red_snake.y_head-=red_snake.thickness
			elif red_snake.direction==3:
				red_snake.x_head-=red_snake.thickness

		#DETECT FOOD COLLISION 
		#BLUE SNAKE
		if(blue_snake.x_head==food_test.x_food and blue_snake.y_head==food_test.y_food):
			blue_snake.body_x.append(blue_snake.x_head) # append add item to end of list
			blue_snake.body_y.append(blue_snake.y_head)
			blue_snake.size+=1
			food_test.x_food=random.choice(food_limit_x)
			food_test.y_food=random.choice(food_limit_y)
			eating=True
			blue_score += 1

		#RED SNAKE
		if(red_snake.x_head==food_test.x_food and red_snake.y_head==food_test.y_food):
			red_snake.body_x.append(red_snake.x_head) # append add item to end of list
			red_snake.body_y.append(red_snake.y_head)
			red_snake.size+=1
			food_test.x_food=random.choice(food_limit_x)
			food_test.y_food=random.choice(food_limit_y)
			eating=True
			red_score += 1

		#DETECT WALLS COLLISION 
		if(blue_snake.x_head<10 or blue_snake.x_head>screen_width-10 or blue_snake.y_head<10 or blue_snake.y_head>screen_height-10):
			game_over()
			done=True
		if(red_snake.x_head<10 or red_snake.x_head>screen_width-10 or red_snake.y_head<10 or red_snake.y_head>screen_height-10):
			game_over()
			done=True


		#DETECT SNAKE COLLISION
		for i in range(0,blue_snake.size-1):
			if(blue_snake.x_head==blue_snake.body_x[i] and blue_snake.y_head==blue_snake.body_y[i] and not eating):
				game_over()
				done=True
		for i in range(0,red_snake.size-1):
			if(red_snake.x_head==red_snake.body_x[i] and red_snake.y_head==red_snake.body_y[i] and not eating):
				game_over()
				done=True


		#DRAWING

		#SCORES
		font = pygame.font.SysFont("comicsansms", 20)
		blue_score_msg=font.render(str(blue_score), True, (0, 0, 255))
		red_score_msg=font.render(str(red_score), True, (255, 0, 0))
		screen.blit(blue_score_msg, (screen_width-30 - blue_score_msg.get_width() // 2, 10 + blue_score_msg.get_height() // 2))
		screen.blit(red_score_msg, (screen_width-30 - red_score_msg.get_width() // 2, screen_height -30 - red_score_msg.get_height() // 2))

		#BLUE SNAKE
		while cnt < (blue_snake.size-1) :
			pygame.draw.rect(screen,(0,0,255),pygame.Rect(blue_snake.body_x[cnt],blue_snake.body_y[cnt], blue_snake.thickness,blue_snake.thickness))
			cnt+=1
		pygame.draw.rect(screen,(0,0,128),pygame.Rect(blue_snake.x_head,blue_snake.y_head, blue_snake.thickness,blue_snake.thickness))
		cnt=0
		#RED SNAKE
		while cnt < (red_snake.size-1) :
			pygame.draw.rect(screen,(255,0,0),pygame.Rect(red_snake.body_x[cnt],red_snake.body_y[cnt], red_snake.thickness,red_snake.thickness))
			cnt+=1
		pygame.draw.rect(screen,(128,0,0),pygame.Rect(red_snake.x_head,red_snake.y_head, red_snake.thickness,red_snake.thickness))
		cnt=0

		#FOOD
		pygame.draw.rect(screen,(0,128,0),pygame.Rect(food_test.x_food,food_test.y_food, food_test.thickness,food_test.thickness))


		#WALLS
		pygame.draw.rect(screen,(0,0,0),pygame.Rect(0,0,10,screen_height))
		pygame.draw.rect(screen,(0,0,0),pygame.Rect(0,0,screen_width,10))
		pygame.draw.rect(screen,(0,0,0),pygame.Rect(screen_width-10,0,10,screen_height))
		pygame.draw.rect(screen,(0,0,0),pygame.Rect(0,screen_height-10,screen_width,10))


		pygame.display.flip()
		clock.tick(30)

def single_player():
	"""Classic Snake based game"""

	pygame.init()
	screen_width = 600 # need to be a multiple of 10 (both) for linspace and rand food
	screen_height = 460

	food_limit_x=linspace(10,screen_width-20,10)
	food_limit_y=linspace(10,screen_height-20,10)

	print food_limit_x
	print food_limit_y

	screen = pygame.display.set_mode((screen_width,screen_height))
	clock = pygame.time.Clock()

	done = False
	game_start=False
	eating=False
	sbodyx=[20,30,40]
	sbodyy=[20,20,20]
	cnt=0
	score=0

	font = pygame.font.SysFont("comicsansms", 20)
   

	class Snake:
		def __init__ (self, x_head, y_head, body_x,body_y, size, direction,thickness):
			self.x_head = x_head
			self.y_head = y_head
			self.body_x=body_x
			self.body_y=body_y
			self.size = size
			self.direction = direction # 1 -> UP ; 2 -> DOWN ; 3 -> LEFT ; 4 -> RIGHT
			self.thickness = thickness

	class Food:
		def __init__ (self, x_food,y_food, thickness):
			self.x_food=x_food
			self.y_food=y_food
			self.thickness=thickness


	blue_snake = Snake(50, 20,sbodyx,sbodyy,4, 4,10)
	food_test=Food(screen_width/2,screen_height/2,10)

	
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				done = True

			pressed = pygame.key.get_pressed()
			if pressed[pygame.K_UP]:
				if blue_snake.direction != 2:
					blue_snake.direction = 1
					game_start=True
			elif pressed[pygame.K_DOWN]:
				if blue_snake.direction != 1:
					blue_snake.direction = 2
					game_start=True
			elif pressed[pygame.K_LEFT]:
				if blue_snake.direction != 4:
					blue_snake.direction = 3
					game_start=True
			elif pressed[pygame.K_RIGHT]:
				if blue_snake.direction != 3:
					blue_snake.direction = 4
					game_start=True

		# CLEAR SCREEN
		screen.fill((255, 255, 255))


		#MOVE SNAKE
		if (blue_snake.direction==1 or blue_snake.direction==2 or blue_snake.direction==3 or blue_snake.direction==4 ) and game_start :
			eating=False
			for i in range(0,blue_snake.size-1):
				if(i==blue_snake.size-2):
					blue_snake.body_x[i]=blue_snake.x_head
					blue_snake.body_y[i]=blue_snake.y_head
				else :
					blue_snake.body_x[i]=blue_snake.body_x[i+1]
					blue_snake.body_y[i]=blue_snake.body_y[i+1]

			if blue_snake.direction==2:
				blue_snake.y_head+=blue_snake.thickness
			elif blue_snake.direction==4:
				blue_snake.x_head+=blue_snake.thickness
			elif blue_snake.direction==1:
				blue_snake.y_head-=blue_snake.thickness
			elif blue_snake.direction==3:
				blue_snake.x_head-=blue_snake.thickness


		#DETECT FOOD COLLISION 
		if(blue_snake.x_head==food_test.x_food and blue_snake.y_head==food_test.y_food):
			blue_snake.body_x.append(blue_snake.x_head) # append add item to end of list
			blue_snake.body_y.append(blue_snake.y_head)
			blue_snake.size+=1
			food_test.x_food=random.choice(food_limit_x)
			food_test.y_food=random.choice(food_limit_y)
			eating=True
			score+=1

		#SCORES
		op_1=font.render(str(score), True, (0, 0, 0))
		screen.blit(op_1, (screen_width-30 - op_1.get_width() // 2, screen_height-30 - op_1.get_height() // 2))


		#DETECT WALLS COLLISION 
		if(blue_snake.x_head<10 or blue_snake.x_head>screen_width-10 or blue_snake.y_head<10 or blue_snake.y_head>screen_height-10):
			game_over_single(score)
			done = True
			


		#DETECT SNAKE COLLISION
		for i in range(0,blue_snake.size-1):
			if(blue_snake.x_head==blue_snake.body_x[i] and blue_snake.y_head==blue_snake.body_y[i] and not eating):
				game_over_single(score)
				done = True

		#BLUE SNAKE
		while cnt < (blue_snake.size-1) :
			pygame.draw.rect(screen,(0,0,0),pygame.Rect(blue_snake.body_x[cnt],blue_snake.body_y[cnt], blue_snake.thickness,blue_snake.thickness),1)
			cnt+=1
		pygame.draw.rect(screen,(0,0,0),pygame.Rect(blue_snake.x_head,blue_snake.y_head, blue_snake.thickness,blue_snake.thickness))
		cnt=0

		#FOOD
		pygame.draw.rect(screen,(255,0,0),pygame.Rect(food_test.x_food,food_test.y_food, food_test.thickness,food_test.thickness),1)


		#WALLS
		pygame.draw.rect(screen,(0,0,0),pygame.Rect(0,0,10,screen_height))
		pygame.draw.rect(screen,(0,0,0),pygame.Rect(0,0,screen_width,10))
		pygame.draw.rect(screen,(0,0,0),pygame.Rect(screen_width-10,0,10,screen_height))
		pygame.draw.rect(screen,(0,0,0),pygame.Rect(0,screen_height-10,screen_width,10))


		pygame.display.flip()
		clock.tick(30)



done=False
while not done:
	game_mode=initial_menu()
	if(game_mode==1):
		single_player()
	elif(game_mode==2):
		multiplayer()
	else:
		done=True