import pygame
import os
import sys
import random


WIDTH = 1500
HEIGHT = 1000
width = 800
height = 1000
FPS = 75
GRAVITY = 0.06
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
WHITE_GRAY = (180, 180, 180)
DARK_GRAY = (80, 80, 80)

bullets = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MFG")
clock = pygame.time.Clock()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
screen_rect = (0, 0, WIDTH, HEIGHT)


def terminate():
    pygame.quit()
    sys.exit()


def END(winner):
    scr = pygame.display.set_mode((WIDTH, HEIGHT))
    if winner == 1:
        text = ['Победил Синий!',
                'Вернуться на главный экран',
                'Вернуться к игре']
    elif winner == 2:
        text = ['Победил Красный!',
                'Вернуться на главный экран',
                'Вернуться к игре']
    coords = [0, 0]
    k = 0
    while True:
        all_sprites.update()
        if winner == 1:
            scr.fill(pygame.Color('blue'))    
        elif winner == 2:
            scr.fill(pygame.Color('red'))        
        all_sprites.draw(screen)        
        font = pygame.font.Font(None, 100)
        text_coord_x = 400
        text_coord_y = 100    
        for line in text:
            string_rendered = font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord_y += 100
            intro_rect.top = text_coord_y
            intro_rect.x = 400
            scr.blit(string_rendered, intro_rect)
            if line == 'Победил Синий!' or line == 'Победил Красный!':
                font = pygame.font.Font(None, 80)
                text_coord_y += 50
            if line == 'Вернуться на главный экран':
                ret_to_main_x = intro_rect.x
                ret_to_main_y = intro_rect.y
                ret_to_main_h = intro_rect.height
                ret_to_main_w = intro_rect.width
            if line == 'Вернуться к игре':
                ret_to_play_x = intro_rect.x
                ret_to_play_y = intro_rect.y
                ret_to_play_h = intro_rect.height
                ret_to_play_w = intro_rect.width
        k += 1
        if k % 25 == 0:
            create_particles((0, 970))
            create_particles((500, 970))
            create_particles((1000, 970))
            create_particles((1500, 970))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                coords[0] = event.pos[0]
                coords[1] = event.pos[1]
                if ret_to_main_x + ret_to_main_w >= coords[0] >= ret_to_main_x and ret_to_main_y + ret_to_main_h >= coords[1] >= ret_to_main_y:
                    Main()
                if ret_to_play_x + ret_to_play_w >= coords[0] >= ret_to_play_x and ret_to_play_y + ret_to_play_h >= coords[1] >= ret_to_play_y:
                    cyckle()
        
        pygame.display.flip()
        clock.tick(FPS)        


def Main():
    sc = pygame.display.set_mode((WIDTH, HEIGHT))
    sc.fill(DARK_GRAY)
    intro_text = ['MFG',
                  'Правила',
                  'Играть']
    font = pygame.font.Font(None, 100)
    text_coord_x = 600
    text_coord_y = 200
    coords = [0, 0]
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord_y += 100
        intro_rect.top = text_coord_y
        intro_rect.x = 600
        sc.blit(string_rendered, intro_rect)
        if line == 'MFG':
            font = pygame.font.Font(None, 80)
            text_coord_y += 50
            continue
        if line == 'Правила':
            pr_x = intro_rect.x
            pr_y = intro_rect.y
            pr_h = intro_rect.height
            pr_w = intro_rect.width
        if line == 'Играть':
            pl_x = intro_rect.x
            pl_y = intro_rect.y
            pl_h = intro_rect.height
            pl_w = intro_rect.width
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                coords[0] = event.pos[0]
                coords[1] = event.pos[1]
                if pr_x + pr_w >= coords[0] >= pr_x and pr_y + pr_h >= coords[1] >= pr_y:
                    prav()
                if pl_x + pl_w >= coords[0] >= pl_x and pl_y + pl_h >= coords[1] >= pl_y:
                    cyckle()
        pygame.display.flip()
        clock.tick(FPS)


def prav():
    sc = pygame.display.set_mode((WIDTH, HEIGHT))
    sc.fill(DARK_GRAY)
    intro_text = ['Правила игры:',
                  '1: Сначала экипаж спит. Сдвинь танк, чтобы разбудить его.',
                  '2: Для передвижения используйте:',
                  '        Синий - стрелки на клавиатуре;',
                  '        Красный - кнопки A, S, D, W.',
                  '3: Для стрельбы используйте:',
                  '        Синий - кнопка Shift;',
                  '        Красный - пробел.',
                  '4: Танки не обращают внимания на стены и друг на друга',
                  'Вернуться на главный экран']
    text_coord_x = 400
    text_coord_y = 50
    font = pygame.font.Font(None, 80)
    coords = [0, 0]
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord_y += 50
        intro_rect.top = text_coord_y
        intro_rect.x = 400
        sc.blit(string_rendered, intro_rect)
        if line == 'Правила игры:':
            font = pygame.font.Font(None, 30)
            text_coord_y += 50         
        if line == 'Вернуться на главный экран':
            x = intro_rect.x
            y = intro_rect.y
            h = intro_rect.height
            w = intro_rect.width
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                coords[0] = event.pos[0]
                coords[1] = event.pos[1]
                if x + w >= coords[0] >= x and y + h >= coords[1] >= y:
                    Main()
        pygame.display.flip()
        clock.tick(FPS)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


Tank_1_u = load_image('blueTank.jpg')
Tank_1_d = pygame.transform.flip(load_image('blueTank.jpg'), 0, 1)
Tank_1_r = pygame.transform.rotate(load_image('blueTank.jpg'), -90)
Tank_1_l = pygame.transform.rotate(load_image('blueTank.jpg'), 90)

Tank_2_u = load_image('redTank.jpg')
Tank_2_d = pygame.transform.flip(load_image('redTank.jpg'), 0, 1)
Tank_2_r = pygame.transform.rotate(load_image('redTank.jpg'), -90)
Tank_2_l = pygame.transform.rotate(load_image('redTank.jpg'), 90)


class Particle(pygame.sprite.Sprite):
    fire = [load_image("star.png")]
    for scale in (10, 20, 40):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))

    def __init__(self, pos, dx, dy):
        super().__init__(all_sprites)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()
        self.velocity = [dx, dy]
        self.rect.x, self.rect.y = pos
        self.gravity = GRAVITY

    def update(self):
        self.velocity[1] += self.gravity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if not self.rect.colliderect(screen_rect):
            self.kill()


def create_particles(position):
    particle_count = 20
    numbers_x = range(-3, 3)
    numbers_y = range(-7, 0)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers_x), random.choice(numbers_y))


class Player(pygame.sprite.Sprite):
    def __init__(self, n):
        self.keystate = pygame.key.get_pressed()
        pygame.sprite.Sprite.__init__(self)
        if n == 1:
            self.image = pygame.Surface((50, 50), 5)
            self.image = Tank_1_u
            self.rect = self.image.get_rect()
            self.rect.centery = HEIGHT / 2
            self.rect.right = height + 290
        if n == 2:
            self.image = pygame.Surface((50, 50))
            self.image = Tank_2_u
            self.rect = self.image.get_rect()
            self.rect.centery = HEIGHT / 2
            self.rect.left = 210
        self.speed_x = 2
        self.speed_y = 2
        self.life = 3

    def move_up(self, t):
        if t == 1:
            if pygame.key.get_pressed()[pygame.K_UP]:
                self.image = Tank_1_u
                self.rect.y -= self.speed_y
                if pygame.sprite.spritecollideany(self, horizontal_borders) or pygame.sprite.collide_rect(self, player_2):
                    self.rect.y += self.speed_y                
                if self.rect.top < 100:
                    self.rect.top = 100
        if t == 2:
            if pygame.key.get_pressed()[pygame.K_w]:
                self.image = Tank_2_u
                self.rect.y -= self.speed_y
                if pygame.sprite.spritecollideany(self, horizontal_borders) or pygame.sprite.collide_rect(self, player_1):
                    self.rect.y += self.speed_y       
                if self.rect.top < 100:
                    self.rect.top = 100            

    def move_down(self, t):
        if t == 1:
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                self.image = Tank_1_d
                self.rect.y += self.speed_y
                if pygame.sprite.spritecollideany(self, horizontal_borders) or pygame.sprite.collide_rect(self, player_2):
                    self.rect.y -= self.speed_y
                if self.rect.bottom > width + 100:
                    self.rect.bottom = width + 100
        if t == 2:
            if pygame.key.get_pressed()[pygame.K_s]:
                self.image = Tank_2_d
                self.rect.y += self.speed_y
                if pygame.sprite.spritecollideany(self, horizontal_borders) or pygame.sprite.collide_rect(self, player_1):
                    self.rect.y -= self.speed_y                
                if self.rect.bottom > width + 100:
                    self.rect.bottom = width + 100            

    def move_left(self, t):
        if t == 1:
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                self.image = Tank_1_l
                self.rect.x -= self.speed_x
                if pygame.sprite.spritecollideany(self, vertical_borders) or pygame.sprite.collide_rect(self, player_2):
                    self.rect.x += self.speed_x
                if self.rect.left < 200:
                    self.rect.left = 200
        if t == 2:
            if pygame.key.get_pressed()[pygame.K_a]:
                self.image = Tank_2_l
                self.rect.x -= self.speed_x
                if pygame.sprite.spritecollideany(self, vertical_borders) or pygame.sprite.collide_rect(self, player_1):
                    self.rect.x += self.speed_x                
                if self.rect.left < 200:
                    self.rect.left = 200            

    def move_right(self, t):
        if t == 1:
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                self.image = Tank_1_r
                self.rect.x += self.speed_x
                if pygame.sprite.spritecollideany(self, vertical_borders) or pygame.sprite.collide_rect(self, player_2):
                    self.rect.x -= self.speed_x
                if self.rect.right > height + 300:
                    self.rect.right = height + 300
        if t == 2:
            if pygame.key.get_pressed()[pygame.K_d]:
                self.image = Tank_2_r
                self.rect.x += self.speed_x
                if pygame.sprite.spritecollideany(self, vertical_borders) or pygame.sprite.collide_rect(self, player_1):
                    self.rect.x -= self.speed_x                
                if self.rect.right > height + 300:
                    self.rect.right = height + 300

    def shoot(self):
        if self.image == Tank_1_u or self.image == Tank_2_u:
            bullet = Bullet(self.rect.centerx, self.rect.top, 'u')
        if self.image == Tank_1_l or self.image == Tank_2_l:
            bullet = Bullet(self.rect.left, self.rect.centery, 'l')
        if self.image == Tank_1_r or self.image == Tank_2_r:
            bullet = Bullet(self.rect.right, self.rect.centery, 'r')
        if self.image == Tank_1_d or self.image == Tank_2_d:
            bullet = Bullet(self.rect.centerx, self.rect.bottom, 'd')
        bullets.add(bullet)

    def death(self):
        self.life -= 1
        if self.life == 0:
            self.kill()
            return True


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direct):
        pygame.sprite.Sprite.__init__(self)
        self.direct = direct
        if self.direct == 'u':
            self.image = pygame.Surface((10, 20))
            self.rect = self.image.get_rect()
            self.rect.bottom = y
            self.rect.centerx = x
        if self.direct == 'd':
            self.image = pygame.Surface((10, 20))
            self.rect = self.image.get_rect()
            self.rect.top = y
            self.rect.centerx = x
        if self.direct == 'r':
            self.image = pygame.Surface((20, 10))
            self.rect = self.image.get_rect()
            self.rect.centery = y
            self.rect.left = x
        if self.direct == 'l':
            self.image = pygame.Surface((20, 10))
            self.rect = self.image.get_rect()
            self.rect.centery = y
            self.rect.right = x
        self.image.fill(WHITE_GRAY)
        self.speedy = 15

    def update(self):
        if self.direct == 'r':
            self.rect.x += self.speedy
            if self.rect.x >= height + 300:
                self.kill()
        if self.direct == 'l':
            self.rect.x -= self.speedy
            if self.rect.x <= 200:
                self.kill()
        if self.direct == 'u':
            self.rect.y -= self.speedy
            if self.rect.y <= 100:
                self.kill()
        if self.direct == 'd':
            self.rect.y += self.speedy
            if self.rect.y >= 100 + width:
                self.kill()
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.kill()
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.kill()


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


def cyckle():
    PlayerGroup = pygame.sprite.Group()
    global player_1
    player_1 = Player(1)
    global player_2
    player_2 = Player(2)
    all_sprites.add(player_1)
    all_sprites.add(player_2)
    
    Border(200, 99, height + 301, 99)
    Border(200, width + 100, height + 300, width - 100)
    Border(200, 100, 200, width + 100)
    Border(height + 300, 100, height + 300, width + 101)
    Border(500, width - 100, 500, width + 100)
    Border(WIDTH - 500, 100, WIDTH - 500, 300)
    Border(WIDTH - 1000, 400, WIDTH - 750, 400)
    Border(WIDTH - 750, 600, WIDTH - 500, 600)
    Border(WIDTH - 750, 400, WIDTH - 750, 600)
    
    sound_boom = pygame.mixer.Sound('data/Выстрел.wav')
    sound_win = pygame.mixer.Sound('data/Победа.mp3')
    
    running = True
    SHOOT_1 = False
    SHOOT_2 = False
    UP = False
    DOWN = False
    RIGHT = False
    LEFT = False
    UP_2 = False
    DOWN_2 = False
    RIGHT_2 = False
    LEFT_2 = False
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    SHOOT_2 = True
                if event.key == pygame.K_RSHIFT:
                    SHOOT_1 = True

                if event.key == pygame.K_a:
                    LEFT_2 = True
                if event.key == pygame.K_d:
                    RIGHT_2 = True
                if event.key == pygame.K_w:
                    UP_2 = True
                if event.key == pygame.K_s:
                    DOWN_2 = True

                if event.key == pygame.K_UP:
                    UP = True
                if event.key == pygame.K_DOWN:
                    DOWN = True
                if event.key == pygame.K_RIGHT:
                    RIGHT = True
                if event.key == pygame.K_LEFT:
                    LEFT = True

        if UP_2:
            player_2.move_up(2)
            if SHOOT_2:
                sound_boom.play()
                player_2.shoot()
                SHOOT_2 = False
        if DOWN_2:
            player_2.move_down(2)
            if SHOOT_2:
                sound_boom.play()
                player_2.shoot()
                SHOOT_2 = False
        if RIGHT_2:
            player_2.move_right(2)
            if SHOOT_2:
                sound_boom.play()
                player_2.shoot()
                SHOOT_2 = False
        if LEFT_2:
            player_2.move_left(2)
            if SHOOT_2:
                sound_boom.play()
                player_2.shoot()
                SHOOT_2 = False

        if UP:
            player_1.move_up(1)
            if SHOOT_1:
                sound_boom.play()
                player_1.shoot()
                SHOOT_1 = False
        if DOWN:
            player_1.move_down(1)
            if SHOOT_1:
                sound_boom.play()
                player_1.shoot()
                SHOOT_1 = False
        if RIGHT:
            player_1.move_right(1)
            if SHOOT_1:
                sound_boom.play()
                player_1.shoot()
                SHOOT_1 = False
        if LEFT:
            player_1.move_left(1)
            if SHOOT_1:
                sound_boom.play()
                player_1.shoot()
                SHOOT_1 = False

        bullets.update()
        all_sprites.update()
        screen.fill(DARK_GRAY)
        bullets.draw(screen)
        all_sprites.draw(screen)
        pygame.display.flip()
        kill_1 = pygame.sprite.spritecollide(player_1, bullets, True)
        kill_2 = pygame.sprite.spritecollide(player_2, bullets, True)
        k_1 = False
        k_2 = False
        if kill_1:
            k_1 = player_1.death()
        if kill_2:
            k_2 = player_2.death()
        
        if k_1:
            k_2 = player_2.death()
            k_2 = player_2.death()
            k_2 = player_2.death()
            for elem in horizontal_borders:
                elem.kill()
            for elem in vertical_borders:
                elem.kill() 
            for elem in bullets:
                elem.kill()
            sound_win.play()
            END(2)
        elif k_2:
            k_1 = player_1.death()
            k_1 = player_1.death()
            k_1 = player_1.death()
            for elem in horizontal_borders:
                elem.kill()
            for elem in vertical_borders:
                elem.kill()
            for elem in bullets:
                elem.kill()
            sound_win.play()
            END(1)
            

    pygame.quit()


Main()
