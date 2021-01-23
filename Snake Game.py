import pygame
import random

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 128, 0)
midnight_blue = (25, 25, 112)

# Creating Window
screen_width = 800
screen_height = 600
display = pygame.display.set_mode((screen_width, screen_height))

# Game title
pygame.display.set_caption("Snake Game")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text,True,color)
    display.blit(screen_text, [x,y])

def plot_snake(display, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(display, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        display.fill((250, 190, 200))
        text_screen("Welcome to Snake Game", white, 190, 250)
        text_screen("Press Space Bar To Play", midnight_blue, 190, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()

        pygame.display.update()
        clock.tick(60)


# Game Loop
def game_loop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snake_list = []
    snake_length = 1
    with open("highscore.txt", "r") as f:
        highscore = f.read()

    food_x = random.randint(0, screen_width / 2)
    food_y = random.randint(0, screen_height / 2)
    score = 0
    init_velocity = 5
    snake_size = 20
    fps = 50

    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            display.fill(black)
            text_screen("Game over! Press Enter To Continue", green, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True

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

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                score += 10
                print("yummy")
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snake_length += 5
                if score>int(highscore):
                    highscore = score

            display.fill(black)
            text_screen("Score: " + str(score) + "  highscore: "+str(highscore), red, 5, 5)
            pygame.draw.rect(display, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True

            plot_snake(display, blue, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()
game_loop()

