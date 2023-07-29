import os
import glob
from pathlib import Path
import sys

sys.path.append("src")
from patch import Patch


class PatchManager:
    def __init__(self, dir: Path, loaded_version=0) -> None:
        self.patches_dir: Path = dir
        self.patches: list[Patch] = self._read_patches()
        

    def _read_patches(self) -> list[Patch]:
        patches = []
        for patch_path in glob.glob(os.path.join(self.patches_dir, "*")):
            patch = Patch.from_file(Path(patch_path))
            patches.append(patch)
        return patches

    def new_version(self, new_bytes: bytes):
        patch = Patch.new(self.get_version(len(self.patches) - 1), new_bytes, len(self.patches))
        self.patches.append(patch)
        patch.to_file(self.patches_dir)

    def get_version(self, version: int) -> bytes:
        file: bytes = b""
        for patch in self.patches[:version+1]:
            file = patch.apply_patch(file)
        return file

    def clear_patches(self):
        patch_files = glob.glob(os.path.join(self.patches_dir, "*"))
        for patch_file in patch_files:
            os.unlink(patch_file)
