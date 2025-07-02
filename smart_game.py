import random
import time
import pyttsx3 as ptx # Our Text-to-speech Module

# Initializing Engine to speak
engine = ptx.init()

# Setting Engines voice to Microsoft's Female Assistant
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Adjusting Engine's speech rate (a bit slower)
engine.getProperty("rate")  
engine.setProperty('rate', 130)

# Welcome message
print("Hello and Welcome to Rock Paper Scissor Game.......")
engine.say("Hello and Welcome to Rock Paper Scissor Game.......")
engine.runAndWait()

# A lsi of choices for computer to choose
choices = ["Rock", "Paper", "Scissor"]

# Initial game state
You_Won = 0
Computer_Won = 0
Games_tied = 0

# Using for loop for a 3-rounds game
for _ in range(3):

    print("-------------------------------------------------------------------")

    print(f"Round {int(_) + 1}")
    engine.say(f"Round {int(_) + 1}")
    engine.runAndWait()

    # Logic for User's Choice
    engine.say("Please Enter your choice....")
    engine.runAndWait()
    user_choice = input("Please Enter your choice (Rock, Paper, Scissor): ").title()
    if user_choice not in choices:
        print("Invalid choice! Please choose Rock, Paper, or Scissor.")
        engine.say("Invalid choice! Please choose Rock, Paper, or Scissor.")
        engine.runAndWait()
        continue

    print(f"Your choice is: {user_choice}")
    engine.say(f"Your choice is: {user_choice}")
    engine.runAndWait()

    time.sleep(1)

    # Logic for Computer's Choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    engine.say(f"Computer chose: {computer_choice}")
    engine.runAndWait()

    time.sleep(1)

    # Using conditionals to get a result of the game
    if user_choice == computer_choice:
        result = "Game tied"
        print(result)
        engine.say(result)
        engine.runAndWait()
    elif user_choice == "Rock" and computer_choice == "Paper":
        result = "Computer Won"
        print(result)
        engine.say(result)
        engine.runAndWait()
    elif user_choice == "Rock" and computer_choice == "Scissor":
        result = "You Won"
        print(result)
        engine.say(result)
        engine.runAndWait()
    elif user_choice == "Paper" and computer_choice == "Rock":
        result = "You Won"
        print(result)
        engine.say(result)
        engine.runAndWait()
    elif user_choice == "Paper" and computer_choice == "Scissor":
        result = "Computer Won"
        print(result)
        engine.say(result)
        engine.runAndWait()
    elif user_choice == "Scissor" and computer_choice == "Paper":
        result = "You Won"
        print(result)
        engine.say(result)
        engine.runAndWait()
    elif user_choice == "Scissor" and computer_choice == "Rock":
        result = "Computer Won"
        print(result)
        engine.say(result)
        engine.runAndWait()

    print("-------------------------------------------------------------------")

    time.sleep(1)

    # Final Game State
    if result == "Computer Won":
        Computer_Won += 1
    elif result == "You Won":
        You_Won += 1
    elif result == "Game tied":
        Games_tied += 1

time.sleep(1)

# Displaying final result
print(f"You have won {You_Won} games.")
engine.say(f"You have won {You_Won} games.")
engine.runAndWait()

time.sleep(1)

print(f"Computer has won {Computer_Won} games.")
engine.say(f"Computer has won {Computer_Won} games.")
engine.runAndWait()

time.sleep(1)

print(f"{Games_tied} games have no result.")
engine.say(f"{Games_tied} games have no result.")
engine.runAndWait()

print("-------------------------------------------------------------------")

time.sleep(1)

print("Calculating the final result........")
engine.say("Calculating the final result........")
engine.runAndWait()

print("-------------------------------------------------------------------")

time.sleep(1)

if (Computer_Won > You_Won):
    print("Looks like Computer has won the series.")
    engine.say("Looks like Computer has won the series.")
    engine.runAndWait()
elif (Computer_Won < You_Won):
    print("Congrats! You have outperformed the computer in best of 3.")
    engine.say("Congrats! You have outperformed the computer in best of 3.")
    engine.runAndWait()
elif (Computer_Won == You_Won):
    print("Series has been concluded as a TIE.")
    engine.say("Series has been concluded as a TIE.")
    engine.runAndWait()

print("-------------------------------------------------------------------")

time.sleep(1)

final_message = "Thanks for playing. I hope you really enjoyed it........"
print(final_message)
engine.say(final_message)
engine.runAndWait()

print("-------------------------------------------------------------------")
print("\n")