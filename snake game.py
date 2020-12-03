

import pygame
import random

pygame.mixer.init()
# pygame.mixer.music.load('abc.mp3')
# pygame.mixer.music.play()
pygame.init()
pygame.font.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue=(0,0,255)
lime=(255,255,0)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# background images
# bgimg= pygame.image.load("photo3.jpg")
# bgimg=pygame.transform.scale(bgimg ,(screen_width,screen_height)).convert_alpha()
# bgimg2=pygame.image.load("photo2.jpg")
# bgimg=pygame.transform.scale(bgimg2 ,(screen_width,screen_height)).convert_alpha()
# bg1 = pygame.image.load("Screen/bg.jpg")
# bg2 = pygame.image.load("Screen/bg2.jpg")
intro = pygame.image.load("photo3.jpg")
intro=pygame.transform.scale(intro ,(screen_width,screen_height)).convert_alpha()

outro = pygame.image.load("photo2.jpg")
outro=pygame.transform.scale(outro,(screen_width,screen_height)).convert_alpha()
outr = pygame.image.load("outro.png")



# Game Title
pygame.display.set_caption("Snakes by Vaibhav")
pygame.display.update()



clock = pygame.time.Clock()
font = pygame.font.Font('fonts.ttf', 50)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game=False
    while not exit_game:


        gameWindow.blit(intro,(0, 0))
        font = pygame.font.SysFont('arial', 50)

        # text_screen("the game",(139,69,19),670,550)
        text_screen("press ",(210,105,30),0,0)
        text_screen("space",(139,69,19),150,0)


        # text_screen("space",(139,69,19),750,0)
        text_screen("to play the game",(210,105,30),470,550)
        text_screen("!",(139,69,19),875,550)
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('abc.mp3')
                    pygame.mixer.music.play()

                    gameloop()


        pygame.display.update()
        clock.tick(60)

# Game Loop

def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0

    with open("highscore.txt","r") as f:
        highscore=f.read()                                       

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 2
    snake_size = 15
    fps = 60
    snk_list = []
    snk_length = 1

    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            gameWindow.blit(outr,(0,0))




            text_screen("Your score :"+str(score),black,320,350)
            text_screen("HIGHSCORE :"+str(highscore),black,310,400)




            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_q:
                        score+=10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                score +=10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                init_velocity+=0.5
                snk_length +=5
                if score > int(highscore):
                    highscore = score



            gameWindow.blit(outro,(0,0))
            text_screen("Score: " + str(score )+" -Highscore : "+str(highscore), (0,128,128),200 , 5)

            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over=True
                pygame.mixer.music.load('abz.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True
                pygame.mixer.music.load('abz.mp3')
                pygame.mixer.music.play()

             # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()

