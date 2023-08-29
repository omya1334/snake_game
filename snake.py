import pygame
import random
import os

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('Snake Song.mp3')
pygame.mixer.music.play()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Hungry Snake")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

#music
try:
    pygame.mixer.music.load('Snake Song.mp3')
    pygame.mixer.music.play(-1)

except Exception as e:
    print(e)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

# welcome window
def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((255,235,205))
        text_screen("Wel-Come To Hungry snake",(220,20,60), 200, 50)
        text_screen("Press Enter To Play",(255,185,15),100,100)
        text_screen("Cheat codes:", (0,0,255), 100, 150)
        text_screen("1.press 'q' to reset Score",(138,43,226),300,200)
        text_screen("1.press 'space' bar to reset", (255,20,147), 300, 250)
        text_screen("High Score",(255,20,147), 320, 300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER:
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
    snk_list = []
    snk_length = 1

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)

    score = 0
    init_velocity = 5
    snake_size = 30
    fps = 60  # frequency per second for snake speed

    #music
    try:
        pygame.mixer.music.load('Snake Song.mp3')
        pygame.mixer.music.play(-1)

    except Exception as a:
        print(a)


    #cheak if HighScore file exist
    if (not os.path.exists("HighScore.txt")):
        with open ("HighScore.txt", "w") as f:
            f.write("0")

    with open("HighScore.txt", "r") as f:
        highscore = f.read()
    while not exit_game:
        if game_over:
            with open("HighScore.txt", "w") as f:
                f.write(str(highscore))
            gameWindow.fill((145,52,40))
            #gameWindow.blit(bgimg,(0,0))
            text_screen("Game Over! Press Enter To Continue",(125,148,7), 100, 250)



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

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
                        score = 0

                    if event.key == pygame.K_SPACE:
                        highscore = 0

                    if event.key == pygame.K_d:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_a:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_w:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_s:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            # food eating moment
            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                score += 10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length += 5
                try:
                    #music
                    pygame.mixer.music.load('Cobra.mp3')
                    pygame.mixer.music.play(1)

                except Exception as c:
                    print(c)

                if score > int(highscore):
                    highscore = score

            gameWindow.fill(white)
            #gameWindow.blit(bgimg,(1,1))
            text_screen("Score: " + str(score) + " HighScore: " + str(highscore), red, 4, 5)
            pygame.draw.rect(gameWindow,(11,70,155), [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('Bomb Blast sound.mp3')
                pygame.mixer.music.play()

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True

                # music of blast
                try:
                    pygame.mixer.music.load('Bomb Blast sound.mp3')
                    pygame.mixer.music.play()

                except Exception as b:
                    print(b)

            plot_snake(gameWindow,black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()