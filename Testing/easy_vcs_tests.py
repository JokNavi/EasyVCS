import os
from pathlib import Path
import unittest
import sys
sys.path.append(".")
from src.patch import Patch
from src.easy_vcs import EasyVCS
    
class TestPatch(unittest.TestCase):
    
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.FILE_PATH: Path = Path("Files/test.txt")
        self.NAME = self.FILE_PATH.stem
        self.HEADER_DIR: Path = Path(os.path.join(self.FILE_PATH.parent, self.NAME))
        self.HEADER_PATH: Path = Path(os.path.join(self.HEADER_DIR, f"{self.NAME}.easy_vcs"))

    def test_create_header_file(self):
        self.HEADER_PATH.unlink(True)
        self.HEADER_DIR.rmdir()

        EASY_VCS = EasyVCS(self.FILE_PATH, self.NAME)
        EASY_VCS._create_header_file()
        self.assertTrue(self.HEADER_DIR.exists())
        self.assertTrue(self.HEADER_PATH.exists())

    def test_new(self):
        self.HEADER_PATH.unlink(True)
        self.HEADER_DIR.rmdir()

        EASY_VCS = EasyVCS.new(self.FILE_PATH, self.NAME)
        self.assertTrue(self.HEADER_DIR.exists())
        self.assertTrue(self.HEADER_PATH.exists())
    
    def test_from_file(self):
        self.HEADER_PATH.unlink(True)
        self.HEADER_DIR.rmdir()

        EASY_VCS = EasyVCS.new(self.FILE_PATH, self.NAME)
        self.assertTrue(self.HEADER_DIR.exists())
        self.assertTrue(self.HEADER_PATH.exists())

        READ_EASY_VCS = EasyVCS.from_file(self.HEADER_PATH)
        self.assertEqual(READ_EASY_VCS, EASY_VCS)

        
        
if __name__ == "__main__":
    unittest.main()
        