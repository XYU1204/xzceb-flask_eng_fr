import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
 def test_french_to_english(self):
     self.assertIsNone(french_to_english(), 'input is Null') # test null input.
     self.assertEqual(french_to_english("Bonjour"), 'Hello') # test hello.

 def test_english_to_french(self):
     self.assertIsNone(english_to_french(), 'input is Null') # test null input
     self.assertEqual(english_to_french('Hello'), 'Bonjour') # test hello.
 
if __name__=="__main__":
    unittest.main()