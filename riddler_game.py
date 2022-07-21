import pygame
import sys
import time
from pygame_functions import *
from button import Button

#Initializes all imported pygame modules
pygame.init()
running = True

#setting clock
clock = pygame.time.Clock()

#game variables
game_paused = False

#Creating initial screen
screen_width, screen_height = 1080, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Main Menu")

#fonts for GUI
mainfont = pygame.font.SysFont('comicsans', 100)
smallfont = pygame.font.SysFont('comicsans', 35)
redtextcolor = (255, 0, 0)

#loading images for GUI
back_ground = pygame.image.load("riddler_main_screen.jpg")
back_ground = pygame.transform.scale(back_ground, (screen_width, screen_height))

button_image = pygame.image.load("red_button2.png")
button_image = pygame.transform.scale(button_image, (250, 75))

quit_image = pygame.image.load("red_button2.png")
quit_image = pygame.transform.scale(quit_image, (250, 75))

game_instructions = pygame.image.load("game_instructions.png")
game_instructions = pygame.transform.scale(game_instructions, (450, 250))

#main text color (Red)
redtextcolor = (250, 0, 0)

#Level and lives

level_lives_font =  pygame.font.SysFont('comicsans', 25)
whitetextcolor = (255, 255, 255)
lives_coord = (400,200)
level_coord = (30, 200)

#riddle font
riddle_font = pygame.font.SysFont('comicsans', 15)
riddle_coord = (150, 350)

# Textbox
input_box = pygame.Rect(150, 450, 140, 32)
user_text = ''

answers = ["an umbrella", "a rubber band", "a stamp", "a mushroom", "the letter g", 
                "nothing", "light", "jared", "a piano", "a clock", "a mountain", "wind", "time","teeth", "an egg"]

riddles = ["What can you catch, but not throw?", "What kind of band never plays music?", "What can travel around the world without leaving its corner?",
            "What kind of room has no doors or windows?", "What is the end of everything?", "Poor People have it. Rich people need it. If you eat it you die. What is it?",
            "What can fill a room but takes up no space?", "Jared’s father has three sons: Snap, Crackle, and..?", "What has many keys but can’t open a single lock?",
            "What has hands but can’t clap?", "What has roots as nobody sees, Is taller than trees, Up, up it goes, And yet never grows?", "Voiceless it cries, Wingless flutters, Toothless bites, Mouthless mutters",
             "This thing all things devours: Birds, beasts, trees, flowers; Gnaws iron, bites steel; Grinds hard stones to meal; Slays king, ruins town, And beats high mountain down.",
             "Thirty white horses on a red hill, First they champ, Then they stamp, Then they stand still", "A box without hinges, key, or lid, Yet golden treasure inside is hid"]

def main_menu():
    pygame.display.set_caption("Main Menu")
    screen = pygame.display.set_mode((screen_width, screen_height))

    while running:
        screen.blit(back_ground, (0, 0)) #places background on screen

        menu_mouse_pos = pygame.mouse.get_pos() #gets the mouses position

        menu_text = mainfont.render("The Riddler Game", True, redtextcolor) #creates text and makes color red
        menu_rect = menu_text.get_rect(center = (540, 100)) #centers the text

        start_button = Button(image = button_image, pos = (150, 250), 
                            text_input = "Next", font = smallfont, base_color = "#d7fcd4", hovering_color = "Red" )
        instructions_button = Button(image = button_image , pos = (150, 350), 
                            text_input = "Instructions", font = smallfont, base_color = "#d7fcd4", hovering_color = "Red")

        screen.blit(menu_text, menu_rect)

        for button in [start_button, instructions_button]:
            button.changeColor(menu_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.checkForInput(menu_mouse_pos):
                    play()
                if instructions_button.checkForInput(menu_mouse_pos):
                    instructions()
        pygame.display.update()

def instructions():
    pygame.display.set_caption("Instructions")

    while running:
        screen.fill("black")
        screen.blit(back_ground, (0,0))
        screen.blit(game_instructions, (100, 300))

        instructions_mouse_pos = pygame.mouse.get_pos()

        instructions_text = mainfont.render("Instructions", True, redtextcolor)
        instructions_rect = instructions_text.get_rect(center = (540, 100))

        menu_button = Button(image = button_image, pos = (540, 650),
                    text_input = "Main Menu", font = smallfont, base_color = "#d7fcd4", hovering_color = "Red")

        screen.blit(instructions_text, instructions_rect)

        for button in [menu_button]:
            button.changeColor(instructions_mouse_pos)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_button.checkForInput(instructions_mouse_pos):
                    main_menu()
        pygame.display.update()

def play():
        pygame.display.set_caption("The Riddler Game")

        while running: 
            screen.fill("black")
            screen.blit(back_ground, (0, 0))

            play_mouse_pos = pygame.mouse.get_pos()

            play_text = mainfont.render("Riddler's Games", True, redtextcolor)
            play_rect = play_text.get_rect(center = (540, 100))

            start_game_button = Button(image = button_image, pos = (540, 250),
                            text_input = "Start Game", font = smallfont, base_color ="#d7fcd4", hovering_color = "Red")
            menu_button = Button(image = button_image, pos = (540, 650),
                            text_input = "Main Menu", font = smallfont, base_color ="#d7fcd4", hovering_color = "Red")

            screen.blit(play_text, play_rect)

            for button in [start_game_button, menu_button]:
                button.changeColor(play_mouse_pos)
                button.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if menu_button.checkForInput(play_mouse_pos):
                        main_menu()
                    if start_game_button.checkForInput(play_mouse_pos):
                        main_game()
            pygame.display.update()



'''
def game_loop():
    level = 1
    lives = 3
    
    lives_lable = level_lives_font.render(f"Lives: {lives}", 1, whitetextcolor)
    level_label = level_lives_font.render(f"Level: {level}", 1, whitetextcolor)
    screen.blit(lives_lable, lives_coord)
    game_riddle = riddle_font.render(riddles[0], 1, whitetextcolor)
    screen.blit(game_riddle, riddle_coord)
    pygame.display.update()
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    pygame.display.update()  
'''

def main_game():
    pygame.display.set_caption("The Riddler Game")

    while running: 
            screen.fill("black")
            screen.blit(back_ground, (0, 0))

            play_mouse_pos = pygame.mouse.get_pos()

            play_text = mainfont.render("Riddler's Games", True, redtextcolor)
            play_rect = play_text.get_rect(center = (540, 100))

            screen.blit(play_text, play_rect)

            level = 1
            lives = 3
    
            lives_lable = level_lives_font.render(f"Lives: {lives}", 1, whitetextcolor)
            level_label = level_lives_font.render(f"Level: {level}", 1, whitetextcolor)
            screen.blit(lives_lable, lives_coord)
            screen.blit(level_label, level_coord)


            game_riddle = riddle_font.render(riddles[0], 1, whitetextcolor)
            screen.blit(game_riddle, riddle_coord)
            
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()        
            
print("Welcome to The Riddler Game")
main_menu()       