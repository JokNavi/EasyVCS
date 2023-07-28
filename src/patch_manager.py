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
            Patch.from_file(patch_path)
            for patch_path in os.listdir(self.patches_dir)
            if os.path.isfile(patch_path)
        ]

    def loaded_version(self) -> int:
        return self.loaded_patch

    def save(self, new_bytes: bytes):
        pass

    def load(self, version: int):
        pass

    def clear_patches(self):
        return [Path(os.path.join(self.patches_dir, patch_path)).unlink() for patch_path in os.listdir(self.patches_dir)]
