from unittest import TestCase, main
from io import StringIO
from unittest.mock import patch
from shell_style.models import Console, Theme

class TestConsole(TestCase):
    def setUp(self):
        self.console = Console("Test Console")

    @patch("sys.stdout", new_callable=StringIO)
    def test_print_title(self, mock_stdout):
        self.console.print_title()
        output = mock_stdout.getvalue().strip()
        self.assertIn("Test Console", output)

    @patch("builtins.input", return_value="Test input")
    def test_prompt(self, mock_input):
        result = self.console.prompt("Enter something: ")
        self.assertEqual(result, "Test input")

    @patch("sys.stdout", new_callable=StringIO)
    def test_write_and_log(self, mock_stdout):
        self.console.write("Write message")
        self.console.log("Log message")
        output = mock_stdout.getvalue()
        self.assertIn("Write message", output)
        self.assertIn("Log message", output)

    def test_theme_setter(self):
        new_theme = Theme(info="cyan", warning="yellow")
        self.console.theme = new_theme
        self.assertEqual(self.console.theme, new_theme)

if __name__ == "__main__":
    main()
