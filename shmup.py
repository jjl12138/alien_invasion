# Shmup game - part 4
# shmup.py
# Adding graphics
import pygame
import random
from os import path


img_dir = path.join(path.dirname(__file__), 'img')


WIDTH = 512  # width of our game window
HEIGHT = 768  # height of our game window
FPS = 60  # 60 frames per second


# Colors(R,G,B),define color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


# initialize pygame and create windw
pygame.init()  # 启动pygame并初始化
pygame.mixer.init()  # 声音初始化
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # 游戏屏幕，按照在配置常量中设置的大小创建
pygame.display.set_caption("Shmup!")
icon = pygame.image.load("img/alien.ico")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()  # 创建一个时钟以便于确保游戏能以指定的FPS运行


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (60,40))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0

    def update(self):
        # any code here will happen every time the game loop updates
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx

        if keystate[pygame.K_UP]:
            self.speedy = -5
        if keystate[pygame.K_DOWN]:
            self.speedy = 5
        self.rect.y += self.speedy

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(meteor_img, (32, 32))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedx = random.randrange(-3, 3)
        self.speedy = random.randrange(1, 5)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -50 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 5)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bullet_img, (48, 48))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -8

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()


# load all game graphics
background = pygame.image.load(path.join(img_dir, 'background2.jpg')).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, 'my_plane.png')).convert()
meteor_img = pygame.image.load(path.join(img_dir, 'enemy1.png')).convert()
bullet_img = pygame.image.load(path.join(img_dir, 'bullet.png')).convert()


all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)


# Game Loop
running = True


while running:
    # keep loop running at the right speed
    clock.tick(FPS)


    # Process input(events)    # 这是游戏主循环，通过变量running控制，如果需要
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()


    # Update                   # 游戏结束的话直接将running设为False即可
    all_sprites.update()

    # check to see if a bullet hit a mob
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    # check to see if a mob hit the player
    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        running = False

    # Render(draw)             # 现在还没有确定具体的代码，先用一些基本代码填充，后续再补充
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    # *after* drawing everything,flip the display
    pygame.display.flip()



pygame.quit()


