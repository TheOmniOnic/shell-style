# Shell-Style

`Shell-Style` is a Python package designed for terminal formatting. It offers a variety of utilities to enhance the terminal experience, including color formatting, progress bars, and additional tools like `tables`, `rgb_to_ansi`, and `hex_to_ansi`. This package makes it easy to add colors, effects, and progress indicators to your terminal output.

## Features

- **Console Support**: Easily format terminal outputs with various effects such as bold, italic, underlined, and more.
- **Tables**: Tabulate information into beautiful tables.
- **Progress Bars**: Track the progress of long-running operations with customizable progress bars.
- **24-bit Color Support**: Use rich, vibrant colors. If your terminal does not support 24-bit colors, Shell-Style will warn you.

## Installation

To install `Shell-Style`, simply run:

```bash
python3 -m pip install shell-style
```

## Usage

### Console Formatting

You can format text using various styles. For example:

```python
from shell_style import Console, Theme, rgb_to_ansi

console = Console("MyConsole")
console.print("This is bold text", style="bold")
console.print("This is underlined text", style="underline")

theme1 = Theme(my_style=rgb_to_ansi(237, 234, 154))
console.theme = theme1

console.print("This is custom text", style="my_style")
```

### RGB to ANSI Conversion

Use `Shell-Style`'s functions to use RGB and HEX colors too:

```python
from shell_style import rgb_to_ansi

ansi_code = rgb_to_ansi(255, 0, 0)  # Red color
console.print(f"Your RGB to ANSI code: {ansi_code}")

from shell_style import hex_to_ansi

ansi_code = hex_to_ansi("#FF5733")  # Hex color code
console.print(f"Your Hex to ANSI code: {ansi_code}")
```

### Tables

Create tabulated output with dynamic content:

```python
from shell_style import Table

table = Table(2)
table.add_row("Name", "Age")
table.add_row("John Doe", 28)
table.add_row("Jane Smith", 34)

table.display()
```

### Progress Bars

Track the progress of long-running tasks with a customizable progress bar:

```python
from shell_style import ProgressBar

progress = ProgressBar(100, delay=0.5)
progress.run(style="bold")
```

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests. Here is the [link to the repository](https://github.com/TheOmniOnic/shell-style)

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Open a pull request

## License

This project is licensed under the GNU General Public License - see the [LICENSE](LICENSE) file for details.