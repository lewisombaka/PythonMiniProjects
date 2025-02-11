import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

width = 600
height = 400

dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Kamwongo')

person_img = pygame.image.load('kaka.png')  # Replace with the path to your person image
food_img = pygame.image.load('food.jfif')  # Replace with the path to your food image

# Scale images to fit the game block size (50x50)
person_img = pygame.transform.scale(person_img, (50, 50))
food_img = pygame.transform.scale(food_img, (50, 50))

# Define clock and snake block size
clock = pygame.time.Clock()
snake_block = 50  # Increase block size to match the image size
snake_speed = 5

# Define font styles
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# List of custom texts for score
score_texts = [
    "Mama Mboga", "Bodaboda", "Sadaka", "nhif", "linda mama", "barabara", 
    "pesa ya wazee", "HELB", "Githeri", "Chapati", "nimechoka", "Niliwa Wuon"
]

# Function to display custom score text
def your_score(length):
    # Get the custom text based on the snake length
    text_index = (length - 1) % len(score_texts)
    value = score_font.render(score_texts[text_index], True, black)
    dis.blit(value, [0, 0])

# Function to draw the snake (using the image)
def our_snake(snake_block, snake_list):
    for x in snake_list:
        dis.blit(person_img, [x[0], x[1]])

# Function to display messages
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [width / 6, height / 3])

# Main game loop
def gameLoop():
    game_over = False
    game_close = False

    # Starting position of the snake
    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Randomize food position
    foodx = round(random.randrange(0, width - snake_block) / 50.0) * 50.0
    foody = round(random.randrange(0, height - snake_block) / 50.0) * 50.0

    while not game_over:

        while game_close:
            dis.fill(blue)
            message("Enda Home", red)
            your_score(Length_of_snake - 1)
            pygame.display.update()

            # Handling key presses to quit or restart the game
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Handling events (keystrokes)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Checking if snake hits the boundaries
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)

        # Draw food (use the image for food)
        dis.blit(food_img, [foodx, foody])

        # Add new head to snake list and remove the tail
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Check if snake collides with itself
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Draw the snake
        our_snake(snake_block, snake_List)
        your_score(Length_of_snake - 1)

        pygame.display.update()

        # Check if snake eats food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 50.0) * 50.0
            foody = round(random.randrange(0, height - snake_block) / 50.0) * 50.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    # Close Pygame window when the game is over
    pygame.quit()
    quit()

# Start the game
gameLoop()
