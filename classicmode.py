from screenwriting.screenwriting import dur_type
from stab import stabgame
import random


def classicmode():
    murderno = random.randint(1, 5)
    if murderno == 1:
        murderer_in_bathroom = True
    else:
        murderer_in_bathroom = False
    bathroom_door = "closed"
    front_door = "closed"
    trousers = "on"
    position = "corridor"
    toilet_lid = "down"
    on_toilet = "no"
    help_count = 0
    pee = "in"
    cmd_count = 0
    cmd_max = 10
    tumblrmeme = "https://www.tumblr.com/blog/view/izeas/665384914566447104"
    SUCM = "off"
    hints = ["dont use words like 'the' or 'a'.", "dont use capital letters.", "keep your commands short, but specific.",
             "if you were thinking of typing something like 'open door' or 'go to toilet', heres one thing you should know: its not that simple.", "try typing 'help'."]
    mood = "willing"

    dur_type("Welcome to Don't Pee Yourself!")
    dur_type("Allow me to set the scene.")
    dur_type("You need to pee. The door to the bathroom is right in front of you, but don't let that fool you into thinking this to be trivial. It's not. You need to do it like an algorithm. And that means specifying. EVERY. SINGLE. STEP. Also, you are wearing trousers, and are unable to pee standing up. The front door of your house is to your left, about two metres away. Just outside your house is a forest containing lots of trees.")
    while pee == "in":
        dur_type("enter a command")
        command = input()
        cmd_count = cmd_count + 1
        if cmd_count == (cmd_max / 2) or cmd_count == (cmd_max / 2 - 0.5):
            dur_type("it hurts! you gotta get the pee out!")
        if cmd_count >= cmd_max:
            pee = "out"
            dur_type("you couldn't hold it in any longer.")

        if command == "remove trousers" or command == "take off trousers" or command == "pull down trousers" or command == "unequip trousers":
            trousers = "off"
            dur_type("your trousers have been removed.")

        elif "pants" in command:
            dur_type("you're not american. call them trousers.")

        elif command == "push bathroom door":
            if position == "corridor":
                if bathroom_door == "closed":
                    dur_type("ngh! the door won't move!")
                elif bathroom_door == "open":
                    door = "closed"
                    dur_type("you just closed the door again.")
                elif bathroom_door == "gone":
                    dur_type("there is no door left to push.")
            elif position == "bathroom":
                if bathroom_door == "closed":
                    dur_type("ngh! it won't budge!")
                elif bathroom_door == "open":
                    dur_type("you couldn't reach to push the door any further.")
                elif bathroom_door == "gone":
                    dur_type("there is no door to push.")
            elif position == "forest":
                dur_type("there's no door in the forest.")

        elif command == "pull bathroom door":
            if position == "corridor":
                if bathroom_door == "closed":
                    door = "open"
                    dur_type("the bathroom door is now open")
                elif bathroom_door == "open":
                    door = "gone"
                    dur_type("you pulled the door off its hinges.")
                elif bathroom_door == "gone":
                    dur_type("but there was no bathroom door to pull.")
            elif position == "bathroom":
                if bathroom_door == "closed":
                    dur_type("you can't pull the door any further")
                elif bathroom_door == "open":
                    door = "closed"
                    dur_type(
                        "you closed the door, although you didn't really need to, because you live alone.")
                elif bathroom_door == "gone":
                    dur_type("there is no door to pull.")
            elif position == "forest":
                dur_type("there's no door in the forest.")

        elif command == "walk forwards" or command == "run forwards":
            if bathroom_door == "closed":
                dur_type("the door is closed")
            else:
                position = "bathroom"
                dur_type("you are now in the bathroom")
                if murderer_in_bathroom == True:
                    dur_type(
                        "also in the bathroom is a murderer. you are now dead.")
                    dur_type(
                        "As the cause of your death was a bullet, you start to pee uncontrollably.")
                    pee = "out"

        elif command == "lift toilet lid":
            if position == "bathroom":
                toilet_lid = "up"
                dur_type("the toilet lid is now up")
            else:
                dur_type("you're too far away")

        elif command == "lift lid" or command == "push door" or command == "pull door":
            dur_type("which one?")

        elif command == "sit" or command == "sit down":
            if position == "bathroom":
                on_toilet = "yes"
                dur_type("you sit on the toilet.")
            else:
                dur_type("you sit on the floor, then stand back up.")

        elif command == "pee" or command == "peepee" or command == "wee" or command == "weewee" or command == "pee pee" or command == "wee wee" or command == "piss" or command == "excrete" or command == "urinate":
            pee = "out"

        elif command == "73nfiwgtehvfu YTI HyuDu484 836 ri*)!+&":
            if mood == "willing" or mood == "scared":
                cmd_max = cmd_max * 2
                if mood == "willing":
                    dur_type("you can now hold your pee in much longer.")
                elif mood == "scared":
                    dur_type(
                        "Secret code accepted, Master. Command Maximum doubled, Master. You can now hold your urine inside of you twice as long, Master.")
                elif mood == "angry":
                    print(
                        "i know there was such a low chance of you getting that (or you cheated), but im not gonna help you.")

        elif command == "help me please" or command == "please help me":
            if help_count > 2:
                dur_type(
                    "you have already used this command up to your limit of 3 times.")
            else:
                help_count = help_count + 1
                dur_type("position: "+position)
                dur_type("trousers: "+trousers)
                dur_type("bathroom door: "+bathroom_door)
                dur_type("front door: "+front_door)
                dur_type("on toilet: "+on_toilet)
                cmd_left = (cmd_max - cmd_count)
                dur_type("commands remaining: "+str(cmd_left))
        elif command == "help" or command == "help please" or command == "please help":
            dur_type("who needs help?")

        elif command == "help me":
            dur_type("learn some manners, and maybe i will")

        elif command == "show me a meme":
            dur_type("I couldn't get the image thing to work, so here's the link:")
            print(tumblrmeme)

        elif command == "show me some memes":
            dur_type("I can't, but try typing 'me.me' into a new tab.")

        elif command == "enable super-easy CHEAT mode":
            if mood == "willing" or mood == "scared":
                cmd_max = 999999999999999999999999999
                SUCM = "on"
            if mood == "willing":
                dur_type(
                    "super-easy CHEAT mode enabled. You can now hold your pee in WAAAY longer.")
            elif mood == "scared":
                dur_type(
                    "Okay, Master. Useful Help mode has been enabled, Master. You can now hold your urine inside of you much longer, Master.")
            elif mood == "angry":
                dur_type(
                    "first you acted absolutely HORRIBLE to me, and now you want to CHEAT? NO!")

        elif command == "walk" or command == "run":
            dur_type("ok but where?")

        elif command == "jump":
            dur_type("the pee loosened a bit. You can't hold it in as long now.")
            cmd_max = cmd_max - 3

        elif command == "run away":
            position = "forest"
            dur_type("you run into a nearby forest.")

        elif command == "give me a hint" or command == "give me a tip" or command == "give me a clue":
            if mood == "willing":
                dur_type(hints[random.randint(0, 3)])
            elif mood == "scared":
                dur_type(
                    "i already told you how to win in just 3 commands, do you really need more?")

        elif command == "GIVE ME A GOSHDARN FRICKING USEFUL HINT RIGHT NOW BEFORE I STAB YOU! I KNOW WHERE YOU LIVE AND WILL NOT HESITATE TO GO OVER TO YOUR HOUSE AND STAB YOU IF YOU DO NOT GIVE ME A USEFUL HINT IMMEDIATELY!!!":
            if mood == "willing":
                interog_ans = random.randint(1, 2)
                if interog_ans == 1:
                    dur_type(
                        "ok! ok! ill give you a hint! type 'run away', then 'remove trousers', then 'pee' and you'll win.")
                    mood = "scared"
                else:
                    mood = "angry"
                    dur_type("no. im not gonna help you. i know you wont stab me. i am your computer after all. you wouldnt stab your computer. im too expensive to replace. and i DEFINITELY wont help you with THAT attitude!")
            elif mood == "scared":
                dur_type(
                    "i already told you how to win in just 3 commands, just scroll up and youll see it!")
            elif mood == "angry":
                dur_type("i already said no, and im gonna say it again: no.")

        elif command == "no u":
            dur_type("oh, you want ME to enter a command? ok.")
            dur_type("run away", 0.666)
            dur_type("your computer ran away.", 0.33)
            dur_type("commands will not work now.")
            dur_type("so you'll be stuck here...", 0.33)
            dur_type("F O R E V E R .", 0.666)
            while 1 == 1:
                dur_type("HA", 0, "HAHA")

        elif command == "stab computer":
            stabgame()
            break

        elif command == "go to toilet" or command == "use toilet" or command == "pee in toilet":
            dur_type("one does not simply '" + command + ".'")

        elif command == "walk upstairs" or command == "run upstairs" or command == "go upstairs":
            dur_type("your house only has one floor.")

        else:
            dur_type("invalid command")
        dur_type("*-<_%^#=~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        if pee == "out":
            if trousers == "on":
                if SUCM == "on":
                    print("wow. you CHEATED and you didnt even win.")
                else:
                    dur_type(""" _____  ___________  _____  
|  _  ||  _  | ___ \/  ___| 
| | | || | | | |_/ /\ `--.  
| | | || | | |  __/  `--. \ 
\ \_/ /\ \_/ / |    /\__/ / 
 \___/  \___/\_|    \____(_)
 ending 1 of 5: bad ending
 you peed yourself.                           
                            """)
            if (trousers == "off" and on_toilet == "no"):
                if SUCM == "on":
                    print(
                        "I mean, I GUESS you won, but I would've expected better from a CHEATER.")
                else:
                    if position == "bathroom":
                        dur_type(""" _    _ _____ _   _ ___                 
| |  | |_   _| \ | |__ \ 
| |  | | | | |  \| |  ) |
| |/\| | | | | . ` | / / 
\  /\  /_| |_| |\  ||_|  
 \/  \/ \___/\_| \_/(_)  
 ending 2 of 5: good enough ending
 you couldn't get to the toilet, but at least you didn't pee yourself!                        
                         """)
                    elif position == "forest":
                        dur_type(""" _   _ _____ _____  _____ _ 
| \ | |_   _/  __ \|  ___| |
|  \| | | | | /  \/| |__ | |
| . ` | | | | |    |  __|| |
| |\  |_| |_| \__/\| |___|_|
\_| \_/\___/ \____/\____/(_)
 ending 3 of 5: adventurous ending
 you peed on a tree.                           
                            """)
            if (trousers == "off" and on_toilet == "yes" and toilet_lid == "down"):
                if SUCM == "on":
                    print(
                        "you did most of the things required for a proper win, but i still wouldve expected better from a CHEATER.")
                else:
                    if position == "bathroom":
                        dur_type(""" _    _ _____ _   _ ___                 
| |  | |_   _| \ | |__ \ 
| |  | | | | |  \| |  ) |
| |/\| | | | | . ` | / / 
\  /\  /_| |_| |\  ||_|  
 \/  \/ \___/\_| \_/(_)  
 ending 4 of 5: forgetful ending
 i mean, technically you didn't pee yourself, you just peed on the toilet lid.
                         """)
            if (trousers == "off" and on_toilet == "yes" and toilet_lid == "up"):
                if SUCM == "on":
                    print("CHEAT. you dont deserve fancy big letters.")
                else:
                    dur_type(""" _    _ _____ _   _ _ 
| |  | |_   _| \ | | |
| |  | | | | |  \| | |
| |/\| | | | | . ` | |
\  /\  /_| |_| |\  |_|
 \/  \/ \___/\_| \_(_)
 ending 5 of 5: good ending                     
 congrats! you peed in the toilet!                     
                                        """)
