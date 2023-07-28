import os
from pathlib import Path
import sys

sys.path.append("src")
from patch import Patch


class PatchManager:
    def __init__(self, dir: Path, loaded_version=0) -> None:
        self.patches_dir: Path = dir
        self.loaded_patch: int = loaded_version
        self.patches: list[Patch] = self._read_patches()

    def _read_patches(self):
        return [
            Patch.from_file(Path(os.path.join(self.patches_dir, patch_path)))
            for patch_path in os.listdir(self.patches_dir)
            if os.path.isfile(os.path.join(self.patches_dir, patch_path))
        ]

    def current_version_number(self) -> int:
        return self.loaded_patch

    def create_version(self, new_bytes: bytes):
        pass

    def get_version(self, version: int) -> bytes:
        file: bytes = b""
        i = 0
        while i <= version:
            file = self.patches[i].apply_patch(file)
            i += 1
        return file
        



    def clear_patches(self):
        return [Path(os.path.join(self.patches_dir, patch_path)).unlink() for patch_path in os.listdir(self.patches_dir)]
