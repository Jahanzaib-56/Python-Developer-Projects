
from random import choice
from time import sleep
import pyttsx3 as ptx

# Initialize the text-to-speech engine
engine = ptx.init()

def properties():
    """Configure the TTS engine's voice, volume, and speech rate."""

    # Set voice to the second available voice (index 1, typically female)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    # Set volume to maximum (range: 0.0 to 1.0)
    engine.setProperty('volume', 1)

    # Set speech rate to 150 words per minute
    engine.setProperty('rate', 150)

def speak(talk):
    """Apply TTS properties and speak the given text aloud."""
    properties()
    engine.say(talk)
    engine.runAndWait()

def choose():
    """
    Prompt the player for their choice and randomly generate the computer's choice.
    Both choices are stored as global variables in Title Case (e.g. 'Rock').
    """
    choices = ['Rock', 'Paper', 'Scissor']

    global My_choice
    # BUG FIX: .upper() made input "ROCK" etc., which never matched Title Case
    # comparisons like "Rock". Use .capitalize() instead to normalize to Title Case.
    My_choice = input("Enter your choice (Rock / Paper / Scissor): ").strip().capitalize()
    string = f"You chose {My_choice}"
    print(string)
    speak(string)

    global Computer_Choice
    Computer_Choice = choice(choices)
    string = f"Computer chose {Computer_Choice}"
    print(string)
    speak(string)

def gameplay():
    """Main game loop: plays Best of 3 rounds and announces the final result."""

    print("ROCK ..... PAPER ..... SCISSOR")
    print("BEST OF 3")

    you_won      = 0
    computer_won = 0
    games_tied   = 0

    for _ in range(3):

        choose()

        # BUG FIX: 'result' was never assigned on invalid input, causing
        # an UnboundLocalError in the score-tracking block below.
        # Default to None so we can safely skip score tracking for invalid input.
        result = None

        # Determine round outcome based on classic Rock-Paper-Scissor rules
        if My_choice == Computer_Choice:
            result = "TIED!"

        elif My_choice == "Rock" and Computer_Choice == "Scissor":
            result = "YOU WIN!"          # Rock crushes Scissor

        elif My_choice == "Rock" and Computer_Choice == "Paper":
            result = "COMPUTER WINS!"    # Paper covers Rock

        elif My_choice == "Paper" and Computer_Choice == "Scissor":
            result = "COMPUTER WINS!"    # Scissor cuts Paper

        elif My_choice == "Paper" and Computer_Choice == "Rock":
            result = "YOU WIN!"          # Paper covers Rock

        elif My_choice == "Scissor" and Computer_Choice == "Rock":
            result = "COMPUTER WINS!"    # Rock crushes Scissor

        elif My_choice == "Scissor" and Computer_Choice == "Paper":
            result = "YOU WIN!"          # Scissor cuts Paper

        else:
            # Invalid input: not one of Rock / Paper / Scissor
            print("Please enter a valid choice: Rock, Paper, or Scissor.")

        # Announce and tally the round result (skip if input was invalid)
        if result is not None:
            print(result)
            speak(result)

            if result == "COMPUTER WINS!":
                computer_won += 1
            elif result == "YOU WIN!":
                you_won += 1
            elif result == "TIED!":
                games_tied += 1

    # ── Final summary ────────────────────────────────────────────────────────
    speak("Evaluating final result!!")

    speak(f"You won {you_won} game{'s' if you_won != 1 else ''}.")
    speak(f"Computer won {computer_won} game{'s' if computer_won != 1 else ''}.")
    speak(f"{games_tied} game{'s' if games_tied != 1 else ''} ended in a tie.")

    # Announce the Best-of-3 winner
    if you_won > computer_won:
        string = "Congratulations! You won the Best of 3!"
    elif you_won < computer_won:
        string = "Computer wins the Best of 3. Better luck next time!"
    else:
        # Equal wins — this covers the you_won == computer_won case
        string = "The Best of 3 has been concluded as a Draw!"

    print(string)
    speak(string)


if __name__ == "__main__":
    try:
        gameplay()
    except Exception as e:
        print(f"An error occurred: {e}")
