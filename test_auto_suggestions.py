import unittest
from auto_suggestions import AutoSuggetions

class TestAutoSuggestions(unittest.TestCase):

    def test_no_asterisk(self):
        # Test when input2 has no asterisk
        input1 = ['take', 'make', 'check', 'ack', 'rake']
        input2 = 'ke'
        expected = ['take', 'make', 'rake']
        self.assertEqual(AutoSuggetions.get_auto_suggestions(input1, input2), expected)

    def test_ends_with_c(self):
        # Test when input2 is "*k" (words ending with 'k')
        input1 = ['take', 'make', 'check', 'ack', 'rake']
        input2 = '*k'
        expected = ['check', 'ack']
        self.assertEqual(AutoSuggetions.get_auto_suggestions(input1, input2), expected)

    def test_starts_with_c(self):
        # Test when input2 is "c*" (words starting with 'c')
        input1 = ['take', 'make', 'check', 'ack', 'rake']
        input2 = 'c*'
        expected = ['check']
        self.assertEqual(AutoSuggetions.get_auto_suggestions(input1, input2), expected)

    def test_full_match(self):
        # Test when input2 is "check" (full match required)
        input1 = ['take', 'make', 'check', 'ackec', 'rake']
        input2 = 'check'
        expected = ['check']
        self.assertEqual(AutoSuggetions.get_auto_suggestions(input1, input2), expected)

    def test_empty_inputs(self):
        # Test when input1 and input2 are empty
        input1 = []
        input2 = ''
        expected = []
        self.assertEqual(AutoSuggetions.get_auto_suggestions(input1, input2), expected)

if __name__ == "__main__":
    unittest.main()