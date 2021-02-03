
import pygame
import time
pygame.init()

# Colour definitions
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
dark_green = (50, 100, 35)
blue = (0, 0, 128)
gray = (128, 128, 128)
# Screen size definitions
display_width = 800
display_height = 600
# The game display is set
gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.RESIZABLE)
pygame.display.set_caption('Monty Python')
clock = pygame.time.Clock()


def display_message(message_text, size_font=50, position_x=display_width, position_y=display_height, color_font=blue,
                    wait_time=2):
    """
    This function displays a text message on the screen
    The input message_text must be a list of strings. Even if it is only a single string
    """
    position_x = int(position_x)
    position_y = int(position_y)
    for i in range(0, len(message_text)):
        font_object_large = pygame.font.Font('freesansbold.ttf', size_font)  # creating font object
        text_surface_object = font_object_large.render(message_text[i], True, color_font)
        text_rect_object = text_surface_object.get_rect()
        position_y = position_y*(1+i*0.1)
        text_rect_object.center = ((position_x // 2), (position_y // 2))
        gameDisplay.blit(text_surface_object, text_rect_object)
    if wait_time > 0:
        time.sleep(wait_time)
    pygame.display.update()


def wait_for_key(expected_key=pygame.KEYDOWN):
    quest_failed = False
    proceed_quest = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quest_failed = True
                break
            if event.type == expected_key:
                proceed_quest = True
                break
        if quest_failed or proceed_quest:
            return quest_failed, proceed_quest


def avatar_animate_auto(avatar_img, position_x, position_y, direction_movement, step_size, num_steps, refresh_rate=0.5):

    for i in range(0, num_steps):
        if direction_movement == 'l' or direction_movement == 'L':
            position_x = position_x - step_size
            if position_x < 0:
                position_x = display_width - 30
        if direction_movement == 'r' or direction_movement == 'R':
            position_x = position_x + step_size
            if position_x > display_width:
                position_x = 30
        if direction_movement == 'u' or direction_movement == 'U':
            position_y = position_y - step_size
            if position_y < 0:
                position_y = display_height - 40
        if direction_movement == 'd' or direction_movement == 'D':
            position_y = position_y + step_size
            if position_y > display_height:
                position_y = 40
        gameDisplay.fill(white)
        gameDisplay.blit(avatar_img, (position_x, position_y))
        pygame.display.update()
        time.sleep(refresh_rate)


def game_prelude():
    pos_x = int(display_width * 0.1)
    pos_y = int(display_height * 0.05)
    gameDisplay.fill(black)
    message_to_display = ['An RPG of the movie', 'Monty Python and the Quest for the Holy Grail']
    display_message(message_to_display, 20, display_width, display_height, white)

    # wait_for_key()
    gameDisplay.fill(black)
    message_to_display = ['Welcome to Britain, 932 AD']
    display_message(message_to_display, 50, display_width, display_height, white)

    # wait_for_key()
    gameDisplay.fill(black)
    message_to_display = ['Arthur is walking around without a sword'] 
    display_message(message_to_display, 30, display_width, display_height, white)
    time.sleep(2)
    # wait_for_key()
    # gameDisplay.fill(white)
    king_arthur_without_sword = pygame.image.load('images/king_arthur_without_xcalib.png')
    avatar_animate_auto(king_arthur_without_sword, pos_x, pos_x, 'r', 25, 20, 0.25)

    gameDisplay.fill(black)
    message_to_display = ['And then he comes across a strange woman lying in a pond', 'and distributing swords']
    display_message(message_to_display, 20, display_width, display_height*0.7, white)

    time.sleep(2)
    display_message(['No... No... he comes across the lady of the lake'], 30, display_width, int(1.1*display_height),
                    white)
    pygame.display.update()
    time.sleep(3)
    lady_of_the_lake = pygame.image.load('images/lady_of_lake.png')
    avatar_animate_auto(lady_of_the_lake, pos_x, pos_y+200, 'u', 50, 4, 1)

    avatar_img = pygame.image.load('images/heroes/king_arthur.png')
    gameDisplay.fill(white)
    display_message(['Arthur becomes King Arthur - with X-caliber'], 25, display_width, pos_y, black)
    pygame.display.update()
    time.sleep(1)
    gameDisplay.blit(avatar_img, (pos_x, pos_y))
    pygame.display.update()
    time.sleep(3)

    gameDisplay.fill(white)
    pygame.display.update()

    message_to_display = ['Original art work by KS', 'Inspired by various artists and Monty Python']
    display_message(message_to_display, 25, display_width, display_height, black, 1)
    display_message(['Game inspired by the movie'], 20, display_width, int(display_height*1.6), black, 2)

    # wait_for_key()
