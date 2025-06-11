# 2048 Game - Python Implementation

A complete implementation of the popular 2048 puzzle game built with Python and Tkinter.

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-cross--platform-lightgrey.svg)

## 🎮 Features

- **4x4 Grid Gameplay**: Classic 2048 game mechanics
- **Arrow Key Controls**: Use arrow keys to move tiles in all directions
- **Automatic Tile Spawning**: New tiles (2 or 4) appear after each move
- **Score Tracking**: Real-time score display
- **Game Over Detection**: Automatic detection when no moves are possible
- **Win Condition**: Celebration when reaching the 2048 tile
- **New Game Button**: Reset and start over at any time
- **Color-Coded Tiles**: Visual distinction for different tile values
- **Responsive UI**: Clean, modern interface

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- Tkinter (included with Python by default)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/kevshakes/2048-python-game.git
   cd 2048-python-game
   ```

2. **Run the game**:
   ```bash
   python3 game_2048.py
   ```
   
   Or use the launcher with instructions:
   ```bash
   python3 play_2048.py
   ```

### Alternative: Direct Download

```bash
# Make executable and run
chmod +x game_2048.py
./game_2048.py
```

## 🎯 How to Play

1. **Objective**: Combine tiles with the same number to reach the 2048 tile
2. **Controls**: Use arrow keys (↑ ↓ ← →) to move tiles
3. **Mechanics**: 
   - All tiles slide in the chosen direction
   - When two tiles with the same number touch, they merge into one
   - After each move, a new tile (2 or 4) appears randomly
4. **Scoring**: Points are awarded equal to the value of merged tiles
5. **Winning**: Reach the 2048 tile to win (but you can continue playing)
6. **Game Over**: When no more moves are possible

## 🏗️ Architecture

The code is structured with clear separation of concerns:

### `Game2048Logic` Class
- Handles all game mechanics
- Grid management and tile movements
- Score calculation
- Game state validation
- Move algorithms for all four directions

### `Game2048GUI` Class  
- Manages the user interface
- Handles user input (arrow keys)
- Updates visual display
- Color scheme and styling

## 📁 Project Structure

```
2048-python-game/
├── game_2048.py          # Main game implementation
├── play_2048.py          # Game launcher with instructions
├── test_2048_logic.py    # Logic testing script
├── README.md             # This file
├── LICENSE               # MIT License
├── .gitignore           # Git ignore rules
└── requirements.txt      # Python dependencies (minimal)
```

## 🎨 Customization

You can easily modify the game by changing:

- **Grid Size**: Modify `grid_size` in `Game2048Logic.__init__()`
- **Colors**: Update the `TILE_COLORS` dictionary in `Game2048GUI`
- **Tile Spawn Probability**: Adjust the ratio in `add_random_tile()`
- **Win Condition**: Change the target value from 2048

## 🧪 Testing

Run the logic tests to verify game mechanics:

```bash
python3 test_2048_logic.py
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Ideas for Contributions

- Add animations for tile movements
- Implement sound effects
- Add high score persistence
- Create different grid sizes (3x3, 5x5)
- Add undo functionality
- Mobile/touch controls

## 🐛 Troubleshooting

**Game won't start**:
- Ensure Python 3.6+ is installed
- Check that Tkinter is available (usually included with Python)

**Arrow keys not working**:
- Click on the game window to ensure it has focus
- Try clicking on the grid area

**Performance issues**:
- The game should run smoothly on any modern system
- If issues persist, try closing other applications

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by the original 2048 game by Gabriele Cirulli
- Built with Python's Tkinter for cross-platform compatibility
- Thanks to the Python community for excellent documentation

## 📊 Technical Details

- **Language**: Python 3.6+
- **GUI Framework**: Tkinter (built-in)
- **Architecture**: Object-oriented with separated logic and UI
- **Grid Representation**: 2D list (4x4)
- **Movement Algorithm**: Slide and merge in single pass
- **Random Generation**: Python's `random` module

---

🎮 **Ready to play? Use the arrow keys to move tiles and try to reach 2048!** 🎮

⭐ **If you enjoy this game, please give it a star!** ⭐
