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

    def test_create_header_file(self):

        EASY_VCS = EasyVCS(self.FILE_PATH, self.NAME)
        EASY_VCS._create_header_file()
        self.assertTrue(EASY_VCS._vcs_dir.exists())
        self.assertTrue(EASY_VCS._patch_dir.exists())
        EASY_VCS.delete()

    # def test_new(self):
    #     self.HEADER_PATH.unlink(True)

    #     EASY_VCS = EasyVCS.new(self.FILE_PATH, self.NAME)
    #     self.assertTrue(self.HEADER_DIR.exists())
    #     self.assertTrue(self.HEADER_PATH.exists())
    
    # def test_from_file(self):
    #     self.HEADER_PATH.unlink(True)

    #     EASY_VCS = EasyVCS.new(self.FILE_PATH, self.NAME)
    #     self.assertTrue(self.HEADER_DIR.exists())
    #     self.assertTrue(self.HEADER_PATH.exists())

    #     READ_EASY_VCS = EasyVCS.from_file(self.HEADER_PATH)
    #     self.assertEqual(READ_EASY_VCS, EASY_VCS)

    # def test_read_patches(self):
    #     directory = Path("Files/test/patches")
    #     patch = Patch.new(b"AAA", b"AAABBB", -1)
    #     file_path = directory / "-1.easy_patch"
    #     file_path.unlink(missing_ok=True)
    #     patch.to_file(directory)
        
        
if __name__ == "__main__":
    unittest.main()
        