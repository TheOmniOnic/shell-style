from unittest import (TestCase, main)
from shell_style.models import Table
from shell_style import strip_ansi

class TestTable(TestCase):
    def setUp(self):
        self.table = Table(columns=3)
        self.table.add_row("Alice", "Bob", "Charlie")
        self.table.add_row("David", "Eve", "Frank")

    def test_add_column(self):
        self.table.add_column("New")
        self.assertEqual(strip_ansi(self.table.table[0][-1]), "New")

    def test_get_column(self):
        self.assertEqual(strip_ansi(self.table.get_column(0, 1)), "Bob")

    def test_get_row(self):
        self.assertEqual(
            [strip_ansi(cell) for cell in self.table.get_row(0)],
            ["Alice", "Bob", "Charlie"]
        )

    def test_set_column(self):
        self.table.set_column("David", 0, 1)
        self.assertEqual(strip_ansi(self.table.get_column(0, 1)), "David")

    def test_symbol_separated_values(self):
        expected = "Alice,Bob,Charlie,\nDavid,Eve,Frank,\n"
        self.assertEqual(strip_ansi(self.table.symbol_separated_values(",")), expected)

if __name__ == "__main__":
    main()
