import sys, time, random
from stab import stabgame
  
door = "closed"
trousers = "on"
position = "corridor"
toilet_lid = "down"
on_toilet = "no"
pee = "in"
cmd_count = 0
cmd_max = 10
tumblrmeme = "https://www.tumblr.com/blog/view/izeas/665384914566447104"
SUCM = "off"
hints = ["dont use words like 'the' or 'a'.","dont use capital letters.","keep your commands short, but specific.","if you were thinking of typing something like 'open door' or 'go to toilet', heres one thing you should know: its not that simple.","try typing 'help'."]
mood = "willing"
# type is a function to print letter by letter.
# Credit to YeeTEDWIN (replit.com)
def type(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.05)
  sys.stdout.write("\n")
  sys.stdout.flush()

def comptype(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.666)
  sys.stdout.write("\n")
  sys.stdout.flush()

def slowtype(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.33)
  sys.stdout.write("\n")
  sys.stdout.flush()

def laugh(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0)
  sys.stdout.write("HA")
  sys.stdout.flush()
  
type("Welcome to Don't Pee Yourself!")
type("WARNING: if you're using speech-to-text, don't play this game. you probably won't win because it's case-sensitive.")
type("Credit to YeeTEDWIN for the function being used right now.")
while pee == "in":
    type("enter a command")
    command = input()
    cmd_count = cmd_count + 1
    if cmd_count == (cmd_max / 2) or cmd_count == (cmd_max / 2 - 0.5):
        type("it hurts! you gotta get the pee out!")
    if cmd_count == cmd_max:
        pee = "out"
        type("you couldn't hold it in any longer.")
    if command == "remove trousers":
        trousers = "off"
        type("your trousers have been removed")
    elif command == "push bathroom door":
        if door == "closed":
            type("ngh! the door won't move!")
        else:
            door = "closed"
            type("you just closed the door again")
    elif command == "pull bathroom door":
        door = "open"
        type("the bathroom door is now open")
    elif command == "enter bathroom" or command == "walk into bathroom" or command == "run into bathroom":
        if door == "closed":
            type("the door is closed")
        else:
            position = "bathroom"
            type("you are now in the bathroom")
    elif command == "lift toilet lid":
        if position == "bathroom":
            toilet_lid = "up"
            type("the toilet lid is now up")
        else:
            type("you're too far away")
    elif command == "lift lid" or command == "push door" or command == "pull door":
        type("which one?")
    elif command == "sit on toilet":
        if position == "bathroom":
            on_toilet = "yes"
            type("you are now on the toilet")
        else:
            type("you sit on the floor, then stand back up because that's not the toilet."
            )
    elif command == "pee":
        pee = "out"
    elif command == "look" or command == "look around":
        type(
            "you are wearing trousers, and there is a pull door  to the bathroom behind you. You live alone, so it's fine if you don't close the door once you're in there."
        )
    elif command == "73nfiwgtehvfu YTI HyuDu484 836 ri*)!+&":
      if mood == "willing" or mood == "scared":
        cmd_max = cmd_max * 2
        if mood == "willing":
          type("you can now hold your pee in much longer")
        elif mood == "scared":
          type("Secret code accepted, Master. Command Maximum doubled, Master. You can now hold your urine inside of you twice as long, Master.")
      elif mood == "angry":
        print("i know there was such a low chance of you getting that (or you cheated), but im not gonna help you.")
    elif command == "help me please" or command == "please help me":
        type(
            "keysmashing usually helps me think, maybe try that? typing look might also help"
        )
    elif command == "help" or command == "help please" or command == "please help":
      type("who needs help?")
    elif command == "help me":
        type("learn some manners, and maybe i will")
    elif command == "show me a meme":
        type("I couldn't get the image thing to work, so here's the link:")
        print(tumblrmeme)
    elif command == "show me some memes":
        type("I can't, but try typing 'me.me' into a new tab")
    elif command == "enable super-easy CHEAT mode":
      if mood == "willing" or mood == "scared":
        cmd_max = 999999999999999999999999999
        SUCM = "on"
        if mood == "willing":
          type("super-easy CHEAT mode enabled. You can now hold your pee in WAAAY longer.")
        elif mood == "scared":
          type("Okay, Master. Useful Help mode has been enabled, Master. You can now hold your urine inside of you much longer, Master.")
        elif mood == "angry":
          type("first you acted absolutely HORRIBLE to me, and now you want to CHEAT? NO!")
    elif command == "walk" or command == "run":
        type("ok but where?")
    elif command == "jump":
        type("the pee loosened a bit. You can't hold it in as long now.")
        cmd_max = cmd_max - 3
    elif command == "run away":
        position = "forest"
        type("you run into a nearby forest.")
    elif command == "give me a hint" or command == "give me a tip" or command == "give me a clue":
      if mood == "willing":
        type(hints[random.randint(0,3)])
      elif mood == "scared":
        type("i already told you how to win in just 3 commands, do you really need more?")
    elif command == "GIVE ME A GOSHDARN FRICKING USEFUL HINT RIGHT NOW BEFORE I STAB YOU! I KNOW WHERE YOU LIVE AND WILL NOT HESITATE TO GO OVER TO YOUR HOUSE AND STAB YOU IF YOU DO NOT GIVE ME A USEFUL HINT IMMEDIATELY!!!":
      if mood == "willing":
        interog_ans = random.randint(1,2)
        if interog_ans == 1:
          type("ok! ok! ill give you a hint! type 'run away', then 'remove trousers', then 'pee' and you'll win.")
          mood = "scared"
        else:
          mood = "angry"
          type("no. im not gonna help you. i know you wont stab me. i am your computer after all. you wouldnt stab your computer. im too expensive to replace. and i DEFINITELY wont help you with THAT attitude!")
      elif mood == "scared":
        type("i already told you how to win in just 3 commands, just scroll up and youll see it!")
      elif mood == "angry":
        type("i already said no, and im gonna say it again: no.")
    elif command == "no u":
      type("oh, you want ME to enter a command? ok.")
      comptype("run away")
      slowtype("your computer ran away.")
      type("commands will not work now.")
      slowtype("so you'll be stuck here...")
      comptype("F O R E V E R .")
      while 1 == 1:
        laugh("HA")
    elif command == "stab computer":
      stabgame()
      break
      
      
    else:
        type("invalid command")

    if pee == "out":
        if trousers == "on":
          if SUCM == "on":
            print("wow. you CHEATED and you didnt even win.")
          else:
            type("you peed yourself.")
            type(""" _____  ___________  _____  
|  _  ||  _  | ___ \/  ___| 
| | | || | | | |_/ /\ `--.  
| | | || | | |  __/  `--. \ 
\ \_/ /\ \_/ / |    /\__/ / 
 \___/  \___/\_|    \____(_)
                            
                            """)
        if (trousers == "off" and on_toilet == "no"):
          if SUCM == "on":
            print("I mean, I GUESS you won, but I would've expected better from a CHEATER.")
          else:
            if position == "bathroom":
              type(
                "you couldn't get to the toilet, but at least you didn't pee yourself!"
              )
              type(""" _    _ _____ _   _ ___                 
| |  | |_   _| \ | |__ \ 
| |  | | | | |  \| |  ) |
| |/\| | | | | . ` | / / 
\  /\  /_| |_| |\  ||_|  
 \/  \/ \___/\_| \_/(_)  
                         
                         """)
            elif position == "forest":
              type("you peed on a tree.")
              type(""" _   _ _____ _____  _____ _ 
| \ | |_   _/  __ \|  ___| |
|  \| | | | | /  \/| |__ | |
| . ` | | | | |    |  __|| |
| |\  |_| |_| \__/\| |___|_|
\_| \_/\___/ \____/\____/(_)
                            
                            """)
        if (trousers == "off" and on_toilet == "yes" and toilet_lid == "down"):
          if SUCM == "on":
            print("you did most of the things required for a proper win, but i still wouldve expected better from a CHEATER.")
          else:
            if position == "bathroom":
              type(
                "your trousers were off, and you were on the toilet, but you forgot to lift the lid. I mean, I guess you didn't pee yourself!"
            )
            type(""" _    _ _____ _   _ ___                 
| |  | |_   _| \ | |__ \ 
| |  | | | | |  \| |  ) |
| |/\| | | | | . ` | / / 
\  /\  /_| |_| |\  ||_|  
 \/  \/ \___/\_| \_/(_)  
                         """)
        if (trousers == "off" and on_toilet == "yes" and toilet_lid == "up"):
          if SUCM == "on":
              print("CHEAT. you dont deserve fancy big letters.")
          else:
            type("congrats! you peed in the toilet!")
            
            type(""" _    _ _____ _   _ _ 
| |  | |_   _| \ | | |
| |  | | | | |  \| | |
| |/\| | | | | . ` | |
\  /\  /_| |_| |\  |_|
 \/  \/ \___/\_| \_(_)
                      
                      
                                        """)
    type ("*-<_%^#=~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")