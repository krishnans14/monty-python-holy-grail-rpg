import pygame
import time

# The following is hearsay, but I'm being quite careful and deliberate in merging
# the namespace as I have variables declared in auxiliary_functions
from auxiliary_functions import *

# The avatars used for the game are all loaded in avatars_monty_python module
import avatars_monty_python as amp
pygame.init()


avatar_width = 60
avatar_list = amp.list_heroes_class


def quest_monty_python():
    """
    This is the main function where the Monty python quest takes place
    """
    x = int(display_width * 0.1)
    y = int(display_height * 0.05)
    x_change = 0
    quest_failed = False
    change_avatar = False
    current_avatar_num = 0
    proceed_quest = False
    change_avatar_dir = 0

    gameDisplay.fill(white)
    display_message(['Here are the heroes whose journey you will take'], 25)
    display_message(['Press any key to continue'], 15, display_width*1.2, display_height*1.7)
    pygame.display.update()
    quest_failed, proceed_quest = wait_for_key()

    while not quest_failed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quest_failed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    change_avatar = True
                    change_avatar_dir = -1
                if event.key == pygame.K_RIGHT:
                    change_avatar = True
                    change_avatar_dir = 1
                if event.key == pygame.K_q:
                    quest_failed = True

        gameDisplay.fill(white)
        if change_avatar:
            current_avatar_num += change_avatar_dir
            if current_avatar_num < 0:
                current_avatar_num = len(avatar_list)-1
            current_avatar_num = current_avatar_num % len(avatar_list)
            change_avatar = False

        avatar_img = avatar_list[current_avatar_num].avatar
        avatar_name = avatar_list[current_avatar_num].name
        gameDisplay.blit(avatar_img, (x, y))
        display_message([avatar_name], 30, display_width, int(display_height*0.05), black, 0)
        display_message(['Press left/right arrow to see others', 'Press q to quit'], 15, int(display_width*1.6),
                        int(display_height * 1.6), dark_green, 0)
        # display_message(['Press Enter to choose your hero'], 15, int(display_width * 1.6), int(display_height * 1.7),
        #                 dark_green, -1)
        # display_message(['Press q to quit'], 15, int(display_width*1.6), int(display_height * 1.8), red, 0)

        # quest_failed, proceed_quest = wait_for_key()
        # time.sleep(2)
        pygame.display.flip()
        clock.tick(60)


game_prelude()
quest_monty_python()
pygame.quit()