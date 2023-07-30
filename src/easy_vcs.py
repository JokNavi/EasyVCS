import os
import glob
from pathlib import Path
import sys
sys.path.append("src")
from patch_manager import PatchManager

class EasyVCS:

    def __init__(self, vcs_file_path: Path) -> None:
        name, bound_file_path = self.read_easy_vcs_save(vcs_file_path.resolve())
        self.name: str = name
        self.bound_file_path: Path = bound_file_path
        self.patch_manager: PatchManager = PatchManager(vcs_file_path.parent / "versions")


    @classmethod
    def new(cls, name: str, bound_file_path: Path):
        vcs_dir = bound_file_path.parent.resolve() / "easy_vcs" / name.lower()
        os.makedirs(vcs_dir, exist_ok=True)
        vcs_file_path = vcs_dir / f"{name.lower()}.easy_vcs"
        with open(vcs_file_path, "w") as file:
            file.write(f"{name.lower()}\n{str(bound_file_path.resolve())}\n")
        return cls(vcs_file_path)

    @staticmethod
    def read_easy_vcs_save(save_path: Path):
        if not save_path.exists():
            return None, None, None
        with open(save_path, "r") as file:
            name, bound_file_path = [line.strip() for line in file.readlines()]
            return name, Path(bound_file_path)

    def delete(self):
        vcs_dir = self.bound_file_path.parent.resolve() / "easy_vcs" / self.name.lower()
        vcs_file_path = vcs_dir / f"{self.name}.easy_vcs"

        self.patch_manager.delete()
        vcs_file_path.unlink()
        vcs_dir.rmdir()

    def save(self):
        new_bytes = self.bound_file_path.read_bytes()
        self.patch_manager.new_version(new_bytes)

    def load(self, version: int):
        new_bytes = self.patch_manager.get_version(version)
        self.bound_file_path.write_bytes(new_bytes)
        

if __name__ == "__main__":
    pass

