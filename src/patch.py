from pathlib import Path
import difflib


class Version:

    def __init__(self, old_bytes: bytes, new_bytes: bytes, version: int) -> None:
        pass

    def apply_patch(self, old_bytes: bytes) -> bytes:
        pass

    def revert_patch(self, new_bytes: bytes) -> bytes:
        pass

if __name__ == "__main__":
    pass
