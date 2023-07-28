import os
from pathlib import Path
import unittest
import sys
sys.path.append(".")
from src.patch import Patch
from src.patch_manager import PatchManager

    
class TestPatchManager(unittest.TestCase):
    

    def test_init(self):
        PATCH_DIR = Path("Files/versions")
        PATCH_DIR.mkdir(True)

        PATCH = Patch.new(b"AAA", b"AAABBB", 1)
        PATCH.to_file(PATCH_DIR)
        MANAGER = PatchManager(PATCH_DIR, 0)
        
        self.assertEqual(len(MANAGER.patches), 1)

        MANAGER.clear_patches()
        PATCH_DIR.rmdir()

    def test_get_version(self):
        PATCH_DIR = Path("Files/versions")
        PATCH_DIR.mkdir(True)

        PATCH_0 = Patch.new(b"", b"AAA", 0)
        PATCH_1 = Patch.new(b"AAA", b"AAABBB", 1)
        PATCH_0.to_file(PATCH_DIR)
        PATCH_1.to_file(PATCH_DIR)
        MANAGER = PatchManager(PATCH_DIR, 0)
        
        self.assertEquals(MANAGER.get_version(0), b"AAA")
        self.assertEquals(MANAGER.get_version(1), b"AAABBB")

        MANAGER.clear_patches()
        PATCH_DIR.rmdir()

        
if __name__ == "__main__":
    unittest.main()