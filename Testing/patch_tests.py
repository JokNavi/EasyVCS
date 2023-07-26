import bsdiff4
import sys
sys.path.append(".")
from src.patch import Patch

def init_test():
    OLD: bytes = b"AAA"
    NEW: bytes =  b"AAABBB"
    patch_data = bsdiff4.diff(OLD, NEW)
    PATCH: Patch = Patch(patch_data, 0)
    assert PATCH.patch_data == patch_data
    assert PATCH.version == 0
    
    

def new_test():
    OLD: bytes = b"AAA"
    NEW: bytes =  b"AAABBB"
    PATCH: Patch = Patch.new(OLD, NEW, 0)
    assert PATCH.patch_data == bsdiff4.diff(OLD, NEW)
    assert PATCH.version == 0



if __name__ == "__main__":
    init_test()
    new_test()
    