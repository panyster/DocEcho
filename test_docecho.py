# test_docecho.py
"""
Tests for DocEcho module.
"""

import unittest
from docecho import DocEcho

class TestDocEcho(unittest.TestCase):
    """Test cases for DocEcho class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DocEcho()
        self.assertIsInstance(instance, DocEcho)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DocEcho()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
