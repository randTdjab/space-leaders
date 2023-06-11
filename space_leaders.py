import pygame
import random

# window things
pygame.init()
win = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Space Leaders")
# window things


# the images
background = pygame.image.load("scd_p_img/-bg.png")
alien_ship = pygame.image.load("scd_p_img/ships/alien_ship.png")
bullet_i = [pygame.image.load("scd_p_img/-bullets/slim/-b1.png"), pygame.image.load("scd_p_img/-bullets/slim/-b2.png"),
            pygame.image.load("scd_p_img/-bullets/slim/-b3.png"), pygame.image.load("scd_p_img/-bullets/slim/-b4.png"),
            pygame.image.load("scd_p_img/-bullets/slim/-b5.png"), pygame.image.load("scd_p_img/-bullets/slim/-b6.png"),
            pygame.image.load("scd_p_img/-bullets/slim/-b7.png"),
            pygame.image.load("scd_p_img/-bullets/slim/-b8.png"), ]
asteroids = pygame.image.load("scd_p_img/enemies/asteroids.png")
main_menu_background = pygame.image.load("scd_p_img/main_menu/main_menu_bg.png")
main_menu_play_button = pygame.image.load("scd_p_img/main_menu/play_button.png")
main_menu_play_button_h = pygame.image.load("scd_p_img/main_menu/play_button_h.png")
game_logo = [pygame.image.load("scd_p_img/main_menu/game_logo_t/game_logo1.png"),
             pygame.image.load("scd_p_img/main_menu/game_logo_t/game_logo2.png"),
             pygame.image.load("scd_p_img/main_menu/game_logo_t/game_logo3.png"),
             pygame.image.load("scd_p_img/main_menu/game_logo_t/game_logo4.png"),
             pygame.image.load("scd_p_img/main_menu/game_logo_t/game_logo5.png"),
             pygame.image.load("scd_p_img/main_menu/game_logo_t/game_logo6.png"),
             pygame.image.load("scd_p_img/main_menu/game_logo_t/game_logo7.png"),
             pygame.image.load("scd_p_img/main_menu/game_logo_t/game_logo8.png"),
             pygame.image.load("scd_p_img/main_menu/game_logo_t/game_logo9.png"),
             pygame.image.load("scd_p_img/main_menu/game_logo_t/game_logo10.png"),
             pygame.image.load("scd_p_img/main_menu/game_logo_t/game_logo11.png"),
             pygame.image.load("scd_p_img/main_menu/game_logo_t/game_logo12.png"),
             pygame.image.load("scd_p_img/main_menu/game_logo_t/game_logo13.png"),
             pygame.image.load("scd_p_img/main_menu/game_logo_t/game_logo14.png"),
             pygame.image.load("scd_p_img/main_menu/game_logo_t/game_logo15.png"),
             pygame.image.load("scd_p_img/main_menu/game_logo_t/game_logo16.png"),
             pygame.image.load("scd_p_img/main_menu/game_logo_t/game_logo17.png"),
             pygame.image.load("scd_p_img/main_menu/game_logo_t/game_logo18.png"),
             pygame.image.load("scd_p_img/main_menu/game_logo_t/game_logo19.png"),
             pygame.image.load("scd_p_img/main_menu/game_logo_t/game_logo20.png"),
             pygame.image.load("scd_p_img/main_menu/game_logo_t/game_logo21.png"),
             pygame.image.load("scd_p_img/main_menu/game_logo_t/game_logo22.png"),
             pygame.image.load("scd_p_img/main_menu/game_logo_t/game_logo23.png"),
             pygame.image.load("scd_p_img/main_menu/game_logo_t/game_logo24.png")
             ]
main_menu_shop_button = pygame.image.load("scd_p_img/main_menu/shop_button.png")
main_menu_shop_button_h = pygame.image.load("scd_p_img/main_menu/shop_button_h.png")
shop_lock = pygame.image.load("scd_p_img/main_menu/lock.png")
alien_ship_frame = pygame.image.load("scd_p_img/main_menu/ship_frames/alien_sh_f.png")
back_sign = pygame.image.load("scd_p_img/back_arrow.png")
back_sign_h = pygame.image.load("scd_p_img/back_arrow_h.png")
pause_sign = pygame.image.load("scd_p_img/pause.png")
pause_sign_h = pygame.image.load("scd_p_img/pause_h.png")
pause_menu = pygame.image.load("scd_p_img/pause_menu.png")
pause_menu_r = pygame.image.load("scd_p_img/pause_menu_r.png")
pause_menu_e = pygame.image.load("scd_p_img/pause_menu_e.png")
war_plane = pygame.image.load("scd_p_img/ships/war_plane.png")
war_plane_bullet = pygame.image.load("scd_p_img/-bullets/war_plane_bullet.png")
# the images
# sound effects
slim_bullet_sound = pygame.mixer.Sound("scd_p_img/mu_so/p.mp3")

# sound effects
# global variables
the_player = alien_ship


# global varibles
# classes
class Player(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 10

    def draw_space_ship(self):
        win.blit(the_player, (self.x, self.y))


class Bullet(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 6

    def draw_bullet(self):
        global slim_animation_count
        if the_player == alien_ship:
            if slim_animation_count >= 24:
                slim_animation_count = 0
            win.blit(bullet_i[slim_animation_count // 3], (self.x, self.y))
            slim_animation_count += 1
        elif the_player == war_plane:
            win.blit(war_plane_bullet, (self.x, self.y))


class Enemy(object):
    def __init__(self, x, enemy_type, speed):
        self.x = x
        self.y = 0
        self.speed = speed
        self.enemy_type = enemy_type

    def draw_enemy(self):
        win.blit(self.enemy_type, (self.x, self.y))


# classes
# music
pygame.mixer.music.load("scd_p_img/mu_so/g_b_m.mp3")
# music
# first stage variables
run = True
player = Player(225, 500)
bullets = []
enemies = []
fire = False
slim_animation_count = 0
enemy_number = 5
asteroid_speed = 2
time = 0
pause_trans = False
pause = False
pause_count = 0
trans_r = False
trans_e = False


def reset_first_stage():
    global run, player, bullets, enemies, fire, slim_animation_count, enemy_number, asteroid_speed, time, pause_trans, pause, pause_count, trans_r, trans_e
    run = True
    player = Player(225, 500)
    bullets = []
    enemies = []
    fire = False
    slim_animation_count = 0
    enemy_number = 5
    asteroid_speed = 2
    time = 0
    pause_trans = False
    pause = False
    pause_count = 0
    trans_r = False
    trans_e = False


# first stage variables variables
# main menu variables
trans_play = False
first_stage = False
count = 0
clock = pygame.time.Clock()
logo_stop = False
trans_shop = False
shop = False
lock_x = 170
lock_y = 150
trans_lock = False


# main menu variables
def draw():
    global main, stage_one, count, logo_stop, lock_x, lock_y, trans_shop
    if main:
        if count >= 96:
            count = 0
        if not logo_stop:
            win.blit(main_menu_background, (0, 0))
            win.blit(game_logo[count // 4], (0, 0))
            count += 1
        elif logo_stop:
            win.blit(game_logo[count // 4], (0, 0))
        if not trans_play:
            win.blit(main_menu_play_button, (110, 160))
        else:
            win.blit(main_menu_play_button_h, (110, 160))
        if not trans_shop:
            win.blit(main_menu_shop_button, (105, 270))
        else:
            win.blit(main_menu_shop_button_h, (105, 270))
    elif shop:
        win.blit(main_menu_background, (0, 0))
        if trans_shop:
            win.blit(back_sign_h, (0, 0))
        elif not trans_shop:
            win.blit(back_sign, (0, 0))
        win.blit(main_menu_shop_button_h, (100, -50))
        win.blit(alien_ship_frame, (20, 150))
        # ships

        win.blit(shop_lock, (lock_x, lock_y))
        win.blit(shop_lock, (lock_x + 150, lock_y))
        win.blit(shop_lock, (lock_x - 150, lock_y + 150))
        win.blit(shop_lock, (lock_x, lock_y + 150))
        win.blit(shop_lock, (lock_x + 150, lock_y + 150))
        win.blit(shop_lock, (lock_x - 150, lock_y + 300))
        win.blit(shop_lock, (lock_x, lock_y + 300))
        win.blit(shop_lock, (lock_x + 150, lock_y + 300))
        # ships
    elif first_stage:
        win.blit(background, (0, 0))
        if pause:
            if not trans_r and not trans_e:
                win.blit(pause_menu, (20, 20))
            elif trans_r:
                win.blit(pause_menu_r, (20, 20))
            elif trans_e:
                win.blit(pause_menu_e, (20, 20))
        else:
            if not pause_trans:
                win.blit(pause_sign, (450, 0))
            else:
                win.blit(pause_sign_h, (450, 0))
            player.draw_space_ship()
            for bullet_draw in bullets:
                bullet_draw.draw_bullet()
            for ENEMY in enemies:
                ENEMY.draw_enemy()
    pygame.display.update()


while run:
    # getting out of loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    # getting out out of loop

    def main_menu():
        clock.tick(96)
        keys = pygame.key.get_pressed()
        global main, time, posx, posy, trans_play, pressed1, pressed2, pressed3, first_stage, logo_stop, trans_shop, shop
        main = True
        posx, posy = pygame.mouse.get_pos()
        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
        # play_button_things
        if 191 <= posx <= 323 and 230 <= posy <= 277:
            trans_play = True
        else:
            trans_play = False
        if 191 <= posx <= 323 and 230 <= posy <= 277 and pressed1 == 1:
            first_stage = True
            main = False
        # play_button_things
        # logo_things
        if posy <= 137:
            logo_stop = True
        else:
            logo_stop = False
        # logo_things

        # shop_button_things
        if posy >= 338 and posy <= 379 and posx >= 175 and posx <= 330:
            trans_shop = True
        else:
            trans_shop = False
        if posy >= 338 and posy <= 379 and posx >= 175 and posx <= 330 and pressed1:
            shop = True
            main = False
        # shop_button_things


    if shop:
        pos1, pos2 = pygame.mouse.get_pos()
        pressed_one, pressed_two, pressed_three = pygame.mouse.get_pressed()
        if pos1 <= 50 and pos2 <= 50 and pressed_one == 1:
            shop = False
        if pos1 <= 50 and pos2 <= 50:
            trans_shop = True
        else:
            trans_shop = False



    elif first_stage:
        if pause:
            pos_x_1, pos_y_2 = pygame.mouse.get_pos()
            pressed_one_1, pressed_two_2, pressed_three_3 = pygame.mouse.get_pressed()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                pause = False
            if pos_x_1 > 97 and pos_x_1 < 400 and pos_y_2 < 253 and pos_y_2 > 154:
                trans_r = True
            else:
                trans_r = False
            if pos_x_1 > 97 and pos_x_1 < 400 and pos_y_2 < 253 and pos_y_2 > 154 and pressed_one_1:
                pause = False
            if pos_x_1 > 139 and pos_x_1 < 351 and pos_y_2 > 335 and pos_y_2 < 412:
                trans_e = True
            else:
                trans_e = False
            if pos_x_1 > 139 and pos_x_1 < 351 and pos_y_2 > 335 and pos_y_2 < 412 and pressed_one_1:
                first_stage = False
                shop = False
                pause = False
                reset_first_stage()
                pygame.mixer.music.stop()
        elif not pause:
            clock.tick(24)
            keys = pygame.key.get_pressed()
            main = False
            stage_one = True
            # pause
            pos_x_1, pos_y_2 = pygame.mouse.get_pos()
            pressed_one_1, pressed_two_2, pressed_three_3 = pygame.mouse.get_pressed()
            if pos_x_1 > 450 and pos_y_2 < 50:
                pause_trans = True
            else:
                pause_trans = False
            if pos_x_1 > 450 and pos_y_2 < 50 and pressed_one_1:
                pause = True

            # pause
            # running music

            if time == 0:
                pygame.mixer.music.play(-1)
            time = 1

            # moving the bullets
            for bullet in bullets:
                if bullet.y > 0:
                    bullet.y -= bullet.speed
                else:
                    bullets.pop(bullets.index(bullet))
            # moving the bullets

            # first stage
            if len(enemies) == 0:
                x = list(range(60, 440))
                for num in range(enemy_number):
                    enemy_x = random.randint(0, len(x) - 1)
                    enemies.append(Enemy(x[enemy_x], asteroids, asteroid_speed))
                    for i in range(100):
                        if enemy_x < len(x):
                            if enemy_x + 1 < len(x):
                                if x[enemy_x + 1] == x[enemy_x] + 1:
                                    x.pop(enemy_x)
                    for s in range(50):
                        enemy_x = enemy_x - 1
                        if enemy_x < len(x):
                            if enemy_x - 1 > 0:
                                if x[enemy_x - 1] == x[enemy_x] - s:
                                    x.pop(enemy_x - 1)
                if enemy_number > 0:
                    enemy_number -= 1
                asteroid_speed += 0.5
            for enemy in enemies:
                for bullet_hit in bullets:
                    if enemy.y + 80 >= bullet_hit.y >= enemy.y:
                        if enemy.x - 10 <= bullet_hit.x <= enemy.x + 30:
                            enemies.pop(enemies.index(enemy))
                            bullets.pop(bullets.index(bullet_hit))
                if enemy.y < 580:
                    enemy.y += enemy.speed
                else:
                    enemies.pop(enemies.index(enemy))
            # moving enemies

            # player interactions
            if keys[pygame.K_LEFT] and player.x > 0:
                player.x -= player.speed
            if keys[pygame.K_RIGHT] and player.x < 430:
                player.x += player.speed
            if keys[pygame.K_SPACE]:
                co = len(bullets)
                if co == 0:
                    slim_bullet_sound.play()
                    bullets.append(Bullet(player.x + 15, player.y))
                elif bullets[co - 1].y <= 300:
                    slim_bullet_sound.play()
                    bullets.append(Bullet(player.x + 15, player.y))
            # player interaction
    else:
        main_menu()
    draw()
pygame.quit()
