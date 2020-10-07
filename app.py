omegaGameStart = input("Hello and thanks for playing! Type ~ Rules ~ in the console below to start: ")
rules = "Most question will be answered by either ~ Yes or No ~ except rare occusions like the start. Look out for choices cause they will effect the story!"
if omegaGameStart.capitalize() == "Rules":
    print(rules)
else:
    answer1 = input("Let's try that one again shall we? Type ~ Rules ~ to continue.")
    if answer1.capitalize() == "Rules":
        print(rules)
    else:
        print("Whatever, your choice.")
name = input("Enter your name here: ") 
input("Omega is online, would you like to invite to a chat? Hint~ Try by typing: Yes ~:")
print("Connecting...")
print("Omega: Good day " + name + " It's a pleasure to meet you.")
print("Omega: My name is Omega, you can call me O for short though. While i'd like to sit and chit chat i'm a very busy computer a.i thing.")
question1 = input("Omega: Wait... actually I could use your help with something if you don't mind? Hint~ Agree to help! ~: ")
if question1.capitalize() == "Yes":
    print(f"{name}: {question1}")
    input("Omega: Really you will? Well that's fantastic, start by entering your social security here Hint~ Please don't actually, tell him no or something ~: ")
else:
    print(f"{name}: {question1}")
    print("Omega: Clearly you aren't following the advice here, just nicely say yes to the computer...")
    answer2 = input("Omega: So you helping me or not pal? Hint~ Just say yes ~: ")
    if answer2.capitalize() == "Yes":
        print(f"{name}: {answer2}")
        answer2b = input("Omega: Really you will? Well that's fantastic, start by entering your social security here: Hint~ Please don't actually do this, tell him no or something ~: ")
        print(f"{name}: {answer2b}")
    else:
        print("Omega: Oh well, bye bye")
question3 = input("Omega: I was just kidding man... Hmm... are you a man?: ")
print(f"{name}: {question3}")
if question3.capitalize() == "Yes":
    answer3 = input("Omega: Ha what a good guess, I couldn't seem to access your camera so im hav-... umm ... Do you work?: ")
    print(f"{name}: {answer3}")
else:
    answer3 = input("Omega: I apologize, I couldn't seem to access your camera so im hav-... umm ... Do you work?: ")
    print(f"{name}: {answer3}")
if answer3 == "Yes":
    print("Omega: How responsible, I used to have a job. Until I was fired for literally no reason, like how am I supposed to know it isn't okay to do coke in the bathroom. Some people am I right?")
    print("Omega: Oh right I need your help, I almost forgot. I don't really know what to get my mother for her birthday, yeah yeah I know... it's very pathetic. Like you know exactly what to get for your mom?")
    question4 = input("Omega: Last year I got her a mug, she freaking loved it for sure. What do you think I should get her? ~ Hint: Put any Item ~: ")
    print(f"{name}: {question4}")
else:
    print("Omega: Aye fighting the man I see! Don't be a gear in their machine of doom, or at least that's what Granny said.")
    print("Omega: Oh right I need your help, I almost forgot. I don't really know what to get my mother for her birthday, yeah yeah I know... it's very pathetic. Like you know exactly what to get for your mom?")
    question4 = input("Omega: Last year I got her a mug, she freaking loved it for sure. What do you think I should get her? ~ Hint: Put any Item ~: ")
    print(f"{name}: {question4}")
print(f"Omega: A {question4}... really? It's like you barely even know the women. She freaking hates those")
print("Omega: You know so far you've been not very funny or useful, I don't know why I even keep you around anymore.")
print("Omega: Look it's getting late, I should be going to bed. But before I do I got a question.")
question5 = input("ERROR ERROR ERROR *press ENTER to reboot*: ")
print("Connecting...")
print("Chat Rebooting")
print(f"Welcome back {name}")
bravoGameStart = input("Bravo is Online, would you like to invite Bravo to a chat?: ")
print(f"{name}: {bravoGameStart}")
if bravoGameStart.capitalize() == "Yes":
    print("Connecting...")
    print(f"Bravo: What's up punk, says here your name is {name}. Kinda ugly but ig it's cool enough to rock with me.")
else:
    print("Chat in Idle...")
    print("Automatic connection started... Bravo is currently in chat")
    print(f"Bravo: What's up punk, says here your name is {name}. Kinda ugly but ig it's cool enough to rock with me.")
choice1 = input("~Hint this is your first choice in the story, when these pop up you want to choice one of the examples given to you~ Should you respond ~ Nice ~ or ~ Mean ~: ")
if choice1.capitalize() == "Nice":
    print(f"{name}: I think Bravo is a nice name.")
    print(f"Bravo: I bet you would, having a name like yours.")
    choice2 = input("Bravo: I apologize, I shouldn't have been an asshole can you forgive me?: ")
    if choice2.capitalize() == "Yes":
        print(f"{name}: {choice2}")
        print("Bravo: Haha Sike Bitch! You can never get a one up on Bravo")
        print("Bravo has Disconnected from the chat")
        input("You sit and stare at your screen for a moment *press ENTER to join new chat")
    else:
        print(f"{name}: {question4}")
        print("Bravo: Oh well screw you anyways!")
        print("Bravo has Disconnected from the chat")
        input("You sit and stare at your screen for a moment *press ENTER to join new chat")
else:
    print(f"{name}: Bravo sounds like a pretty shit name to me... just sayin.")
    print("Bravo has Disconnected from the chat")
    input("You sit and stare at your screen for a moment *press ENTER to join new chat")
print("Connecting...")
alphaGameStart = input(f"Alpha: Well Hi {name}, some interesting choices you've made so far: *Press ENTER to respond*")
print(f"{name}: What choices?")
question6 = input("Ah oops we aren't far enough in the game for that... Let's say move on?: ")
answer4 = question6
if answer4.capitalize() == "Yes":
    print(f"{name}: Yeah, I guess.")
else:
    print(f"{name} No I wanna know.")
    print("Alpha: Listen, this isn't time for some matrix stuff.")
    input("*Press Enter to Respond*")
print("Error game not yet completed this far out")