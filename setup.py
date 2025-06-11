#!/usr/bin/env python3
"""
Setup script for 2048 Python Game
Simple setup and verification script
"""

import sys
import subprocess
import os

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 6):
        print("❌ Python 3.6 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True

def check_tkinter():
    """Check if Tkinter is available"""
    try:
        import tkinter
        print("✅ Tkinter is available")
        return True
    except ImportError:
        print("❌ Tkinter is not available")
        print("Please install tkinter (usually comes with Python)")
        return False

def test_game_logic():
    """Test the game logic"""
    try:
        from game_2048 import Game2048Logic
        game = Game2048Logic()
        print("✅ Game logic test passed")
        return True
    except Exception as e:
        print(f"❌ Game logic test failed: {e}")
        return False

def main():
    """Main setup function"""
    print("🎮 2048 Game Setup and Verification")
    print("=" * 40)
    
    all_good = True
    
    # Check Python version
    if not check_python_version():
        all_good = False
    
    # Check Tkinter
    if not check_tkinter():
        all_good = False
    
    # Test game logic
    if not test_game_logic():
        all_good = False
    
    print("=" * 40)
    
    if all_good:
        print("🎉 Setup complete! Everything looks good.")
        print("\nTo play the game, run:")
        print("  python3 game_2048.py")
        print("  or")
        print("  python3 play_2048.py")
    else:
        print("❌ Setup incomplete. Please fix the issues above.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
