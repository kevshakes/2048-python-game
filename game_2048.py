#!/usr/bin/env python3
"""
2048 Game Implementation using Tkinter

A complete implementation of the popular 2048 puzzle game with:
- 4x4 grid gameplay
- Arrow key controls
- Score tracking
- Game over detection
- New game functionality
- Color-coded tiles

Author: Amazon Q
"""

import tkinter as tk
from tkinter import messagebox
import random
import copy


class Game2048Logic:
    """
    Handles all game logic for 2048 including:
    - Grid management
    - Move calculations
    - Score tracking
    - Game state validation
    """
    
    def __init__(self):
        self.grid_size = 4
        self.reset_game()
    
    def reset_game(self):
        """Initialize a new game"""
        self.grid = [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.score = 0
        self.game_over = False
        self.won = False
        
        # Add two initial tiles
        self.add_random_tile()
        self.add_random_tile()
    
    def add_random_tile(self):
        """Add a random tile (2 or 4) to an empty cell"""
        empty_cells = []
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.grid[i][j] == 0:
                    empty_cells.append((i, j))
        
        if empty_cells:
            row, col = random.choice(empty_cells)
            # 90% chance for 2, 10% chance for 4
            self.grid[row][col] = 2 if random.random() < 0.9 else 4
    
    def move_left(self):
        """Move all tiles left and combine matching adjacent tiles"""
        moved = False
        new_grid = copy.deepcopy(self.grid)
        
        for i in range(self.grid_size):
            # Remove zeros and shift left
            row = [cell for cell in new_grid[i] if cell != 0]
            
            # Combine adjacent matching tiles
            j = 0
            while j < len(row) - 1:
                if row[j] == row[j + 1]:
                    row[j] *= 2
                    self.score += row[j]
                    if row[j] == 2048 and not self.won:
                        self.won = True
                    row.pop(j + 1)
                j += 1
            
            # Pad with zeros
            row.extend([0] * (self.grid_size - len(row)))
            new_grid[i] = row
        
        # Check if grid changed
        if new_grid != self.grid:
            moved = True
            self.grid = new_grid
        
        return moved
    
    def move_right(self):
        """Move all tiles right"""
        # Reverse, move left, reverse back
        self.grid = [row[::-1] for row in self.grid]
        moved = self.move_left()
        self.grid = [row[::-1] for row in self.grid]
        return moved
    
    def move_up(self):
        """Move all tiles up"""
        # Transpose, move left, transpose back
        self.grid = list(map(list, zip(*self.grid)))
        moved = self.move_left()
        self.grid = list(map(list, zip(*self.grid)))
        return moved
    
    def move_down(self):
        """Move all tiles down"""
        # Transpose, move right, transpose back
        self.grid = list(map(list, zip(*self.grid)))
        moved = self.move_right()
        self.grid = list(map(list, zip(*self.grid)))
        return moved
    
    def can_move(self):
        """Check if any moves are possible"""
        # Check for empty cells
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.grid[i][j] == 0:
                    return True
        
        # Check for possible merges
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                current = self.grid[i][j]
                # Check right neighbor
                if j < self.grid_size - 1 and self.grid[i][j + 1] == current:
                    return True
                # Check bottom neighbor
                if i < self.grid_size - 1 and self.grid[i + 1][j] == current:
                    return True
        
        return False
    
    def make_move(self, direction):
        """Make a move in the specified direction"""
        if self.game_over:
            return False
        
        moved = False
        if direction == 'left':
            moved = self.move_left()
        elif direction == 'right':
            moved = self.move_right()
        elif direction == 'up':
            moved = self.move_up()
        elif direction == 'down':
            moved = self.move_down()
        
        if moved:
            self.add_random_tile()
            if not self.can_move():
                self.game_over = True
        
        return moved


class Game2048GUI:
    """
    Handles the graphical user interface for the 2048 game
    """
    
    # Color scheme for different tile values
    TILE_COLORS = {
        0: ("#cdc1b4", "#776e65"),      # Empty
        2: ("#eee4da", "#776e65"),      # 2
        4: ("#ede0c8", "#776e65"),      # 4
        8: ("#f2b179", "#f9f6f2"),      # 8
        16: ("#f59563", "#f9f6f2"),     # 16
        32: ("#f67c5f", "#f9f6f2"),     # 32
        64: ("#f65e3b", "#f9f6f2"),     # 64
        128: ("#edcf72", "#f9f6f2"),    # 128
        256: ("#edcc61", "#f9f6f2"),    # 256
        512: ("#edc850", "#f9f6f2"),    # 512
        1024: ("#edc53f", "#f9f6f2"),   # 1024
        2048: ("#edc22e", "#f9f6f2"),   # 2048
    }
    
    def __init__(self):
        self.game = Game2048Logic()
        self.setup_gui()
        self.update_display()
    
    def setup_gui(self):
        """Initialize the GUI components"""
        self.root = tk.Tk()
        self.root.title("2048 Game")
        self.root.geometry("500x600")
        self.root.configure(bg="#faf8ef")
        self.root.resizable(False, False)
        
        # Bind arrow keys
        self.root.bind('<Key>', self.key_pressed)
        self.root.focus_set()
        
        # Title
        title_label = tk.Label(
            self.root,
            text="2048",
            font=("Arial", 40, "bold"),
            bg="#faf8ef",
            fg="#776e65"
        )
        title_label.pack(pady=20)
        
        # Score display
        self.score_label = tk.Label(
            self.root,
            text="Score: 0",
            font=("Arial", 18, "bold"),
            bg="#faf8ef",
            fg="#776e65"
        )
        self.score_label.pack(pady=10)
        
        # Game grid frame
        self.grid_frame = tk.Frame(self.root, bg="#bbada0", padx=10, pady=10)
        self.grid_frame.pack(pady=20)
        
        # Create grid of labels for tiles
        self.tile_labels = []
        for i in range(4):
            row = []
            for j in range(4):
                label = tk.Label(
                    self.grid_frame,
                    text="",
                    font=("Arial", 24, "bold"),
                    width=4,
                    height=2,
                    relief="flat",
                    bd=5
                )
                label.grid(row=i, column=j, padx=5, pady=5)
                row.append(label)
            self.tile_labels.append(row)
        
        # Control buttons frame
        button_frame = tk.Frame(self.root, bg="#faf8ef")
        button_frame.pack(pady=20)
        
        # New game button
        new_game_btn = tk.Button(
            button_frame,
            text="New Game",
            font=("Arial", 14, "bold"),
            bg="#8f7a66",
            fg="#f9f6f2",
            padx=20,
            pady=10,
            command=self.new_game,
            relief="flat"
        )
        new_game_btn.pack(side=tk.LEFT, padx=10)
        
        # Instructions
        instructions = tk.Label(
            self.root,
            text="Use arrow keys to move tiles. Combine tiles with the same number to reach 2048!",
            font=("Arial", 10),
            bg="#faf8ef",
            fg="#776e65",
            wraplength=400
        )
        instructions.pack(pady=10)
    
    def update_display(self):
        """Update the visual display of the game grid and score"""
        # Update score
        self.score_label.config(text=f"Score: {self.game.score}")
        
        # Update grid
        for i in range(4):
            for j in range(4):
                value = self.game.grid[i][j]
                label = self.tile_labels[i][j]
                
                if value == 0:
                    label.config(text="", bg=self.TILE_COLORS[0][0])
                else:
                    label.config(
                        text=str(value),
                        bg=self.TILE_COLORS.get(value, ("#3c3a32", "#f9f6f2"))[0],
                        fg=self.TILE_COLORS.get(value, ("#3c3a32", "#f9f6f2"))[1]
                    )
        
        # Check game state
        if self.game.won and not hasattr(self, 'win_shown'):
            self.win_shown = True
            result = messagebox.askyesno(
                "Congratulations!",
                "You reached 2048! Do you want to continue playing?"
            )
            if not result:
                self.new_game()
        
        if self.game.game_over:
            messagebox.showinfo(
                "Game Over",
                f"No more moves possible!\nFinal Score: {self.game.score}"
            )
    
    def key_pressed(self, event):
        """Handle arrow key presses"""
        key_map = {
            'Up': 'up',
            'Down': 'down',
            'Left': 'left',
            'Right': 'right'
        }
        
        if event.keysym in key_map:
            moved = self.game.make_move(key_map[event.keysym])
            if moved:
                self.update_display()
    
    def new_game(self):
        """Start a new game"""
        self.game.reset_game()
        if hasattr(self, 'win_shown'):
            delattr(self, 'win_shown')
        self.update_display()
    
    def run(self):
        """Start the game loop"""
        self.root.mainloop()


def main():
    """Main function to run the 2048 game"""
    print("Starting 2048 Game...")
    print("Use arrow keys to move tiles.")
    print("Combine tiles with the same number to reach 2048!")
    print("Press 'New Game' button to restart at any time.")
    
    game = Game2048GUI()
    game.run()


if __name__ == "__main__":
    main()
