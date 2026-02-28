# My project - Arcade Collection

A collection of **five classic games** built in Python using *Pygame*, featuring a launcher menu to easily play:  

- **Connect 4**
- **Minesweeper** 
- **Snake**
- **Pong**
- **Space Invaders**

This project was created **13 days into learning Pygame**, showcasing rapid learning, problem-solving, and creativity.

---

## 🖥 Screenshots

*(Replace these paths with actual images from your `Docs/` folder or in-game screenshots)*

| Launcher | Connect 4 | Minesweeper |
|----------|------------|------------|
| ![Launcher](Docs/launcher.png) | ![Connect 4](Docs/connect4.png) | ![Minesweeper](Docs/minesweeper.png) |

| Snake | Pong | Space Invaders |
|-------|------|----------------|
| ![Snake](Docs/snake.png) | ![Pong](Docs/pong.png) | ![Space Invaders](Docs/spaceinvaders.png) |

---

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Arcade.git

Install dependencies:

pip install -r requirements.txt

Run the launcher:

python Arcade/launcher.py

Click on any game icon to start playing!

🎮 Controls

Connect 4 – Click the column to place your piece
Minesweeper – Left click to reveal, right click to flag
Snake – Arrow keys to move
Pong – Player 1: W/S, Player 2: Up/Down
Space Invaders – Arrow keys to move, spacebar to shoot

✨ Features

Fully playable multi-game arcade with a graphical launcher

Custom graphics and animations for each game

Sound effects and music in Space Invaders

Clean folder organization for images, sounds, and scripts

Handles user input, collision detection, and game logic efficiently

🛠 Technical Details

Built in Python 3.x

Uses Pygame for graphics, input, and sounds

Modular code with separate files for each game

Launcher allows easy navigation between games

🌟 Future Improvements

Save high scores for Snake, Pong, and Space Invaders

Add levels or difficulty options

Include additional mini-games

Polish animations and add background music

💡 Learning Outcome

Rapidly improved Python skills in game logic, graphics, and event handling

Learned to structure a multi-file project professionally

Gained experience in animations, sound integration, and GUI design

📂 Repository Structure
Arcade/
├── Connect4/
│   ├── connect_4_pygame.py
│   └── Images/
├── Minesweeper/
│   ├── minesweeper_pygame.py
│   └── Images/
├── Snake/
│   ├── Snake_Pygame.py
│   └── Images/
├── Pong/
│   └── Pong_pygame.py
├── Space_Invaders/
│   ├── Space_invaders_Pygame.py
│   └── Images/
├── launcher.py
└── requirements.txt