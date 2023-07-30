import os
from pathlib import Path
import unittest
import sys
sys.path.append(".")
from src.easy_vcs import EasyVCS
    
class TestPatch(unittest.TestCase):
    
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        

    def test_init(self):
        BOUND_FILE_PATH = Path("Files/Bound_file.txt")
        EASY_VCS = EasyVCS.new("Test_VCS", BOUND_FILE_PATH, 0)
        self.assertEqual(EASY_VCS.name, "Test_VCS".lower())
        self.assertEqual(EASY_VCS.bound_file_path, BOUND_FILE_PATH.resolve())
        self.assertEqual(EASY_VCS.loaded_version, 0)
        EASY_VCS.delete()


if __name__ == "__main__":
    unittest.main()
        