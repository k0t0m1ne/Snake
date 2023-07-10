import pygame as pygame
from random import randint

appl=0
pygame.init()
font = pygame.font.SysFont("Calibri", 36)
text1 = font.render("Проиграл", 1, (255, 255, 255))

side = 30
w = 17
h = 15
disp = pygame.display.set_mode((w * side, h * side))
blue=(21, 32, 229)
white=(255, 255, 255) 
yellow=(255, 193, 6)
red=(255,0,0)
purple=(255,0,255)
game_running=0

dirs = [pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT, pygame.K_UP]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
snake = [(7, 3), (7, 4)]
direction = 0
a=0

#Функция расположения яблока на поле
def place_apple():
    a = (randint(0, w - 1), randint(0, h - 1))
    while a in snake:
        a = (randint(0, w - 1), randint(0, h - 1))
    return a

apple = place_apple()

# Проверка игрока на столкновения с игровыми объектами
def check_collisions():
    head = snake[-1]
    for i in range(len(snake)-1):
        if head == snake[i]:
            return 2
    if head[0] >= w or head[0] < 0:
        return 2
    if head[1] >= h or head[1] < 0:
        return 2
    if head == apple:
        return 1
    return 0
app=0

clock = pygame.time.Clock()
f = pygame.font.SysFont('Avenir Heavy', 50, True)
a=5


while True:

    text2 = font.render(("Ты собрал яблок:"+str(app)), 1, (255, 255, 255))
    clock.tick(a)

    # Инпуты змейки
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            break
        if e.type == pygame.KEYDOWN:
            if game_running == 0:
                game_running = 1
            if e.key == pygame.K_SPACE:
                game_running = 0
                snake = [(7, 3), (7, 4)]
                direction = 0
                apple = place_apple()
                a=5
                app=0
                
            if e.key==dirs[0] and direction!=2:
                direction=0
            if e.key==dirs[1] and direction!=3:
                direction=1
            if e.key==dirs[2] and direction!=0:
                direction=2
            if e.key==dirs[3] and direction!=1:
                direction=3
    
    snake.append((snake[-1][0]+dx[direction],snake[-1][1]+dy[direction]))

    # Все возможные столкновения
    check=check_collisions()
    if check==1:
        app+=1
        apple=place_apple()
        a+=1
    if check==0:
        snake.pop(0)
    if check==2:
        game_running=2


    # Экран
    disp.fill((0,102,0))
    disp.blit(text2, (8, 16))
    pygame.draw.rect(disp,yellow,(apple[0]*side,apple[1]*side,side,side))
    pygame.draw.rect(disp,yellow,(apple[0]*side,apple[1]*side,side,side),3)
    for i in range(len(snake)):
        pygame.draw.rect(disp,(153,153,255),(snake[i][0]*side,snake[i][1]*side,side,side))
        pygame.draw.rect(disp,(0,0,0),(snake[i][0]*side,snake[i][1]*side,side,side),5)
    if game_running==2:
        disp.fill((0,102,0))
        disp.blit(text1, (100, 200))
        disp.blit(text2, (100, 250))

    pygame.display.update()
