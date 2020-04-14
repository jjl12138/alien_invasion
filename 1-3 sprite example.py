#  Pygame Sprite Example
import pygame
import random
import os


WIDTH = 800 # width of our game window
HEIGHT = 600 # height of our game window
FPS = 30 # 30 frames per second


# Colors(R,G,B),define color
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


# set up asset folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')


class Player(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder,'p1_jump.png')).convert()  # pygame.image.load()加载图像 convert()将格式转化为更快显示的类型，加速pygame的绘制
        self.image.set_colorkey(BLACK) # 将图片背景颜色中和colorkey相同的颜色设置为透明
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.y_speed = 5

    def update(self, *args):
        # any code here will happen every time the game loop updates
        self.rect.x += 5
        self.rect.y +=self.y_speed
        if self.rect.bottom > HEIGHT - 200:
            self.y_speed = -5
        if self.rect.top < 200:
            self.y_speed = 5
        if self.rect.left > WIDTH:
            self.rect.right = 0



# initialize pygame and create windw
pygame.init()  # 启动pygame并初始化
pygame.mixer.init()  # 声音初始化
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # 游戏屏幕，按照在配置常量中设置的大小创建
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()  # 创建一个时钟以便于确保游戏能以指定的FPS运行


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


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


    # Update                   # 游戏结束的话直接将running设为False即可
    all_sprites.update()


    # Render(draw)             # 现在还没有确定具体的代码，先用一些基本代码填充，后续再补充
    screen.fill(BLUE)
    all_sprites.draw(screen)
    # *after* drawing everything,flip the display
    pygame.display.flip()



pygame.quit()
