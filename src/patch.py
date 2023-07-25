from pathlib import Path
import difflib


class Patch:

    def __init__(self, old_bytes: bytes, new_bytes: bytes, version: int) -> None:
        pass

    @classmethod
    def from_file(cls: object, path: Path):
        pass
    
    def apply_patch(self, old_bytes: bytes) -> bytes:
        pass

    def revert_patch(self, new_bytes: bytes) -> bytes:
        pass

    def to_file(self, dir: Path) -> None:
        pass

if __name__ == "__main__":
    pass
