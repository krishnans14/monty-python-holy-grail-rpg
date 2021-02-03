import pygame
pygame.init()


class MPCharacter:
    """
    This will be parent class for all the Monty Python characters
    """
    def __init__(self, name, avatar_location):
        self.name = name
        self.avatar = pygame.image.load(avatar_location)


class MPHero(MPCharacter):
    """
    This will be used to create the heroes. They will have an image associated with them
    """
    def __init__(self, name, avatar_location, sigil, sword_skill=None, escape_skill=None):
        super().__init__(name, avatar_location)
        self.sigil = sigil


king_arthur_class = MPHero("Arthur, King of the Britons", 'images/heroes/king_arthur.png', "Sun")
king_arthur_class.sword_skill = 100
sir_lancelot_class = MPHero("Sir Lancelot the brave, of Camelot", "images/heroes/sir_lancelot.png", "Dragon")
sir_robin_class = MPHero("Sir Robin the not-so-brave", "images/heroes/sir_robin.png", "Chicken")
sir_galahad_class = MPHero("Sir Galahad the pure", "images/heroes/sir_galahad.png", "Cross")
sir_bedevere_class = MPHero("Sir Bedevere the wise", "images/heroes/sir_bedevere.png", "Tree of Wisdom")

list_heroes_class = [king_arthur_class, sir_lancelot_class, sir_robin_class, sir_bedevere_class, sir_galahad_class]

#
# class MPEnemy(MPCharacter):
#     """
#
#     """
#
#
# class MPRelics(MPCharacter):
#     """
#     This will be to assign relics and other tools in the game
#     """
#
# king_arthur_big_img = pygame.image.load('images/heroes/king_arthur.png')
# sir_bedevere_big_img = pygame.image.load('images/heroes/sir_bedevere.png')
# sir_galahad_big_img = pygame.image.load('images/heroes/sir_galahad.png')
# sir_lancelot_big_img = pygame.image.load('images/heroes/sir_lancelot.png')
# sir_robin_big_img = pygame.image.load('images/heroes/sir_robin.png')
#
# mp_heroes = [king_arthur_big_img, sir_bedevere_big_img, sir_galahad_big_img, sir_lancelot_big_img, sir_robin_big_img]
#
#
#
#
# king_arthur_img = pygame.image.load('images/king_arthur_1.png')
#
# tim_img = pygame.image.load('images/tim_1.png')
# old_man_big_img = pygame.image.load('images/old_man_bridge_of_death.png')
# old_man_img = pygame.image.load('images/old_man_bridge_of_death_1.png')
# black_knight_big_img = pygame.image.load('images/black_knight.png')
# black_knight_stand = pygame.image.load('images/black_knight_stand.png')
#
# list_of_avatars = [king_arthur_img, old_man_img, tim_img, black_knight_stand]


# In this function, we would load the avatars of the heroes which would be
# King Arthur
# Sir Lancelot the Brave
# Sir Galahad the innocent
# Sir Bedevere the wise
# Sir Robin the not to brave as Lancelot, not so wise ...
#
# There can be several images for each hero, but at least two, one for the initial display
# of heroes and the other for any animation


# In this part, we would load the avatars of the villains that the heroes have to overcome
# The Black Knight
# The Killer Bunny
# The Old man at the bridge of death
# The Knight who says Ni
# The Three headed knight
# The French

def random_villain():
    """
    This function will return a random villain chosen from the list of villains we have
    """