from unittest import TestCase, main
from io import StringIO
from unittest.mock import patch
from shell_style.models import ProgressBar

class TestProgressBar(TestCase):
    def setUp(self):
        self.progress_bar = ProgressBar(values=5, symbol="#", delay=0.1)

    @patch("time.sleep", return_value=None)
    @patch("sys.stdout", new_callable=StringIO)
    def test_run(self, mock_stdout, mock_sleep):
        self.progress_bar.run()
        output = mock_stdout.getvalue()
        self.assertEqual(output.count("#"), 5)
        self.assertTrue(output.endswith("\033[0m"))  # Ensure STOP sequence is applied

    def test_values_setter(self):
        self.progress_bar.values = 10
        self.assertEqual(self.progress_bar.values, 10)

    def test_symbol_setter(self):
        self.progress_bar.symbol = "*"
        self.assertEqual(self.progress_bar.symbol, "*")

if __name__ == "__main__":
    main()
