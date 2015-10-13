import pygame
import os
import random
import math

_image_library = {}


def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path).convert_alpha()
        _image_library[path] = image
    return image


def show_info(font, screen, screen_width, screen_height, teta, vi, wind):

    angle = font.render("teta : " + str(teta), True, (255, 255, 255))
    power = font.render("power : " + str(vi), True, (255, 255, 255))
    wind = font.render("wind : " + str(wind), True, (255, 255, 255))

    if(teta == 90):
        angle = font.render("teta : " + "max", True, (255, 255, 255))
    elif(teta == 0):
        angle = font.render("teta : " + "min", True, (255, 255, 255))

    if(vi == 30):
        power = font.render("power : " + "max", True, (255, 255, 255))
    elif(vi == 0):
        power = font.render("power : " + "min", True, (255, 255, 255))

    screen.blit(angle, (screen_width / 2 - angle.get_width() //
                        2, screen_height / 7 - angle.get_height() // 2))
    screen.blit(power, (screen_width / 2 - angle.get_width() //
                        2, screen_height / 5 - power.get_height() // 2))
    screen.blit(wind, (screen_width / 2 - angle.get_width() //
                        2, screen_height / 5 + wind.get_height() ))


def winner(font, screen, screen_width, screen_height,opc):

    winner1 = font.render("Left Tank Wins" , True, (255, 255, 255))
    winner2 = font.render("Right Tank Wins" , True, (255, 255, 255))

    if(opc==1):
        screen.blit(winner1, (screen_width / 2 - winner1.get_width() //
                        2, screen_height / 2 - winner1.get_height() // 2))
    else:
        screen.blit(winner2, (screen_width / 2 - winner2.get_width() //
                        2, screen_height / 2 - winner2.get_height() // 2))

    pygame.display.flip()




def change_values(teta, vi):
    """Update projectile velocity in both directions"""
    viy = -vi * math.sin(math.radians(teta))
    vix = vi * math.cos(math.radians(teta))
    return [vix, viy]


def missile_initial_pos(teta, tank, left_tank_turn):
    """Determines the initial position of the missile"""
    center_x = tank.x + tank.width / 2
    center_y = tank.y + tank.height / 2
    radius = tank.height / 2

    if left_tank_turn == True:
        x = center_x + math.cos(math.radians(teta)) * radius
        y = center_y - math.sin(math.radians(teta)) * radius
    else:
        # 10 is the missile width
        x = center_x - math.cos(math.radians(teta)) * radius - 10
        y = center_y - math.sin(math.radians(teta)) * radius

    return [x, y]


def gameplay():
    """Main function of the game"""
    screen_width = 600
    screen_height = 460
    done = False

    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Tanky")
    clock = pygame.time.Clock()

    # LOAD MUSIC / SOUND EFFECTS
    battle_music=pygame.mixer.music.load('assets/battle.mp3')
    win=pygame.mixer.Sound('assets/win.wav')
    shooting=pygame.mixer.Sound('assets/cannon.wav')
    explosion=pygame.mixer.Sound('assets/explosion.wav')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1, 0.0)

#-- BACKGROUND
    # DUNES (EARTH) -- 827x358
    dunes_img = get_image('assets/dunes.png')
    dunes_height = 358
    # JUPITER -- 640x480
    jupiter_img = get_image('assets/jupiter.png')
    jupiter_width = 640
    jupiter_height = 480
    # CLOUDS -- 32x31
    cloud_img = get_image('assets/cloud.png')
    cloud_width = 32
    # TOWER -- 50x130
    tower_img = get_image('assets/tower.png')
    tower_width = 50
    tower_height = 130
    tower_x = screen_width/2 - tower_width/2
    tower_y = screen_height - tower_height
#--

    # WIND (only affects speed on xx)
    wind = random.randint(-8, 8)

#-- TANK VARIABLES

    left_tank_img0 = get_image('assets/left_tank/0.png')
    left_tank_img5 = get_image('assets/left_tank/5.png')
    left_tank_img10 = get_image('assets/left_tank/10.png')
    left_tank_img15 = get_image('assets/left_tank/15.png')
    left_tank_img20 = get_image('assets/left_tank/20.png')
    left_tank_img25 = get_image('assets/left_tank/25.png')
    left_tank_img30 = get_image('assets/left_tank/30.png')
    left_tank_img35 = get_image('assets/left_tank/35.png')
    left_tank_img40 = get_image('assets/left_tank/40.png')
    left_tank_img45 = get_image('assets/left_tank/45.png')
    left_tank_img50 = get_image('assets/left_tank/50.png')
    left_tank_img55 = get_image('assets/left_tank/55.png')
    left_tank_img60 = get_image('assets/left_tank/60.png')
    left_tank_img65 = get_image('assets/left_tank/65.png')
    left_tank_img70 = get_image('assets/left_tank/70.png')
    left_tank_img75 = get_image('assets/left_tank/75.png')
    left_tank_img80 = get_image('assets/left_tank/80.png')
    left_tank_img85 = get_image('assets/left_tank/85.png')
    left_tank_img90 = get_image('assets/left_tank/90.png')
    left_tank_imge = [left_tank_img0, left_tank_img5, left_tank_img10, left_tank_img15, left_tank_img20, left_tank_img25, left_tank_img30, left_tank_img35, left_tank_img40,
                      left_tank_img45, left_tank_img50, left_tank_img55, left_tank_img60, left_tank_img65, left_tank_img70, left_tank_img75, left_tank_img80, left_tank_img85, left_tank_img90]
    left_tank_img = left_tank_imge[9]

    right_tank_img0 = get_image('assets/right_tank/0.png')
    right_tank_img5 = get_image('assets/right_tank/5.png')
    right_tank_img10 = get_image('assets/right_tank/10.png')
    right_tank_img15 = get_image('assets/right_tank/15.png')
    right_tank_img20 = get_image('assets/right_tank/20.png')
    right_tank_img25 = get_image('assets/right_tank/25.png')
    right_tank_img30 = get_image('assets/right_tank/30.png')
    right_tank_img35 = get_image('assets/right_tank/35.png')
    right_tank_img40 = get_image('assets/right_tank/40.png')
    right_tank_img45 = get_image('assets/right_tank/45.png')
    right_tank_img50 = get_image('assets/right_tank/50.png')
    right_tank_img55 = get_image('assets/right_tank/55.png')
    right_tank_img60 = get_image('assets/right_tank/60.png')
    right_tank_img65 = get_image('assets/right_tank/65.png')
    right_tank_img70 = get_image('assets/right_tank/70.png')
    right_tank_img75 = get_image('assets/right_tank/75.png')
    right_tank_img80 = get_image('assets/right_tank/80.png')
    right_tank_img85 = get_image('assets/right_tank/85.png')
    right_tank_img90 = get_image('assets/right_tank/90.png')
    right_tank_imge = [right_tank_img0, right_tank_img5, right_tank_img10, right_tank_img15, right_tank_img20, right_tank_img25, right_tank_img30, right_tank_img35, right_tank_img40,
                       right_tank_img45, right_tank_img50, right_tank_img55, right_tank_img60, right_tank_img65, right_tank_img70, right_tank_img75, right_tank_img80, right_tank_img85, right_tank_img90]
    right_tank_img = right_tank_imge[9]

    life_img1 = get_image('assets/life/1.png')
    life_img2 = get_image('assets/life/2.png')
    life_img3 = get_image('assets/life/3.png')
    life_img = [life_img1, life_img2, life_img3]

    class Tank:

        def __init__(self, x, y, width, height, speed, damage):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.speed = speed
            self.damage = damage

    # TANK.PNG DIMENSIONS: 50x50
    tank_width = 50
    tank_height = 50
    tank_speed = 7
    left_tank_turn = True   # Left tank starts the game

    left_tank = Tank(
        40, screen_height - tank_height, tank_width, tank_height, tank_speed, 0)
    right_tank = Tank(screen_width - 40 - tank_width, screen_height -
                      tank_height, tank_width, tank_height, tank_speed, 0)
#--

#-- GENERATE 5 CLOUDS FOR BACKGROUND (RANDOMLY PLACED)

    clouds = []
    for i in range(0, 5):
        cloud = [
            random.randrange(0, screen.get_width() - 1), random.randrange(0, 150)]
        clouds.append(cloud)
#--


#-- MISSILE
    class Missile:

        def __init__(self, x, y):
            self.x = x
            self.y = y

    missile_img0000 = get_image('assets/cannonball.png')

    missile_max_speed = 30
    t = 0
    vi = missile_max_speed
    vi2 = missile_max_speed
    teta = 45
    teta2 = 45
    viy = -vi * math.sin(math.radians(teta))
    viy2 = -vi2 * math.sin(math.radians(teta2))
    vfy2 = 0
    vix = vi * math.cos(math.radians(teta))
    vix2 = -vi2 * math.cos(math.radians(teta2))
    vfx = vix
    vfx2 = vix2
    ax = 0
    gravity = 1
    ay = 9.8*gravity
    shoot = False

    missile = Missile(left_tank.x + left_tank.width, screen_height - 20)

#--

#-- EXPLOSION
    explosion_img0 = get_image('assets/explosion/explosion_1.png')
    explosion_img1 = get_image('assets/explosion/explosion_2.png')
    explosion_img2 = get_image('assets/explosion/explosion_3.png')
    explosion_img3 = get_image('assets/explosion/explosion_4.png')
    explosion_img4 = get_image('assets/explosion/explosion_5.png')
    explosion_img5 = get_image('assets/explosion/explosion_6.png')
    explosion_img6 = get_image('assets/explosion/explosion_7.png')
    explosion_img7 = get_image('assets/explosion/explosion_8.png')
    explosion_img8 = get_image('assets/explosion/explosion_9.png')
    explosion_img9 = get_image('assets/explosion/explosion_10.png')
    explosion_img10 = get_image('assets/explosion/explosion_11.png')
    explosion_img = [explosion_img0, explosion_img1, explosion_img2, explosion_img3, explosion_img4,
                     explosion_img5, explosion_img6, explosion_img7, explosion_img8, explosion_img9, explosion_img10]
    collison_r = False
    collison_l = False
    collision_tower = False
    explosion_index = 0
#--

    font = pygame.font.SysFont("comicsansms", 20)
    font2 = pygame.font.SysFont("comicsansms", 50)

    # CREATING MASKS FOR MISSILE AND TANKS
    r_tank_mask = pygame.mask.from_surface(right_tank_img)
    l_tank_mask = pygame.mask.from_surface(left_tank_img)
    missile_mask = pygame.mask.from_surface(missile_img0000)
    tower_mask = pygame.mask.from_surface(tower_img)


    # Game background: 1 - Earth (default); 2 - Jupiter; 3 - Moon
    background = 1

    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_1]: #CHANGE BACKGROUND TO EARTH
            background = 1

        elif pressed[pygame.K_2]: #CHANGE BACKGROUND TO JUPITER
            background = 2

        elif pressed[pygame.K_LEFT] and not shoot:     # MOVE LEFT
            if left_tank_turn == True:
                if left_tank.x > 0 + left_tank.speed:
                    left_tank.x -= left_tank.speed
            else:
                if right_tank.x > screen_width/2 + tower_width/2 + right_tank.speed:
                    right_tank.x -= right_tank.speed

        elif pressed[pygame.K_RIGHT] and not shoot:  # MOVE RIGHT
            if left_tank_turn == True:
                if (left_tank.x + left_tank.width) < screen_width/2 - tower_width/2 - left_tank.speed:
                    left_tank.x += left_tank.speed
            else:
                if right_tank.x + right_tank.width < screen_width - right_tank.speed:
                    right_tank.x += right_tank.speed

        elif pressed[pygame.K_UP] and not shoot:  # ANGLE ++
            if left_tank_turn == True:
                if(teta < 90):
                    teta += 5
                [vix, viy] = change_values(teta, vi)
                left_tank_img = left_tank_imge[teta / 5]
                tank_mask_l = pygame.mask.from_surface(
                    left_tank_img)  # UPDATE MASK

            else:
                if(teta2 < 90):
                    teta2 += 5
                [vix2, viy2] = change_values(teta2, vi2)
                vix2 *= -1
                right_tank_img = right_tank_imge[teta2 / 5]
                tank_mask_r = pygame.mask.from_surface(
                    right_tank_img)  # UPDATE MASK

        elif pressed[pygame.K_DOWN] and not shoot:  # ANGLE --
            if left_tank_turn == True:
                if(teta > 0):
                    teta -= 5
                [vix, viy] = change_values(teta, vi)
                left_tank_img = left_tank_imge[teta / 5]
                tank_mask_l = pygame.mask.from_surface(
                    left_tank_img)  # UPDATE MASK

            else:
                if(teta2 > 0):
                    teta2 -= 5
                [vix2, viy2] = change_values(teta2, vi2)
                vix2 *= -1
                right_tank_img = right_tank_imge[teta2 / 5]
                tank_mask_r = pygame.mask.from_surface(
                    right_tank_img)  # UPDATE MASK

        elif pressed[pygame.K_SPACE] and not shoot:  # SHOOT
            # DETECT MISSILE INITIAL POSITION
            if left_tank_turn == True:
                [missile_x, missile_y] = missile_initial_pos(
                    teta, left_tank, left_tank_turn)
            else:
                [missile_x, missile_y] = missile_initial_pos(
                    teta2, right_tank, left_tank_turn)

            missile = Missile(missile_x, missile_y)

            shoot = True
            shooting.play()

        elif pressed[pygame.K_z] and not shoot:  # POWER --
            if left_tank_turn == True:
                if(vi > 0):
                    vi -= 0.2
                [vix, viy] = change_values(teta, vi)
            else:
                if(vi2 > 0):
                    vi2 -= 0.2
                [vix2, viy2] = change_values(teta2, vi2)
                vix2 *= -1

        elif pressed[pygame.K_x] and not shoot:  # POWER ++
            if left_tank_turn == True:
                if(vi < missile_max_speed):
                    vi += 0.2
                [vix, viy] = change_values(teta, vi)
            else:
                if(vi2 < missile_max_speed):
                    vi2 += 0.2
                [vix2, viy2] = change_values(teta2, vi2)
                vix2 *= -1

    #-- MOVE CLOUDS
        # IF ANY CLOUD LEAVES THE SCREEN, ANOTHER ONE IS GENERATED
        for i in range(0, 5):
            if clouds[i][0] + cloud_width <= 0:
                clouds[i] = [screen_width, random.randrange(0, 150)]
            # MOVE CLOUDS
            else:
                clouds[i][0] -= 0.5
    #--

    #-- MOVE MISSILE
        if(shoot == True and (missile.y <= screen_height)):
            t += (1 / float(60))
            if left_tank_turn == True:
                vfy = viy + ay * t
                vfx = vix
                missile.x += vfx * t + 0.5 * wind * (t * t)
                missile.y += vfy * t + 0.5 * ay * (t * t)
            else:
                vfy2 = viy2 + ay * t
                vfx2 = vix2
                missile.x += vfx2 * t + 0.5 * wind * (t * t)
                missile.y += vfy2 * t + 0.5 * ay * (t * t)
        elif (missile.y > screen_height or collison_r or collison_l or collision_tower): #CHANGE TURN

            # GENERATE NEW WIND
            wind =random.randint(-8, 8)

            if(left_tank_turn == False):
                left_tank_turn = True
                missile = Missile(
                    left_tank.x + left_tank.width, screen_height - 20)

            else:
                left_tank_turn = False
                missile = Missile(right_tank.x, screen_height - 20)

            collision_tower=False

            shoot = False
            t = 0
    #--

        screen.fill((220, 214, 186))  # background color

    #-- DRAW OUR STUFF
        if background == 1: #dunes
            screen.blit(dunes_img, (0, screen_height - dunes_height))
            gravity = 1
        elif background == 2: #jupiter
            screen.blit(jupiter_img, (0, screen_height - jupiter_height))
            gravity = 2.54
        
        # TOWER
        screen.blit(tower_img, (screen_width/2 - tower_width/2, screen_height - tower_height))

        # CLOUDS
        for j in range(0, 5):
            screen.blit(cloud_img, clouds[j])

        # MISSILE
        if(shoot == True):
            if missile.y <= screen_height:
                #-- DETECT MISSILE ANGLE
                screen.blit(missile_img0000, (missile.x, missile.y))
            #--
        # TANKS

        if(not collison_l and left_tank.damage < 3):
            screen.blit(
                life_img[left_tank.damage], (left_tank.x + 5, left_tank.y + 15))
            screen.blit(left_tank_img, (left_tank.x, left_tank.y))
        else:
            if (explosion_index < 11) and (left_tank.damage > 2):
                if(explosion_index==0):
                    pygame.mixer.music.stop()
                    explosion.play()                
                pygame.display.flip()
                screen.blit(explosion_img[explosion_index], (left_tank.x - 20, left_tank.y - 25))
                explosion_index += 1
            elif(explosion_index>=10 and not pygame.mixer.get_busy() ):
                winner(font2, screen, screen_width, screen_height,2)
                win.play()
                pygame.time.wait(1700)
                done=True                
            else:
                left_tank.damage += 1
                collison_l = False

        if(not collison_r and right_tank.damage < 3):
            screen.blit(life_img[right_tank.damage], (right_tank.x + 5, right_tank.y + 15))
            screen.blit(right_tank_img, (right_tank.x, right_tank.y))
        else:
            if explosion_index < 11 and right_tank.damage > 2:
                if(explosion_index==0):
                    pygame.mixer.music.stop()
                    explosion.play()
                pygame.display.flip()
                screen.blit(explosion_img[explosion_index], (right_tank.x - 20, right_tank.y - 25))
                explosion_index+=1
            elif(explosion_index>=10 and not pygame.mixer.get_busy() ):
                winner(font2, screen, screen_width, screen_height,1)
                win.play()
                pygame.time.wait(1700)
                done=True 
            else:
                right_tank.damage += 1
                collison_r = False

    #--

    # DETECT MISSILE COLLISION
        if(shoot):
            if(left_tank_turn == True):
                offset_tank_x, offset_tank_y = (
                    int(right_tank.x) - int(missile.x)), (int(right_tank.y) - int(missile.y))
                offset_tower_x, offset_tower_y = (
                    int(tower_x) - int(missile.x)), (int(tower_y) - int(missile.y))
                offset_tank_s_x, offset_tank_s_y = (
                    int(left_tank.x) - int(missile.x)), (int(left_tank.y) - int(missile.y))
                
                if (missile_mask.overlap(r_tank_mask, (offset_tank_x, offset_tank_y)) != None):
                    collison_r = True
                    shoot = False
                elif (missile_mask.overlap(tower_mask, (offset_tower_x, offset_tower_y)) != None):
                    collision_tower = True
                    shoot = False
                elif (missile_mask.overlap(l_tank_mask, (offset_tank_s_x, offset_tank_s_y)) != None):
                    collison_l = True
                    shoot = False
            else:
                offset_tank_x, offset_tank_y = (
                    int(left_tank.x) - int(missile.x)), (int(left_tank.y) - int(missile.y))
                offset_tower_x, offset_tower_y = (
                    int(tower_x) - int(missile.x)), (int(tower_y) - int(missile.y))
                offset_tank_s_x, offset_tank_s_y = (
                    int(right_tank.x) - int(missile.x)), (int(right_tank.y) - int(missile.y))
                if (missile_mask.overlap(r_tank_mask, (offset_tank_x, offset_tank_y)) != None):
                    collison_l = True
                    shoot = False
                elif (missile_mask.overlap(tower_mask, (offset_tower_x, offset_tower_y)) != None):
                    collision_tower = True
                    shoot = False
                elif (missile_mask.overlap(r_tank_mask, (offset_tank_s_x, offset_tank_s_y)) != None):
                    collison_r = True
                    shoot = False


        if(left_tank_turn == False):
            show_info(font, screen, screen_width, screen_height, teta2, vi2, wind)
        else:
            show_info(font, screen, screen_width, screen_height, teta, vi, wind)

        pygame.display.flip()
        clock.tick(60)
    #--

gameplay()
