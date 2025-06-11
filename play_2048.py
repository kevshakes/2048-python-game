#!/usr/bin/env python3
"""
2048 Game Launcher
Simple launcher script with instructions
"""

import sys
import os

def main():
    print("=" * 50)
    print("🎮 Welcome to 2048! 🎮")
    print("=" * 50)
    print()
    print("INSTRUCTIONS:")
    print("• Use arrow keys (↑ ↓ ← →) to move tiles")
    print("• Combine tiles with same numbers to reach 2048")
    print("• Click 'New Game' to restart anytime")
    print("• Press Ctrl+C in terminal to quit")
    print()
    print("CONTROLS:")
    print("• ↑ Arrow Key: Move tiles up")
    print("• ↓ Arrow Key: Move tiles down") 
    print("• ← Arrow Key: Move tiles left")
    print("• → Arrow Key: Move tiles right")
    print()
    print("Starting game in 3 seconds...")
    print("=" * 50)
    
    # Import and start the game
    try:
        from game_2048 import main as start_game
        start_game()
    except ImportError:
        print("Error: Could not find game_2048.py")
        print("Make sure game_2048.py is in the same directory")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nThanks for playing 2048! 👋")
        sys.exit(0)

if __name__ == "__main__":
    main()
