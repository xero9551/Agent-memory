import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from app import greeting


class AppTest(unittest.TestCase):
    def test_greeting(self):
        self.assertIn('boundary test', greeting())


if __name__ == '__main__':
    unittest.main()
