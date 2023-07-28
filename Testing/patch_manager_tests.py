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

        PATCH = Patch.new(b"AAA", b"AAABBB", -1)
        PATCH.to_file(PATCH_DIR)
        MANAGER = PatchManager(PATCH_DIR, 0)

        MANAGER.clear_patches()
        PATCH_DIR.rmdir()
        



if __name__ == "__main__":
    unittest.main()