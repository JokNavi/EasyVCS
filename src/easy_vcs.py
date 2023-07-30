import os
import glob
from pathlib import Path
import sys
sys.path.append("src")
from patch_manager import PatchManager

class EasyVCS:

    def __init__(self, vcs_file_path: Path) -> None:
        name, bound_file_path, loaded_version = self.read_easy_vcs_save(vcs_file_path.resolve())
        self.name: str = name
        self.bound_file_path: Path = bound_file_path
        self.loaded_version: int = loaded_version
        self.patch_manager: PatchManager = PatchManager(vcs_file_path.parent / "versions")


    @classmethod
    def new(cls, name: str, bound_file_path: Path, loaded_version: int = 0):
        vcs_dir = bound_file_path.parent.resolve() / "easy_vcs" / name.lower()
        os.makedirs(vcs_dir, exist_ok=True)
        vcs_file_path = vcs_dir / f"{name.lower()}.easy_vcs"
        with open(vcs_file_path, "w") as file:
            file.write(f"{name.lower()}\n{str(bound_file_path.resolve())}\n{str(loaded_version)}\n")
        return cls(vcs_file_path)

    @staticmethod
    def read_easy_vcs_save(save_path: Path):
        if not save_path.exists():
            return None, None, None
        with open(save_path, "r") as file:
            name, bound_file_path, loaded_version = [line.strip() for line in file.readlines()]
            return name, Path(bound_file_path), int(loaded_version)

    def delete(self):
        vcs_dir = self.bound_file_path.parent.resolve() / "easy_vcs" / self.name.lower()
        vcs_file_path = vcs_dir / f"{self.name}.easy_vcs"

        self.patch_manager.delete()
        vcs_file_path.unlink()
        vcs_dir.rmdir()
        

if __name__ == "__main__":
    pass

