# Contributing to 2048 Python Game

Thank you for your interest in contributing to the 2048 Python Game! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Reporting Issues

If you find a bug or have a suggestion for improvement:

1. **Check existing issues** first to avoid duplicates
2. **Create a new issue** with a clear title and description
3. **Include steps to reproduce** the bug if applicable
4. **Add screenshots** if they help explain the issue

### Submitting Changes

1. **Fork the repository**
2. **Create a feature branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes** with clear, focused commits
4. **Test your changes** thoroughly
5. **Update documentation** if needed
6. **Submit a pull request**

## 🛠️ Development Setup

### Prerequisites

- Python 3.6 or higher
- Git
- Text editor or IDE

### Local Development

1. **Clone your fork**:
   ```bash
   git clone https://github.com/your-username/2048-python-game.git
   cd 2048-python-game
   ```

2. **Test the game**:
   ```bash
   python3 game_2048.py
   ```

3. **Run tests**:
   ```bash
   python3 test_2048_logic.py
   ```

## 📝 Coding Standards

### Python Style Guide

- Follow **PEP 8** style guidelines
- Use **meaningful variable names**
- Add **docstrings** for classes and functions
- Keep **functions focused** and single-purpose
- Use **type hints** where appropriate

### Code Structure

- **Separate concerns**: Keep game logic and UI separate
- **Comment complex logic**: Explain non-obvious code
- **Error handling**: Add appropriate try/catch blocks
- **Consistent formatting**: Use consistent indentation and spacing

### Example Code Style

```python
def calculate_score(merged_value: int) -> int:
    """
    Calculate score points for a merged tile.
    
    Args:
        merged_value: The value of the merged tile
        
    Returns:
        Points to add to the score
    """
    return merged_value
```

## 🎯 Contribution Ideas

### Beginner-Friendly

- **Fix typos** in documentation
- **Improve error messages**
- **Add more test cases**
- **Update color schemes**
- **Enhance UI styling**

### Intermediate

- **Add sound effects** using pygame
- **Implement animations** for tile movements
- **Add high score persistence**
- **Create different themes**
- **Add keyboard shortcuts**

### Advanced

- **Multiple grid sizes** (3x3, 5x5, 6x6)
- **Undo/Redo functionality**
- **AI solver implementation**
- **Network multiplayer**
- **Mobile touch controls**

## 🧪 Testing Guidelines

### Before Submitting

- **Test all game functions**: Ensure moves, scoring, and game states work
- **Test edge cases**: Full grid, no moves possible, winning condition
- **Test UI interactions**: Button clicks, key presses, window resizing
- **Cross-platform testing**: Test on different operating systems if possible

### Test Cases to Consider

- Game initialization
- All four movement directions
- Tile merging logic
- Score calculation
- Game over detection
- Win condition (reaching 2048)
- New game functionality

## 📋 Pull Request Guidelines

### PR Title Format

Use clear, descriptive titles:
- `feat: add sound effects for tile movements`
- `fix: resolve game over detection bug`
- `docs: update installation instructions`
- `refactor: improve code organization`

### PR Description Template

```markdown
## Description
Brief description of changes made.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring
- [ ] Performance improvement

## Testing
- [ ] Tested locally
- [ ] Added/updated tests
- [ ] All existing tests pass

## Screenshots (if applicable)
Add screenshots for UI changes.

## Additional Notes
Any additional information or context.
```

## 🎨 Design Guidelines

### UI/UX Principles

- **Keep it simple**: Clean, uncluttered interface
- **Consistent styling**: Use consistent colors and fonts
- **Responsive design**: Handle different screen sizes
- **Accessibility**: Consider color contrast and keyboard navigation

### Color Scheme

The current color scheme follows the original 2048 design:
- Background: `#faf8ef`
- Grid: `#bbada0`
- Empty tiles: `#cdc1b4`
- Numbered tiles: Various colors based on value

## 🚀 Release Process

### Version Numbering

We use semantic versioning (SemVer):
- **Major** (1.0.0): Breaking changes
- **Minor** (0.1.0): New features, backward compatible
- **Patch** (0.0.1): Bug fixes, backward compatible

### Release Checklist

- [ ] All tests pass
- [ ] Documentation updated
- [ ] Version number bumped
- [ ] Changelog updated
- [ ] Tagged release created

## 📞 Getting Help

### Communication Channels

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For questions and general discussion
- **Pull Request Comments**: For code-specific discussions

### Code Review Process

1. **Automated checks**: Ensure code passes any automated tests
2. **Peer review**: At least one maintainer will review your code
3. **Feedback incorporation**: Address any requested changes
4. **Final approval**: Maintainer approves and merges

## 🏆 Recognition

Contributors will be recognized in:
- **README.md**: Contributors section
- **Release notes**: Major contributions highlighted
- **GitHub**: Contributor graphs and statistics

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to the 2048 Python Game! 🎮

Your contributions help make this project better for everyone. Whether you're fixing a small bug or adding a major feature, every contribution is valued and appreciated.

Happy coding! 🚀
