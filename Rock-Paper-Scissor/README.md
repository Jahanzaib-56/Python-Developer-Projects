# ✊✋✌️ Rock Paper Scissors — Voice-Enabled CLI Game

A Python terminal game of **Rock, Paper, Scissors** with built-in **text-to-speech** narration. Play a Best-of-3 match against the computer while the game announces every move and result out loud.

---

## 🎮 Features

- **Best of 3** match format with win/loss/draw tracking
- **Text-to-speech narration** via `pyttsx3` — every move and result is spoken aloud
- **Randomized computer opponent** using Python's `random.choice`
- Clean input normalization — type in any case (`rock`, `ROCK`, `Rock`)
- Graceful error handling for invalid inputs and unexpected exceptions

---

## 📋 Requirements

- Python **3.7+**
- [`pyttsx3`](https://pypi.org/project/pyttsx3/)

> `pyttsx3` works offline and supports Windows (SAPI5), macOS (NSSpeechSynthesizer), and Linux (espeak).

---

## ⚙️ Installation

**1. Clone the repository**
```bash
git clone https://github.com/your-username/rock-paper-scissors.git
cd rock-paper-scissors
```

**2. (Optional) Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

**3. Install dependencies**
```bash
pip install pyttsx3
```

---

## 🚀 Usage

```bash
python rock_paper_scissors.py
```

You'll be prompted three times to enter your choice:

```
ROCK ..... PAPER ..... SCISSOR
BEST OF 3
Enter your choice (Rock / Paper / Scissor): rock
You chose Rock
Computer chose Scissor
YOU WIN!
...
```

At the end of all three rounds, the game announces the final score and overall winner.

---

## 🗂️ Project Structure

```
rock-paper-scissors/
├── rock_paper_scissors.py   # Main game script
└── README.md
```

---

## 🔧 How It Works

| Function | Responsibility |
|---|---|
| `properties()` | Configures TTS voice, volume, and speech rate |
| `speak(text)` | Applies properties and speaks the given string |
| `choose()` | Gets player input and generates computer's random choice |
| `gameplay()` | Runs the 3-round loop, tracks scores, and announces the winner |

---

## 🐛 Known Issues / Limitations

- On some Linux systems, `pyttsx3` requires `espeak` to be installed separately:
  ```bash
  sudo apt install espeak
  ```
- The voice index (`voices[1]`) is set to the second available system voice. If your system only has one voice, change the index to `voices[0]`.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for improvements such as:
- A best-of-5 mode
- A GUI version using `tkinter` or `pygame`
- Score persistence across sessions

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
