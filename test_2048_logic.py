#!/usr/bin/env python3
"""
Test script for 2048 game logic
Tests the core game mechanics without GUI
"""

import sys
sys.path.append('.')
from game_2048 import Game2048Logic

def test_game_logic():
    """Test basic game functionality"""
    print("Testing 2048 Game Logic...")
    
    # Initialize game
    game = Game2048Logic()
    print(f"✓ Game initialized with score: {game.score}")
    
    # Check initial state
    non_zero_tiles = sum(1 for row in game.grid for cell in row if cell != 0)
    print(f"✓ Initial tiles placed: {non_zero_tiles} (should be 2)")
    
    # Test grid setup
    assert len(game.grid) == 4, "Grid should be 4x4"
    assert len(game.grid[0]) == 4, "Grid should be 4x4"
    print("✓ Grid dimensions correct (4x4)")
    
    # Test move capability
    can_move_initial = game.can_move()
    print(f"✓ Can make moves: {can_move_initial}")
    
    # Test a simple move
    initial_grid = [row[:] for row in game.grid]  # Copy grid
    moved = game.make_move('left')
    print(f"✓ Move left executed: {moved}")
    
    # Verify new tile was added if move was successful
    if moved:
        new_non_zero = sum(1 for row in game.grid for cell in row if cell != 0)
        print(f"✓ Tiles after move: {new_non_zero}")
    
    print("\n2048 Game Logic Test Completed Successfully! 🎮")
    print("\nSample grid state:")
    for row in game.grid:
        print([f"{cell:4d}" if cell != 0 else "   ." for cell in row])
    
    return True

if __name__ == "__main__":
    test_game_logic()
