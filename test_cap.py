import unittest
import cap

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multiplr_words(self):
        text = 'hello there'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Hello There')

if __name__ == "__main__":
    unittest.main()
