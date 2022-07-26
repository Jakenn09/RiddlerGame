import pygame
import sys
import time
from button import Button

#Initializes all imported pygame modules
pygame.init()
running = True

#setting clock
clock = pygame.time.Clock()

#game variables
game_paused = False

#Creating initial screen
screen_width, screen_height = 1440, 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Main Menu")

# fonts and color for GUI
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
game_instructions = pygame.transform.scale(game_instructions, (900, 900))

#main text color (Red)
redtextcolor = (250, 0, 0)

# Level and lives with font, color and coordinates for GUI
level_lives_font =  pygame.font.SysFont('comicsans', 25)
whitetextcolor = (255, 255, 255)
lives_coord = (400,200)
level_coord = (30, 200)

# Riddle font and coordinates for GUI
riddle_font = pygame.font.SysFont('comicsans', 25)
riddle_coord = (150, 350)

# Textbox (might not be used)
Textfont = pygame.font.SysFont(None, 25)
user_text = ''
input_rect = pygame.Rect(250, 450, 140, 30)



# List containing the answers to the riddles
answers = ["a cold", "a rubber band", "a stamp", "a mushroom", "the letter g", 
                "nothing", "light", "jared", "a piano", "a clock"]

# List containing the riddles
riddles = ["What can you catch, but not throw?", "What kind of band never plays music?", "What can travel around the world without leaving its corner?",
            "What kind of room has no doors or windows?", "What is the end of everything?", "Poor People have it. Rich people need it. If you eat it you die. What is it?",
            "What can fill a room but takes up no space?", "Jared’s father has three sons: Snap, Crackle, and..?", "What has many keys but can’t open a single lock?",
            "What has hands but can’t clap?"]

# Main menu function 
def main_menu():
    pygame.display.set_caption("Main Menu") 
    screen = pygame.display.set_mode((screen_width, screen_height))

    while running:
        screen.blit(back_ground, (0, 0)) # places background on screen

        menu_mouse_pos = pygame.mouse.get_pos() # gets the mouses position

        menu_text = mainfont.render("The Riddler Game", True, redtextcolor) # creates text and makes color red
        menu_rect = menu_text.get_rect(center = (540, 100)) # centers the text

        start_button = Button(image = button_image, pos = (150, 250), 
                            text_input = "Next", font = smallfont, base_color = "#d7fcd4", hovering_color = "Red" ) # creation of the start button
        instructions_button = Button(image = button_image , pos = (150, 350), 
                            text_input = "Instructions", font = smallfont, base_color = "#d7fcd4", hovering_color = "Red") # creation of the instructions button 

        screen.blit(menu_text, menu_rect) # adds the menu text and rectangle to the screen

        for button in [start_button, instructions_button]:
            button.changeColor(menu_mouse_pos) # changes color of button when highlighted
            button.update(screen) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # exits GUI when red X is pressed
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: # if mouse is pressed on start button, play function runs 
                if start_button.checkForInput(menu_mouse_pos):
                    play()
                if instructions_button.checkForInput(menu_mouse_pos): # if mouse is pressed on instructions button, instructions function is run
                    instructions()
        pygame.display.update() # updates GUI on button press

def instructions():
    pygame.display.set_caption("Instructions")

    while running:
        screen.fill("black") # Sets screen and background
        screen.blit(back_ground, (0,0))
        screen.blit(game_instructions, (.5, .5)) # adds the instruction .png to the GUI

        instructions_mouse_pos = pygame.mouse.get_pos()

        instructions_text = mainfont.render("Instructions", True, redtextcolor)
        instructions_rect = instructions_text.get_rect(center = (540, 100))

        menu_button = Button(image = button_image, pos = (540, 650),
                    text_input = "Main Menu", font = smallfont, base_color = "#d7fcd4", hovering_color = "Red")

        screen.blit(instructions_text, instructions_rect) # adds instructions text to the screen

        for button in [menu_button]:
            button.changeColor(instructions_mouse_pos) # changes color of button when highlighted
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # exits GUI when red X is pressed
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_button.checkForInput(instructions_mouse_pos): # if menu button is pressed, takes user back to main menu function 
                    main_menu()
        pygame.display.update()

def play():
        pygame.display.set_caption("The Riddler Game")

        while running: 
            screen.fill("black") # Sets default screen
            screen.blit(back_ground, (0, 0))

            play_mouse_pos = pygame.mouse.get_pos()

            play_text = mainfont.render("Riddler's Games", True, redtextcolor)
            play_rect = play_text.get_rect(center = (540, 100))

            start_game_button = Button(image = button_image, pos = (540, 250),
                            text_input = "Start Game", font = smallfont, base_color ="#d7fcd4", hovering_color = "Red") # creation of start game button 
            menu_button = Button(image = button_image, pos = (540, 650),
                            text_input = "Main Menu", font = smallfont, base_color ="#d7fcd4", hovering_color = "Red") # creation of main menu button 

            screen.blit(play_text, play_rect) # adds the pplay text to the screen

            for button in [start_game_button, menu_button]:
                button.changeColor(play_mouse_pos) # changes color of button when highlighted
                button.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # exits GUI when red X is pressed
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if menu_button.checkForInput(play_mouse_pos): # if menu button is pressed, takes user back to main menu
                        main_menu()
                    if start_game_button.checkForInput(play_mouse_pos): # if start game button is pressed, takes you to the main game loop
                        Riddle_0() 
            pygame.display.update()

def Riddle_0():
    global user_text
    pygame.display.set_caption("The Riddler Game")
    while running:
            
            screen.fill("black") # sets screen to default
            screen.blit(back_ground, (0, 0))

            play_mouse_pos = pygame.mouse.get_pos() # gets mouse position 
            play_text = mainfont.render("Riddler's Games", True, redtextcolor)
            play_rect = play_text.get_rect(center = (540, 100))
            screen.blit(play_text, play_rect) # blits text to the screen

            game_riddle = riddle_font.render(riddles[0], 1, whitetextcolor) 
            screen.blit(game_riddle, riddle_coord) # blits the riddle to the screen

            level = 1
            level_label = level_lives_font.render(f"Level: {level}", 1, whitetextcolor)
            screen.blit(level_label, level_coord) # blits the level to the screen
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # if red x is clicked, closes game
                    pygame.quit()
                    sys.exit() 
                if event.type == pygame.KEYDOWN: # if keydown is pressed, changes user text
                    if event.key == pygame.K_BACKSPACE: # if backspace is pressed, last entry in user text string is deleted
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN: # if user clicks after inputting an answer
                    if user_text == "a cold": 
                        print("Thats Correct")
                        user_text = "" # resets user text to blank text box
                        Riddle_1() # moves to next riddle
                    else:
                        Game_Over() # if answer is wrong on mouse click, game over
                
                    
            pygame.draw.rect(screen, whitetextcolor, input_rect, 2)
            text_surface = Textfont.render(user_text, True, whitetextcolor)
            screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
            input_rect.w = max(100, text_surface.get_width() + 15)
            #print(user_text)
            pygame.display.flip()
            clock.tick(60)
'''
The remaining functions do the same process as Riddle_0()
Commenting on each would be redundant. So I will highlight the changes in each of the following functions
Riddle_1() thru Riddle_9() add one to the level count, change the index of the riddles list to print the correct
riddle to the screen, on MOUSECLICK move to the next approperiate function, or if the answer is wrong user is sent to the Game_Over function
If the user is able to answer all 10 riddles correctly, you can see in Riddle_9 that the user is sent to GameWon()
'''              
def Riddle_1():
    global user_text
    pygame.display.set_caption("The Riddler Game")
    while running:
            
            screen.fill("black") # sets screen to default
            screen.blit(back_ground, (0, 0))

            play_mouse_pos = pygame.mouse.get_pos()
            play_text = mainfont.render("Riddler's Games", True, redtextcolor)
            play_rect = play_text.get_rect(center = (540, 100))
            screen.blit(play_text, play_rect)

            game_riddle = riddle_font.render(riddles[1], 1, whitetextcolor)
            screen.blit(game_riddle, riddle_coord)

            level = 2
            level_label = level_lives_font.render(f"Level: {level}", 1, whitetextcolor)
            screen.blit(level_label, level_coord)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if user_text == "a rubber band":
                        print("Thats Correct")
                        user_text = ""
                        Riddle_2()
                    else:
                        Game_Over()       
            pygame.draw.rect(screen, whitetextcolor, input_rect, 2)
            text_surface = Textfont.render(user_text, True, whitetextcolor)
            screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
            input_rect.w = max(100, text_surface.get_width() + 15)
            #print(user_text)
            pygame.display.flip()
            clock.tick(60)  

def Riddle_2():
    global user_text
    pygame.display.set_caption("The Riddler Game")
    while running:
            
            screen.fill("black") # sets screen to default
            screen.blit(back_ground, (0, 0))

            play_mouse_pos = pygame.mouse.get_pos()
            play_text = mainfont.render("Riddler's Games", True, redtextcolor)
            play_rect = play_text.get_rect(center = (540, 100))
            screen.blit(play_text, play_rect)

            game_riddle = riddle_font.render(riddles[2], 1, whitetextcolor)
            screen.blit(game_riddle, riddle_coord)

            level = 3
            level_label = level_lives_font.render(f"Level: {level}", 1, whitetextcolor)
            screen.blit(level_label, level_coord)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if user_text == "a stamp":
                        print("Thats Correct")
                        user_text = ""
                        Riddle_3()
                    else:
                        Game_Over()
                
                    
            pygame.draw.rect(screen, whitetextcolor, input_rect, 2)
            text_surface = Textfont.render(user_text, True, whitetextcolor)
            screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
            input_rect.w = max(100, text_surface.get_width() + 15)
            #print(user_text)
            pygame.display.flip()
            clock.tick(60)

def Riddle_3():
    global user_text
    pygame.display.set_caption("The Riddler Game")
    while running:
            
            screen.fill("black") # sets screen to default
            screen.blit(back_ground, (0, 0))

            play_mouse_pos = pygame.mouse.get_pos()
            play_text = mainfont.render("Riddler's Games", True, redtextcolor)
            play_rect = play_text.get_rect(center = (540, 100))
            screen.blit(play_text, play_rect)

            game_riddle = riddle_font.render(riddles[3], 1, whitetextcolor)
            screen.blit(game_riddle, riddle_coord)

            level = 4
            level_label = level_lives_font.render(f"Level: {level}", 1, whitetextcolor)
            screen.blit(level_label, level_coord)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if user_text == "a mushroom":
                        print("Thats Correct")
                        user_text = ""
                        Riddle_4()
                    else:
                        Game_Over()
                
                    
            pygame.draw.rect(screen, whitetextcolor, input_rect, 2)
            text_surface = Textfont.render(user_text, True, whitetextcolor)
            screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
            input_rect.w = max(100, text_surface.get_width() + 15)
            #print(user_text)
            pygame.display.flip()
            clock.tick(60)

def Riddle_4():
    global user_text
    pygame.display.set_caption("The Riddler Game")
    while running:
            
            screen.fill("black") # sets screen to default
            screen.blit(back_ground, (0, 0))

            play_mouse_pos = pygame.mouse.get_pos()
            play_text = mainfont.render("Riddler's Games", True, redtextcolor)
            play_rect = play_text.get_rect(center = (540, 100))
            screen.blit(play_text, play_rect)

            game_riddle = riddle_font.render(riddles[4], 1, whitetextcolor)
            screen.blit(game_riddle, riddle_coord)

            level = 5
            level_label = level_lives_font.render(f"Level: {level}", 1, whitetextcolor)
            screen.blit(level_label, level_coord)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if user_text == "the letter g":
                        print("Thats Correct")
                        user_text = ""
                        Riddle_5()
                    else:
                        Game_Over()
                
                    
            pygame.draw.rect(screen, whitetextcolor, input_rect, 2)
            text_surface = Textfont.render(user_text, True, whitetextcolor)
            screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
            input_rect.w = max(100, text_surface.get_width() + 15)
            #print(user_text)
            pygame.display.flip()
            clock.tick(60)

def Riddle_5():
    global user_text
    pygame.display.set_caption("The Riddler Game")
    while running:
            
            screen.fill("black") # sets screen to default
            screen.blit(back_ground, (0, 0))

            play_mouse_pos = pygame.mouse.get_pos()
            play_text = mainfont.render("Riddler's Games", True, redtextcolor)
            play_rect = play_text.get_rect(center = (540, 100))
            screen.blit(play_text, play_rect)

            game_riddle = riddle_font.render(riddles[5], 1, whitetextcolor)
            screen.blit(game_riddle, riddle_coord)

            level = 6
            level_label = level_lives_font.render(f"Level: {level}", 1, whitetextcolor)
            screen.blit(level_label, level_coord)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if user_text == "nothing":
                        print("Thats Correct")
                        user_text = ""
                        Riddle_6()
                    else:
                        Game_Over()
                
                    
            pygame.draw.rect(screen, whitetextcolor, input_rect, 2)
            text_surface = Textfont.render(user_text, True, whitetextcolor)
            screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
            input_rect.w = max(100, text_surface.get_width() + 15)
            #print(user_text)
            pygame.display.flip()
            clock.tick(60)

def Riddle_6():
    global user_text
    pygame.display.set_caption("The Riddler Game")
    while running:
            
            screen.fill("black") # sets screen to default
            screen.blit(back_ground, (0, 0))

            play_mouse_pos = pygame.mouse.get_pos()
            play_text = mainfont.render("Riddler's Games", True, redtextcolor)
            play_rect = play_text.get_rect(center = (540, 100))
            screen.blit(play_text, play_rect)

            game_riddle = riddle_font.render(riddles[6], 1, whitetextcolor)
            screen.blit(game_riddle, riddle_coord)

            level = 7
            level_label = level_lives_font.render(f"Level: {level}", 1, whitetextcolor)
            screen.blit(level_label, level_coord)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if user_text == "light":
                        print("Thats Correct")
                        user_text = ""
                        Riddle_7()
                    else:
                        Game_Over()
                
                    
            pygame.draw.rect(screen, whitetextcolor, input_rect, 2)
            text_surface = Textfont.render(user_text, True, whitetextcolor)
            screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
            input_rect.w = max(100, text_surface.get_width() + 15)
            #print(user_text)
            pygame.display.flip()
            clock.tick(60)

def Riddle_7():
    global user_text
    pygame.display.set_caption("The Riddler Game")
    while running:
            
            screen.fill("black") # sets screen to default
            screen.blit(back_ground, (0, 0))

            play_mouse_pos = pygame.mouse.get_pos()
            play_text = mainfont.render("Riddler's Games", True, redtextcolor)
            play_rect = play_text.get_rect(center = (540, 100))
            screen.blit(play_text, play_rect)

            game_riddle = riddle_font.render(riddles[7], 1, whitetextcolor)
            screen.blit(game_riddle, riddle_coord)

            level = 8
            level_label = level_lives_font.render(f"Level: {level}", 1, whitetextcolor)
            screen.blit(level_label, level_coord)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if user_text == "jared":
                        print("Thats Correct")
                        user_text = ""
                        Riddle_8()
                    else:
                        Game_Over()
                
                    
            pygame.draw.rect(screen, whitetextcolor, input_rect, 2)
            text_surface = Textfont.render(user_text, True, whitetextcolor)
            screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
            input_rect.w = max(100, text_surface.get_width() + 15)
            #print(user_text)
            pygame.display.flip()
            clock.tick(60)

def Riddle_8():
    global user_text
    pygame.display.set_caption("The Riddler Game")
    while running:
            
            screen.fill("black") # sets screen to default
            screen.blit(back_ground, (0, 0))

            play_mouse_pos = pygame.mouse.get_pos()
            play_text = mainfont.render("Riddler's Games", True, redtextcolor)
            play_rect = play_text.get_rect(center = (540, 100))
            screen.blit(play_text, play_rect)

            game_riddle = riddle_font.render(riddles[8], 1, whitetextcolor)
            screen.blit(game_riddle, riddle_coord)

            level = 9
            level_label = level_lives_font.render(f"Level: {level}", 1, whitetextcolor)
            screen.blit(level_label, level_coord)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if user_text == "a piano":
                        print("Thats Correct")
                        user_text = ""
                        Riddle_9()
                    else:
                        Game_Over()
             
            pygame.draw.rect(screen, whitetextcolor, input_rect, 2)
            text_surface = Textfont.render(user_text, True, whitetextcolor)
            screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
            input_rect.w = max(100, text_surface.get_width() + 15)
            #print(user_text)
            pygame.display.flip()
            clock.tick(60)

def Riddle_9():
    global user_text
    pygame.display.set_caption("The Riddler Game")
    while running:
            
            screen.fill("black") # sets screen to default
            screen.blit(back_ground, (0, 0))

            play_mouse_pos = pygame.mouse.get_pos()
            play_text = mainfont.render("Riddler's Games", True, redtextcolor)
            play_rect = play_text.get_rect(center = (540, 100))
            screen.blit(play_text, play_rect)

            game_riddle = riddle_font.render(riddles[9], 1, whitetextcolor)
            screen.blit(game_riddle, riddle_coord)

            level = 10
            level_label = level_lives_font.render(f"Level: {level}", 1, whitetextcolor)
            screen.blit(level_label, level_coord)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if user_text == "a clock":
                        print("Thats Correct")
                        Game_Won()
                    else:
                        Game_Over()
                
                    
            pygame.draw.rect(screen, whitetextcolor, input_rect, 2)
            text_surface = Textfont.render(user_text, True, whitetextcolor)
            screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
            input_rect.w = max(100, text_surface.get_width() + 15)
            pygame.display.flip()
            clock.tick(60)

def Game_Over():
    pygame.display.set_caption("Game Over")

    while running:
        screen.fill("black") # Sets screen and background
        screen.blit(back_ground, (0,0))

        GameOver_text = mainfont.render("Game Over", True, redtextcolor)
        GameOver_rect = GameOver_text.get_rect(center = (540, 100))

        screen.blit(GameOver_text, GameOver_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # exits GUI when red X is pressed
                sys.exit()
        pygame.display.update()


def Game_Won():
    pygame.display.set_caption("You Won The Game")

    while running:
        screen.fill("black") # Sets screen and background
        screen.blit(back_ground, (0,0))

        GameWon_text = mainfont.render("YOU WIN!!!", True, redtextcolor)
        GameWon_rect = GameWon_text.get_rect(center = (540, 100))

        screen.blit(GameWon_text, GameWon_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # exits GUI when red X is pressed
                sys.exit()
        pygame.display.update()

print("Welcome to The Riddler Game")
main_menu()   
    