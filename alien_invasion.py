#  Pygame template - skeleton for a new pygame project
import time

import pygame
import random


WIDTH = 360 # width of our game window
HEIGHT = 480 # height of our game window
FPS = 30 # 30 frames per second


# Colors(R,G,B),define color
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)



# initialize pygame and create windw
pygame.init()  # 启动pygame并初始化
pygame.mixer.init()  # 声音初始化
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # 游戏屏幕，按照在配置常量中设置的大小创建
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()  # 创建一个时钟以便于确保游戏能以指定的FPS运行


myfont = pygame.font.Font(None, 60)
textImage = myfont.render("pygame", True, WHITE)  # 参数1：文本内容 参数2：抗锯齿字体 参数3：颜色值（RGB）


# Game Loop
running = True
count = 0
start = time.time()  # 返回当前时间的时间戳


while running:

    # keep loop running at the right speed
    clock.tick(FPS)

    # Process input(events)    # 这是游戏主循环，通过变量running控制，如果需要
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False


    # Update                   # 游戏结束的话直接将running设为False即可
    count += 1
    now = time.time()
    fps = count/(now-start)
    fpsImage = myfont.render(str(fps),True,WHITE)


    # Render(draw)             # 现在还没有确定具体的代码，先用一些基本代码填充，后续再补充
    screen.fill(BLACK)
    screen.blit(fpsImage,(100,100))
    # *after* drawing everything,flip the display
    pygame.display.flip()



pygame.quit()














