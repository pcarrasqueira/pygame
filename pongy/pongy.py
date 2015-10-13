import pygame
import os
import random


def main():
    option = initial_menu(1000,800)
    show_keys (1000,800,option)
    gameplay(option)


_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

def add_score(score):
    next_score = int(score)+1
    return str(next_score)

def is_game_over(score):
    if (score == "5"):
        return True
    else:
        return False


def initial_menu(screen_width, screen_height):

    """Returns the option chosen (1 - 3)\n-1 means EXIT"""
    
    pygame.init()
    
    font = pygame.font.SysFont("comicsansms", 30)
    op_1=font.render("1-Single Player", True, (0, 128, 0))
    op_2=font.render("2-Multiplayer", True, (0, 128, 0))
    op_3=font.render("ESC-Exit", True, (0, 128, 0))


    screen = pygame.display.set_mode((screen_width, screen_height))
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
        screen.blit(op_2, (screen_width/2 - op_2.get_width() // 2, screen_height / 2 - op_2.get_height() // 2))
        screen.blit(op_3, (screen_width/2 - op_3.get_width() // 2, screen_height * 2/3 - op_3.get_height() // 2))

        pygame.display.flip()
        clock.tick(60)

def show_keys(screen_width, screen_height, game_mode):

    pygame.init()
    done = False
    font = pygame.font.SysFont("comicsansms", 30)

    if game_mode == 1:
        key_1=font.render("Move: <Arrows>", True, (0, 0, 0))
        key_2=font.render("Shoot: <Down_Arrow>", True, (0, 0, 0))
        key_3=font.render("Launch ball: <Space>", True, (0, 0, 0))
        key_4=font.render("Exit: <Escape>", True, (0, 0, 0))
        proceed_key=font.render("Press any key to continue...", True, (0, 0, 0))

    elif game_mode == 2:
        key_1=font.render("Move: <Arrows>", True, (0, 128, 0))
        key_2=font.render("Shoot: <Down_Arrow>", True, (0, 128, 0))
        key_3=font.render("Move: <Z - X>", True, (0, 0, 128))
        key_4=font.render("Shoot: <C>", True, (0, 0, 128))
        key_5=font.render("Launch ball: <Space>", True, (0, 0, 0))
        key_6=font.render("Exit: <Escape>", True, (0, 0, 0))
        proceed_key=font.render("Press any key to continue...", True, (0, 0, 0))


    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()


    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                done = True

        # CLEAR SCREEN
        screen.fill((255, 255, 255))

        if game_mode == 1:
            screen.blit(key_1, (screen_width/2 - key_1.get_width() // 2, screen_height /6 - key_1.get_height() // 2))
            screen.blit(key_2, (screen_width/2 - key_2.get_width() // 2, screen_height *2/6 - key_2.get_height() // 2))
            screen.blit(key_3, (screen_width/2 - key_3.get_width() // 2, screen_height *3/6 - key_3.get_height() // 2))
            screen.blit(key_4, (screen_width/2 - key_4.get_width() // 2, screen_height *4/6 - key_4.get_height() // 2))
            screen.blit(proceed_key, (screen_width/2 - proceed_key.get_width() // 2, screen_height * 5/6 - proceed_key.get_height() // 2))
        elif game_mode == 2:
            screen.blit(key_1, (screen_width/2 - key_1.get_width() // 2, screen_height /10 - key_1.get_height() // 2))
            screen.blit(key_2, (screen_width/2 - key_2.get_width() // 2, screen_height *2/10 - key_2.get_height() // 2))
            screen.blit(key_3, (screen_width/2 - key_3.get_width() // 2, screen_height *8/10 - key_3.get_height() // 2))
            screen.blit(key_4, (screen_width/2 - key_4.get_width() // 2, screen_height *9/10 - key_4.get_height() // 2))
            screen.blit(key_5, (screen_width/2 - key_5.get_width() // 2, screen_height *1/2 - key_5.get_height()*2))
            screen.blit(key_6, (screen_width/2 - key_6.get_width() // 2, screen_height *1/2 - key_6.get_height() // 2))
            screen.blit(proceed_key, (screen_width/2 - proceed_key.get_width() // 2, screen_height * 1/2 + proceed_key.get_height()))


        pygame.display.flip()
        clock.tick(60)


def gameplay(game_mode):

    singleplayer = (game_mode == 1)
    multiplayer = (game_mode == 2)

    pygame.mixer.init()

    screen_width = 1000
    screen_height = 800
    done = False

    # LOAD SOUNDS
    sound_shot = pygame.mixer.Sound('assets/shot.wav')


    # BARS
    class Bar:
        def __init__ (self, x, y, width, height, speed):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.speed = speed

    bar1 = Bar(30, 0, 150, 20, 20)
    bar2 = Bar(30, screen_height-20, 150, 20, 20)


    # BALLS
    class Ball:
        def __init__(self, ball_width, ball_height, ball_x, ball_y, ball_vert_direction, ball_horiz_direction, ball_speed_horiz, ball_speed_vert, ball_hits):
            self.width = ball_width
            self.height = ball_height
            self.x = ball_x
            self.y = ball_y
            self.vert_direction = ball_vert_direction; # By default ball goes up
            self.horiz_direction = ball_horiz_direction; # By default ball goes right
            self.speed_horiz = ball_speed_horiz
            self.speed_vert = ball_speed_vert
            self.hits = ball_hits # Number of times the main ball hits any BAR (as the number goes up, game becomes harder)

    ball_w = 20
    ball_h = 20
    direction= [-1,1]
    ball1 = Ball(ball_w, ball_h, (screen_width / 2) - ball_w, (screen_height/2) - ball_h/2, random.choice(direction), random.choice(direction), 12, 6, 0)
    ball_hit_bar = False

    # SHOTS
    class Shot:
        def __init__(self, is_fired, x, y, width, height, speed):
            self.is_fired = is_fired
            self.x = x        
            self.y = y
            self.width = width
            self.height = height
            self.speed = speed

    shot1 = Shot(False, 0, bar1.y+bar1.height, 5, 8, 10)
    shot2 = Shot(False, 0, bar2.y, 5, 8, 10)

    # POWERS
    class Power:
        def __init__ (self, name, x, y, speed):
            self.name = name
            self.x = x
            self.y = y
            self.speed = speed

    # CURRENT POWERS
    enlarge = Power ('enlarge', random.randint(50, screen_width-50), screen_height/2, 5)
    shrink = Power ('shrink', random.randint(50, screen_width-50), screen_height/2, 5)
    missile = Power ('missile', random.randint(50, screen_width-50), screen_height/2, 5)

    power_available = False
    power_width = 30
    power_height = 30
    powers = ['enlarge', 'shrink', 'missile']
    active_power = ''


    first_ball = True
    second_ball = False
    game_start=False


    font = pygame.font.SysFont("comicsansms", 72)

    # SCORE BOARD
    game_over = False
    score_1 = "0"
    score_2 = "0"
    if multiplayer:
        win_text1 = font.render("Player 1 WON", True, (0, 128, 0))
        win_text2 = font.render("Player 2 WON", True, (0, 128, 0))
    elif singleplayer:
        win_text1 = font.render("You WON", True, (0, 128, 0))
        win_text2 = font.render("You LOST", True, (0, 128, 0))


    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_start = True
                if (first_ball == False):
                    ball1 = Ball(ball_w, ball_h, (screen_width / 2) - ball_w, (screen_height/2) - ball_h, 1, 1, 12, 7, 0)
                first_ball = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_l:
                second_ball = True
                ball2 = Ball(ball_w, ball_h, (screen_width / 2) - ball_w + 100, (screen_height/2) - ball_h, -1, -1, 8, 11,0)

        pressed = pygame.key.get_pressed()

        # PLAYER 1 KEYS (ARROWS)
        if pressed[pygame.K_LEFT]: 
            if bar1.x > bar1.speed:
                bar1.x -= bar1.speed
        if pressed[pygame.K_RIGHT]: 
            if bar1.x < screen_width - (bar1.width + bar1.speed):
                bar1.x += bar1.speed
            
        # PLAYER 2 KEYS (Z and X)
        if (multiplayer):
            if pressed[pygame.K_z]: 
                if bar2.x > bar2.speed:
                    bar2.x -= bar2.speed
            if pressed[pygame.K_x]: 
                if bar2.x < screen_width - (bar2.width + bar2.speed):
                    bar2.x += bar2.speed
        
        # SHOT 1
        if pressed[pygame.K_DOWN]: 
            if shot1.is_fired == False:
                sound_shot.play()
                shot1.is_fired = True
                shot1.x = bar1.x+bar1.width/2
        
        # SHOT 2
        if pressed[pygame.K_c]: 
            if shot2.is_fired == False:
                sound_shot.play()
                shot2.is_fired = True
                shot2.x = bar2.x+bar2.width/2

        # AI
        if (singleplayer):
            if(game_start):
                if ball1.vert_direction==-1:
                    if bar2.x+bar2.width < ball1.x:  
                        bar2.x += bar2.speed
                    elif bar2.x > ball1.x:
                        bar2.x -= bar2.speed
                else:
                    if bar2.x+bar2.width < screen_width/2:
                        bar2.x += bar2.speed/2
                    elif bar2.x > screen_width/2:
                        bar2.x -= bar2.speed/2



        # COLLISION DETECTION
        # BALL 1
        if (first_ball):
            if (ball1.x < bar1.x + bar1.width and ball1.x+ball1.width > bar1.x and ball1.y > bar1.y+bar1.height-ball1.speed_vert and ball1.y <= bar1.y+bar1.height):
                ball1.vert_direction *= -1
                ball1.hits +=1
                ball1.speed_vert += ball1.hits/5
                ball_hit_bar = True
            elif (ball1.x < bar2.x + bar2.width and ball1.x+ball1.width > bar2.x and ball1.y+ball1.height >= bar2.y and ball1.y+ball1.height < bar2.y+ball1.speed_vert):
                ball1.vert_direction *= -1
                ball1.hits +=1
                ball1.speed_vert += ball1.hits/5
                ball_hit_bar = True
            if (ball1.x <= 0 or ball1.x >= screen_width-ball1.width): #ball1 - walls
                ball1.horiz_direction *= -1

            # DETECT BALL OUT OF SCREEN
            if (ball1.y > screen_height or ball1.y+ball1.height < 0):
                if ball1.y > screen_height:
                    score_1 = add_score(score_1)
                if ball1.y+ball1.height < 0:
                    score_2 = add_score(score_2)

                first_ball = False
                game_start = False
                del ball1
                ball1 = Ball(ball_w, ball_h, (screen_width / 2) - ball_w, (screen_height/2) - ball_h/2, 1, 1, 12, 7,0)
                first_ball = True


        # BALL TRAJECTORY
        if game_start:
            ball1.y -= (ball1.speed_vert) * ball1.vert_direction
            ball1.x -= ball1.speed_horiz * ball1.horiz_direction


        # POWER-UP GENERATION (RANDOM)
        if (ball1.hits%3 == 1 and power_available == False and ball_hit_bar):
            ball_hit_bar = False
            power_available = True
            active_power = random.choice(powers)
            enlarge.y -= enlarge.speed * random.choice(direction)
            shrink.y -= shrink.speed * random.choice(direction)
            missile.y -= missile.speed * random.choice(direction)


        # COLLISION DETECTION FOR POWERS
        if (power_available):
            if active_power == 'enlarge':
                if enlarge.y > bar1.y+bar1.height-enlarge.speed and enlarge.y <= bar1.y+bar1.height:
                    power_available = False
                    if (enlarge.x < bar1.x + bar1.width and enlarge.x+power_width > bar1.x):
                        bar1.width += 50
                        enlarge.x = random.randint(50, screen_width-50)
                        enlarge.y = screen_height/2
                elif enlarge.y+power_height >= bar2.y and enlarge.y+power_height < bar2.y+enlarge.speed:
                    power_available = False
                    if enlarge.x < bar2.x + bar2.width and enlarge.x+power_width > bar2.x: 
                        bar2.width += 50
                        enlarge.x = random.randint(50, screen_width-50)
                        enlarge.y = screen_height/2

            elif active_power == 'shrink':
                if shrink.y > bar1.y+bar1.height-shrink.speed and shrink.y <= bar1.y+bar1.height:
                    power_available = False             
                    if (shrink.x < bar1.x + bar1.width and shrink.x+power_width > bar1.x):
                        bar1.width -= 50
                        shrink.x = random.randint(50, screen_width-50)
                        shrink.y = screen_height/2
                elif shrink.y+power_height >= bar2.y and shrink.y+power_height < bar2.y+shrink.speed:
                    power_available = False
                    if shrink.x < bar2.x + bar2.width and shrink.x+power_width > bar2.x: 
                        bar2.width += 50
                        shrink.x = random.randint(50, screen_width-50)
                        shrink.y = screen_height/2

            elif active_power == 'missile':
                if missile.y > bar1.y+bar1.height-missile.speed and missile.y <= bar1.y+bar1.height:
                    power_available = False
                    if (missile.x < bar1.x + bar1.width and missile.x+power_width > bar1.x):
                        shot1.height += 80
                        missile.x = random.randint(50, screen_width-50)
                        missile.y = screen_height/2
                elif missile.y+power_height >= bar2.y and missile.y+power_height < bar2.y+missile.speed:
                    power_available = False
                    if missile.x < bar2.x + bar2.width and missile.x+power_width > bar2.x: 
                        bar2.width += 50
                        missile.x = random.randint(50, screen_width-50)
                        missile.y = screen_height/2



        # COLLISION DETECTION
        # BALL 2
        if (second_ball):
            if (ball2.x < bar1.x + bar1.width and ball2.x+ball2.width > bar1.x and ball2.y > bar1.y+bar1.height-10 and ball2.y <= bar1.y+bar1.height):
                ball2.vert_direction *= -1
            if (ball2.x < bar2.x + bar2.width and ball2.x+ball2.width > bar2.x and ball2.y+ball2.height >= bar2.y and ball2.y+ball2.height < bar2.y+10 ):
                ball2.vert_direction *= -1
            if (ball2.x <= 0 or ball2.x >= screen_width-ball2.width):
                ball2.horiz_direction *= -1
            ball2.y -= ball2.speed_vert * ball2.vert_direction
            ball2.x -= ball2.speed_horiz * ball2.horiz_direction

            # DETECT BALL OUT OF SCREEN
            if (ball2.y > screen_height or ball2.y+ball2.height < 0):
                if ball2.y > screen_height:
                    score_1 = add_score(score_1)
                if ball2.y+ball2.height < 0:
                    score_2 = add_score(score_2)

                second_ball = False
                del ball2


        # SHOT 1
        if shot1.is_fired:
            shot1.y += shot1.speed
            if shot1.y+shot1.height >= screen_height - bar2.height:
                if shot1.x >= bar2.x and shot1.x <= bar2.x+bar2.width:
                    score_1 = add_score(score_1)
                shot1.y = bar1.y+bar1.height
                shot1.is_fired = False

        # SHOT 2
        if shot2.is_fired:
            shot2.y -= shot2.speed
            if shot2.y <= 0:
                if shot2.x >= bar1.x and shot2.x <= bar1.x+bar1.width:
                    score_2 = add_score(score_2)
                shot2.y = bar2.y
                shot2.is_fired = False


        # CLEAR SCREEN
        screen.fill((255, 255, 255))
        
        # DRAW FIELD
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, screen_height/2-1, screen_width, 2))

        # Detect if game is over
        if is_game_over(score_1) == True:
            screen.blit(win_text1, (screen_width/2 - win_text1.get_width() // 2, screen_height / 2 - win_text1.get_height() // 2))
        
        elif is_game_over(score_2) == True:
            screen.blit(win_text2, (screen_width/2 - win_text2.get_width() // 2, screen_height / 2 - win_text2.get_height() // 2))

        else:
            # DRAW SCORES
            text1 = font.render(score_1, True, (0, 128, 0))
            text2 = font.render(score_2, True, (0, 128, 0))
            screen.blit(text1, (screen_width*7/8 - text1.get_width() // 8, screen_height / 4 - text1.get_height() // 2))
            screen.blit(text2, (screen_width*7/8 - text2.get_width() // 8, screen_height * 3/4 - text2.get_height() // 2))

            # DRAW BALLS
            if (first_ball):
                screen.blit(get_image('assets/green_ball.png'), (ball1.x, ball1.y))
            if (second_ball):
                screen.blit(get_image('assets/green_ball.png'), (ball2.x, ball2.y))

            # DRAW POWERS
            if power_available:
                if active_power == 'enlarge':
                    screen.blit(get_image('assets/enlarge.png'), (enlarge.x, enlarge.y))
                    enlarge.y -= enlarge.speed
                elif active_power == 'shrink':
                    screen.blit(get_image('assets/shrink.png'), (shrink.x, shrink.y))
                    shrink.y -= shrink.speed
                if active_power == 'missile':
                    screen.blit(get_image('assets/missile.png'), (missile.x, missile.y))
                    missile.y -= missile.speed

            # DRAW BARS
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(bar1.x, bar1.y, bar1.width, bar1.height))
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(bar2.x, bar2.y, bar2.width, bar2.height))

            # DRAW SHOT 1
            if shot1.is_fired:
                pygame.draw.rect(screen, (128, 0, 0), pygame.Rect(shot1.x, shot1.y, shot1.width, shot1.height))
            # DRAW SHOT 2
            if shot2.is_fired:
                pygame.draw.rect(screen, (128, 0, 0), pygame.Rect(shot2.x, shot2.y, shot2.width, shot2.height))


        pygame.display.flip()
        clock.tick(60)

main()        