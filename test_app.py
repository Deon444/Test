import unittest

import app


class TestApp(unittest.TestCase):
    def test_greet(self) -> None:
        self.assertEqual(app.greet("Ada"), "Hello, Ada!")


if __name__ == "__main__":
    unittest.main()
