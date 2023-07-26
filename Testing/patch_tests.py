from pathlib import Path
import bsdiff4
import unittest
import sys
sys.path.append(".")
from src.patch import Patch
    
class TestPatch(unittest.TestCase):

    def test_apply_patch(self):
        OLD: bytes = b"AAA"
        NEW: bytes =  b"AAABBB"
        PATCH: Patch = Patch.new(OLD, NEW, 0)
        self.assertEqual(PATCH.apply_patch(OLD), NEW)

    def test_new_constructor(self):
        OLD: bytes = b"AAA"
        NEW: bytes =  b"AAABBB"
        PATCH: Patch = Patch.new(OLD, NEW, 0)
        self.assertEqual(PATCH.patch_data, bsdiff4.diff(OLD, NEW))
        self.assertEqual(PATCH.version, 0)

    def test_init_constructor(self):
        OLD: bytes = b"AAA"
        NEW: bytes =  b"AAABBB"
        PATCH_DATA = bsdiff4.diff(OLD, NEW)
        PATCH: Patch = Patch(PATCH_DATA, 0)
        self.assertEqual(PATCH.patch_data, PATCH_DATA)
        self.assertEqual(PATCH.version, 0)

    def test_to_file(self):
        VERSION = -1
        OLD: bytes = b"AAA"
        NEW: bytes =  b"AAABBB"
        PATCH: Patch = Patch.new(OLD, NEW, VERSION)

        DIR: Path = Path("Files")
        FILE_PATH: Path = DIR.joinpath(f"{VERSION}.easy_patch")
        
        FILE_PATH.unlink(True)
        self.assertFalse(FILE_PATH.exists())

        PATCH.to_file(DIR)
        self.assertTrue(FILE_PATH.exists())
       
        

if __name__ == "__main__":
    unittest.main()
    