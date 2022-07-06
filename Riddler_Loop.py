from lib2to3.pgen2.token import NEWLINE
import random

answers = ["an umbrella", "a rubber band", "a stamp", "a mushroom", "the letter g", 
                "nothing", "light", "jared", "a piano", "a clock", "a mountain", "wind", "time","teeth", "an egg"]

riddles = ["What can you catch, but not throw?", "What kind of band never plays music?", "What can travel around the world without leaving its corner?",
            "What kind of room has no doors or windows?", "What is the end of everything?", "Poor People have it. Rich people need it. If you eat it you die. What is it?",
            "What can fill a room but takes up no space?", "Jared’s father has three sons: Snap, Crackle, and..?", "What has many keys but can’t open a single lock?",
            "What has hands but can’t clap?", "What has roots as nobody sees, Is taller than trees, Up, up it goes, And yet never grows?", "Voiceless it cries, Wingless flutters, Toothless bites, Mouthless mutters",
             "This thing all things devours: Birds, beasts, trees, flowers; Gnaws iron, bites steel; Grinds hard stones to meal; Slays king, ruins town, And beats high mountain down.",
             "Thirty white horses on a red hill, First they champ, Then they stamp, Then they stand still", "A box without hinges, key, or lid, Yet golden treasure inside is hid"]

def riddle_game():
    LIVES = 3
    LEVEL_COUNTER = 1

    print("Welcome to the Riddle Game \n\n" 
        + "\t[Instructions]\n\nYou will be asked to slove a series of riddles.\nStarting with 3 lives, you must answer at least 10 riddles correctly to win the game.")
    print("Each time you answer incorrectly, you will lose a life\n" + "And if all lives are lost, you will lose the game")
    play_game = input("\n\nWould you like to play a game?(Y or N) ")
    play_game = play_game.lower()

    print("\nLets Begin")
    while play_game == "y":
        for i in range(len(riddles)):
            print("\nRiddle number",LEVEL_COUNTER)
            print(riddles[i])
            user_answer = input("Answer: ")
            user_answer = user_answer.lower()
            if user_answer == answers[i]:
                print("\nThats correct!") 
                LEVEL_COUNTER = LEVEL_COUNTER + 1
                if LEVEL_COUNTER >= 10:
                    print("CONGRATS, you have defeated The Riddler")
                    play_game = "n"
                    break
            else:
                LIVES = LIVES - 1
                print("\nThat answer is incorrect")
                print("You have", LIVES, "lives reamining")
                LEVEL_COUNTER = LEVEL_COUNTER + 1
                
                if LIVES == 0: 
                    print("You have run out of lives, You Lose")
                    play_game = "n"
                    break
                
                
 
riddle_game()

    
    

