# group project, i did the code entirely

def key_unlock(glb, door):
    glb[door] = True

def puzzles(puzzle_type, prompt_msg, correct_ans, pass_dialogue, fail_dialogue):
    print(prompt_msg)
    answer = input().strip().lower()
    if answer.lower() == correct_ans.lower():
        print(pass_dialogue)
        return "SUCCESS"
    else:
        print(fail_dialogue)
        return "FAIL"

def main_game():
    glb = {
        'door1': True,
        'door2': False,
        'door3': False,
        'door4': False,
        'door5': False,
        'door6': False,
        'door7': False,
        'secret': False
    }
    doors_solved = ['door1']
    game_func = True
    is_alive = True
    while game_func and is_alive:
        print("You are now in the main room. Select a room to enter.")
        print("SELECT: door 1 | door 2 | door 3 | door 4 | door 5 | door 6 | door 7 | exit")
        choice = input().strip()
        if choice == "exit":
            game_func = False
            print("You exited the game.")
            break
        elif choice == "door 1":
            if 'door1' in doors_solved:
                print("You entered the first room, and the door behind you had closed abruptly. What came into your eyes was a hauntingly beautiful landscape, filled with green and nature - a dense forest cloaked with eerie stillness. Directly in front of you were rocks arranged in a strange but oddly orderly fashion, and in front of them is a device with a keyboard and a tiny screen. It looked like a morse code puzzle which looked like this:")
                puzzle_type = "morse code"
                prompt_msg = "... - --- -. . | What are the rocks trying to tell you? "
                correct_ans = "stone"
                pass_dialogue = "The code was correct, you heard rustling sounds coming from the trees and something shiny fell from it. It was a key, most likely the key to the next room."
                fail_dialogue = "The stones ganged up and turned into a golem and smacked you across the face and you died."
                result = puzzles(puzzle_type, prompt_msg, correct_ans, pass_dialogue, fail_dialogue)
                if result == "SUCCESS":
                    key_unlock(glb, "door2")
                    doors_solved.append('door2')
                    print("Congratulations! You solved the puzzle. Door 2 is now unlocked.\n")
                else:
                    print("You failed to solve the puzzle.")
                    is_alive = False
            else:
                print("Door is locked. You need to solve the previous door first.")
        elif choice == "door 2":
            if 'door2' in doors_solved:
                print("Similiar to the first room, the door behind you came to a close all of a sudden. You were then greeted with a harsh and unforgiving sight - a vast desert sprawled before you, with barren landscape stretching to the horizon. The sunlight was not natural and you feel your skin burning under the blazing waves of heat. Amidst the barren expanse, a series of intricate markings etched into the sand, forming a short line of words and another answering device beside it. It seems like it might be a riddle this time. ")
                puzzle_type = "riddle"
                prompt_msg = "I walk on 4 legs in the morning, 2 legs at noon, and 3 legs at night. | What am I?"
                correct_ans = "human"
                pass_dialogue = "The fabric of the desert started to shift and rearrange itself, forming a hole spiralling downwards in the middle of the sand. You moved towards raging sand and grab the shiny key that was in the heart of the sand. "
                fail_dialogue = "The sand turns into a golem and smack you across the face and killed you."
                result = puzzles(puzzle_type, prompt_msg, correct_ans, pass_dialogue, fail_dialogue)
                if result == "SUCCESS":
                    key_unlock(glb, "door3")
                    doors_solved.append('door3')
                    print("Congratulations! You solved the puzzle. Door 3 is now unlocked.\n")
                else:
                    print("You failed to solve the puzzle.")
                    is_alive = False
            else:
                print("Door is locked. You need to solve the previous door first.")
        elif choice == "door 3":
            if 'door3' in doors_solved:
                print("Again, the door closes behind you with a loud bang. You're starting to get used to this scene. Upon entering, you came across a scene that you always wanted to forget. It was the classroom from your old high school. What greeted you was the face of your least favourite, or rather hated teacher, your computer science teacher, Mr Hasntven. He held a metal cane on his hand, with a sinister and uncanny smile hung on his face. You started to have PTSD (flashbacks) and started shivering. In fear, you sat down on one of the seats as instructed by Mr. (insert name), he handed you a paper with a question on it while starting the timer at the same time. Nervously, you started to solve the question that was written on the paper. ")
                puzzle_type = "maths"
                prompt_msg = "6 + 5(3/5) = | What's the answer?"
                correct_ans = "9"
                pass_dialogue = "Mr. Hasntven starts slow clapping as he starts praising you for your answer with the most unnatural tone you've ever heard. It was then you realised it was not actually him, and you actually had nothing to be scared of. Suddenly, Mr. Hasntven gets launched into the ceiling, leaving a hole in which the key then falls from hole blasted by him."
                fail_dialogue = "Mr Hasntven turns unnaturally red, as if getting angry, and his head started expanding ad eventually explodes. You die due to the explosion. "
                result = puzzles(puzzle_type, prompt_msg, correct_ans, pass_dialogue, fail_dialogue)
                if result == "SUCCESS":
                    key_unlock(glb, "door4")
                    doors_solved.append('door4')
                    print("Congratulations! You solved the puzzle. Door 4 is now unlocked.\n")
                else:
                    print("You failed to solve the puzzle.")
                    is_alive = False
            else:
                print("Door is locked. You need to solve the previous door first.")
        elif choice == "door 4":
            if 'door4' in doors_solved:
                print("What came into your eyes this time was once again something familiar. You looked up and see a familiar skyline of your town, but it seemed a little different from usual. The area was eerily silent; ownerless cars, no people, no birds, and only inanimate buildings.")
                print("You see a trash can, a car, and a cardboard box, and an unfamiliar building The door behind you is locked.")
                q = True
                while q:
                    print("What do you think about approaching? \nOptions: trash can | car | cardboard box")
                    option = input().strip().lower()
                    if option == "trash can":
                        print("Look through trash? (yes/no)")
                        answer = input().strip().lower()
                        if answer == "yes":
                            print("Absolutely disgusting. You receive a yellow banana.")
                        else:
                            print("Crisis averted.")
                    elif option == "car":
                        print("Search the car? (yes/no)")
                        answer = input().strip().lower()
                        if answer == "yes":
                            print("The car explodes, you died.")
                            q = False
                            is_alive = False
                            break
                        else:
                            print("You go back to the entrance.")
                    elif option == "cardboard box":
                        print("Search? (yes/no)")
                        answer = input().strip().lower()
                        if answer == "yes":
                            print("You found the key inside the cardboard box, but nothing else happened. You start wondering: Was it supposed to be this easy?")
                            print("Regardless, you went back to the entrance confused.")
                            key_unlock(glb, "door5")
                            doors_solved.append('door5')
                            print("Congratulations! You found the key and unlocked the door.\n")
                            q = False
                        else:
                            print("You go back to the entrance. ")
                    elif option == "door":
                        if 'door5' in doors_solved:
                            key_unlock(glb, "door6")
                            doors_solved.append('door6')
                            print("Congratulations! You unlocked the door.\n")
                            q = False
                        else:
                            print("The door is locked. You need to find the key first.")
                    elif option == "building" :
                            q = False
                            key_unlock(glb,"door4")
                            doors_solved.append("door4")
                            print("\nYou've entered a secret room")
                            print("""
░██████╗███████╗░█████╗░██████╗░███████╗████████╗
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝
╚█████╗░█████╗░░██║░░╚═╝██████╔╝█████╗░░░░░██║░░░
░╚═══██╗██╔══╝░░██║░░██╗██╔══██╗██╔══╝░░░░░██║░░░
██████╔╝███████╗╚█████╔╝██║░░██║███████╗░░░██║░░░
╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░""")
                            print("You arrive at a carnival . It was a place that was filled with you childhood memories. Even though this was supposed to make you feel nostalgic and bright, you can't help but feel uneasy")
                            print("While exploring the carnival, you see a sign pointing to the left")
                            print("-> Left")
                            print("Do you follow the sign? (yes/no)")
                            answer3 = input().strip().lower()
                            if answer3 == "yes":
                                m = True
                                print("You follow the sign, and it leeads you to a locked door. You decided to search the area for the key to unlock to door.")
                                while m:
                                    print("Where do you search?")
                                    print("Game Booth | Food Stall")
                                    option = input().strip().lower()
                                    if option == "game booth":
                                        print("Explore the game booths? (yes/no)")
                                        answerq = input().strip().lower()
                                        if answerq == "yes":
                                            print("You found a stuffed rabbit with a button on the back. Once you press it, the stuff animal gives out a smile and you died.")
                                            m = False
                                            is_alive = False
                                        else:
                                            print("You don't explore the game booth.")
                                    elif option == "food stall":
                                        print("Search the food stall? (yes/no)")
                                        answero = input().strip().lower()
                                        if answero == "yes":
                                            print("You found the key. You then opened the door with the key. Upon twisting the door knob and swinging the door open, a wave of bright light struck into your vision and you closed your eyes. After opening your eyes, you woke up in your own room, and realised all of this was just a dream. ")
                                            key_unlock(glb, "secret")
                                            doors_solved.append('secret')
                                            print("Congratulations! You have completed the game.")
                                            print("Thank you for playing! ")
                                            completion_dialogue = "Congratulations! You have successfully completed all the puzzles and unlocked all the doors."
                                            print(completion_dialogue)

                                            restart = input("Do you want to restart the game? (yes/no): ").lower().strip()
                                            if restart == "yes":
                                                main_game()
                                                break
                                            else:
                                                print("You exited the game.")
                                                game_func = False
                                                break
                                            m = False
                                            break
                                        else:
                                            print("You don't explore the food stall.")
                                    else:
                                        print("Invalid option. Try again.")
                            else:
                                print("You continue to walk straight and see a clown standing in front. You thought the clown looked familiar so you got even closer. As you soon as you stood in front of it, it gave out a horrifying smile and stabbed you with a knife. You died. ")
                                is_alive = False
                    else:
                            print("Invalid option. Try again.")
            else:
                print("Door is locked. You need to solve the previous door first.")

        elif choice == "door 5":
            if 'door5' in doors_solved:
                print("You entered the room, and immediately hear a ear-piercing melody of the birthday ong. Your eardrums feel like they could explode anytime. You see a ballroom with a huge sign saying 'Happy Birthday' and a familiar red velvet cake sitting on top of one of the tables. Other than the birthday song sounding a little unusual, the room had no signs of having puzzles or special mechanisms, and the deafening melody was making your eardrums bleed. You try to get out of the room, but the door was locked with an alphabet lock. Maybe the hint was within the birthday song.")
                puzzle_type = "alphabet_lock"
                prompt_msg = "Happy bIrthday to you\nHappy birthday tO you\nHaPpy birthday dear W\nHappy birthday to You."
                correct_ans = "IOPWY"
                pass_dialogue = "The code was correct and the door swung open. You rushed out of the door but tripped over something. It was the key for door 6 just laying in the middle of nowhere."
                fail_dialogue = "After failing the attempt, you started losing your mind as blood comes out from your ears. You exploded and died."
                result = puzzles(puzzle_type, prompt_msg, correct_ans, pass_dialogue, fail_dialogue)
                if result == "SUCCESS":
                    key_unlock(glb, "door6")
                    doors_solved.append('door6')
                    print("Congratulations! You solved the puzzle. Door 6 is now unlocked.")
                else:
                    print("You failed to solve the puzzle.")
            else:
                print("Door is locked. You need to solve the puzzle for the previous door first.")
        elif choice == "door 6":
            if 'door6' in doors_solved:
                print("Door 6 puzzle")
                print("You are in the wild west. You saw some people at a far distance and decided to approach them. When you talked to them, they just stared straight into you and handed you a note.")
                print("Do you take the note?")
                answer1 = input().strip().lower()
                if answer1 == "yes":
                    print("You took the note from their hands . Then, they pulled out revolvers from their backpockets and pointed it at you but didn't shoot. You knew you had to answer the question correctly.")
                    puzzle_type = "riddle"
                    prompt_msg = "Who was the most famous cat in the wild west?"
                    correct_ans = "Kitty Carson"
                    pass_dialogue = "The answer was correct. The 3 men put their revolvers away and one of them handed you a key."
                    fail_dialogue = "The answer was incorret. They 3 men pulled their triggers and put a hole straight through your head. You died."
                    result = puzzles(puzzle_type, prompt_msg, correct_ans, pass_dialogue, fail_dialogue)
                    if result == "SUCCESS":
                        key_unlock(glb, "door7")
                        doors_solved.append('door7')
                        print("Congratulations! You solved the puzzle. Door 7 is now unlocked.")
                    else:
                        print("You failed to solve the puzzle.")
                        is_alive = False
                else:
                    print("- They are unhappy you rejected the note and shot you.")
                    is_alive = False
            else:
                print("Door is locked. You need to solve the previous door first.")
        elif choice == "door 7":
            if 'door7' in doors_solved:
                print("Door 7 puzzle")
                print("You walked into a dark room with eerie and ominous decorations hanging around. This room seems to be a haunted house. You were walking around when you find yourself in a situation where there are 4 potential directions (North,East,South,West) to go. You saw a message painted on the wall in red that seem to be the clue to where to go. ")
                print("A man moves towards the west and then takes a left turn. After covering some distance in that direction, he takes a right turn and finally, takes another right turn.")
                puzzle_type = "direction"
                prompt_msg = "Which direction is the man facing now? (North, East, West, South)"
                correct_ans = "North"
                pass_dialogue = "You walk into a room with nothing except an open door, you walked in and return to the main room. You continue solving the puzzle after puzzle until you eventually realize there’s no end to it. You are now stuck solving puzzles forever. The end."
                fail_dialogue = "A ghostlike entity suddenly pops out and you felt a excruciating pain from your chest. You get a heart attack and died. Weak."
                result = puzzles(puzzle_type, prompt_msg, correct_ans, pass_dialogue, fail_dialogue)
                if result == "SUCCESS":
                    print("Congratulations! You solved the puzzle.")
                    print("Thank you for playing the game!")
                    completion_dialogue = "Congratulations! You have successfully completed all the puzzles and unlocked all the doors."
                    print(completion_dialogue + """
░█████╗░░█████╗░███╗░░██╗░██████╗░██████╗░░█████╗░████████╗░██████╗
██╔══██╗██╔══██╗████╗░██║██╔════╝░██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
██║░░╚═╝██║░░██║██╔██╗██║██║░░██╗░██████╔╝███████║░░░██║░░░╚█████╗░
██║░░██╗██║░░██║██║╚████║██║░░╚██╗██╔══██╗██╔══██║░░░██║░░░░╚═══██╗
╚█████╔╝╚█████╔╝██║░╚███║╚██████╔╝██║░░██║██║░░██║░░░██║░░░██████╔╝
░╚════╝░░╚════╝░╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░""")

                    restart = input("Do you want to restart the game? (yes/no): ").lower().strip()
                    if restart == "yes":
                        main_game()
                    else:
                        print("You exited the game.")
                        game_func = False

                else:
                    print("You failed to solve the puzzle.")
                    is_alive = False
            else:
                print("Door is locked. You need to solve the previous door first.")
        else:
            print("Invalid choice. Try again.")

    print("Thank you for playing the game!")

print("""
██╗░░░░░███████╗░██████╗░███████╗███╗░░██╗██████╗░  ░█████╗░███████╗
██║░░░░░██╔════╝██╔════╝░██╔════╝████╗░██║██╔══██╗  ██╔══██╗██╔════╝
██║░░░░░█████╗░░██║░░██╗░█████╗░░██╔██╗██║██║░░██║  ██║░░██║█████╗░░
██║░░░░░██╔══╝░░██║░░╚██╗██╔══╝░░██║╚████║██║░░██║  ██║░░██║██╔══╝░░
███████╗███████╗╚██████╔╝███████╗██║░╚███║██████╔╝  ╚█████╔╝██║░░░░░
╚══════╝╚══════╝░╚═════╝░╚══════╝╚═╝░░╚══╝╚═════╝░  ░╚════╝░╚═╝░░░░░

██╗░░██╗███████╗██╗░░░░░██████╗░░█████╗░
╚██╗██╔╝██╔════╝██║░░░░░██╔══██╗██╔══██╗
░╚███╔╝░█████╗░░██║░░░░░██║░░██║███████║
░██╔██╗░██╔══╝░░██║░░░░░██║░░██║██╔══██║
██╔╝╚██╗███████╗███████╗██████╔╝██║░░██║
╚═╝░░╚═╝╚══════╝╚══════╝╚═════╝░╚═╝░░╚═╝""")
print("Welcome to the game! Press Enter to start or type 'exit' to quit.")
start_game = input().strip()
if start_game.lower() == "exit":
    print("You exited the game.")
else:
    main_game()
