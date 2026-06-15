import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, parent_dir)

import unittest
from src.dfa import dfa_search
class TestDFASearch(unittest.TestCase):
    
    def test_standard_search(self):
        """Test finding multiple occurrences in a standard string."""
        self.assertEqual(dfa_search("AABAACAADAABAABA", "AABA"), [0, 9, 12])
        
    def test_no_match(self):
        """Test when the needle is not present in the haystack."""
        self.assertEqual(dfa_search("HELLO WORLD", "TEST"), [])
        
    def test_empty_needle(self):
        """Test with an empty needle string."""
        self.assertEqual(dfa_search("ANY TEXT", ""), [])
        
    def test_empty_haystack(self):
        """Test with an empty haystack string."""
        self.assertEqual(dfa_search("", "NEEDLE"), [])
        
    def test_overlapping_matches(self):
        """Test if the algorithm correctly finds overlapping matches."""
        self.assertEqual(dfa_search("AAAA", "AA"), [0, 1, 2])
        
    def test_haystack_shorter_than_needle(self):
        """Test when the text is shorter than the pattern to find."""
        self.assertEqual(dfa_search("SHORT", "LONGER_NEEDLE"), [])
        
    def test_exact_match(self):
        """Test when haystack and needle are exactly the same."""
        self.assertEqual(dfa_search("EXACT", "EXACT"), [0])
        

if __name__ == '__main__':
    unittest.main()