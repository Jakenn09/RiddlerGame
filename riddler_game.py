import pygame
import sys
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

start_image = pygame.image.load("red_button2.png")
start_image = pygame.transform.scale(start_image, (250, 75))

instructions_image = pygame.image.load("red_button2.png")
instructions_image = pygame.transform.scale(instructions_image, (250,75))

quit_image = pygame.image.load("red_button2.png")
quit_image = pygame.transform.scale(quit_image, (250, 75))

#main text color (Red)
redtextcolor = (250, 0, 0)

def main_menu():
    pygame.display.set_caption("Main Menu")
    screen = pygame.display.set_mode((screen_width, screen_height))

    while running:
        screen.blit(back_ground, (0, 0)) #places background on screen

        menu_mouse_pos = pygame.mouse.get_pos() #gets the mouses position

        menu_text = mainfont.render("The Riddler Game", True, redtextcolor) #creates text and makes color red
        menu_rect = menu_text.get_rect(center = (540, 100)) #centers the text

        start_button = Button(image = start_image, pos = (150, 250), 
                            text_input = "Start", font = smallfont, base_color = "#d7fcd4", hovering_color = "Red" )
        instructions_button = Button(image = instructions_image , pos = (150, 350), 
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

        instructions_mouse_pos = pygame.mouse.get_pos()

        instructions_text = mainfont.render("Instructions", True, redtextcolor)
        instructions_rect = instructions_text.get_rect(center = (540, 100))

        menu_button = Button(image = instructions_image, pos = (540, 650),
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

            start_game_button = Button(image = instructions_image, pos = (540, 250),
                            text_input = "Start Game", font = smallfont, base_color ="#d7fcd4", hovering_color = "White")
            menu_button = Button(image = instructions_image, pos = (540, 650),
                            text_input = "Main Menu", font = smallfont, base_color ="#d7fcd4", hovering_color = "White")

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
            pygame.display.update()
                    
                        
print("Welcome to The Riddler Game")
main_menu()       