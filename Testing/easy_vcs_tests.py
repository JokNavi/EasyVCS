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
        TEST_VCS = EasyVCS.new("Test_VCS", BOUND_FILE_PATH)
        self.assertEqual(TEST_VCS.name, "Test_VCS".lower())
        self.assertEqual(TEST_VCS.bound_file_path, BOUND_FILE_PATH.resolve())
        TEST_VCS.delete()

    def test_new_version(self):
        BOUND_FILE_PATH = Path("Files/Bound_file.txt")
        TEST_VCS = EasyVCS.new("Test_VCS", BOUND_FILE_PATH)

        BOUND_FILE_PATH.write_text("Version 0")
        TEST_VCS.save()
        BOUND_FILE_PATH.write_text("Version 1")
        TEST_VCS.save()

        TEST_VCS.load(0)
        self.assertEqual(BOUND_FILE_PATH.read_bytes(), b"Version 0")

        TEST_VCS.load(1)
        self.assertEqual(BOUND_FILE_PATH.read_bytes(), b"Version 1")
        
        TEST_VCS.load(2)
        self.assertEqual(BOUND_FILE_PATH.read_bytes(), b"Version 1")
        
        TEST_VCS.delete()

if __name__ == "__main__":
    unittest.main()
        