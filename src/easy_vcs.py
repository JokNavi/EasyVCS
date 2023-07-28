import os
from pathlib import Path
import sys
sys.path.append("src")
from patch import Patch


class EasyVCS:
    def __init__(self, bound_file_path: Path, name: str) -> None:
        if not os.path.exists(bound_file_path):
            return FileNotFoundError()
        self.bound_file_path: Path = bound_file_path
        self.name: str = name

        self._vcs_dir: Path = Path(os.path.join(self.bound_file_path.parent, f"{self.name}"))
        self._patch_dir: Path = Path(os.path.join(self._vcs_dir, "patches"))
        self._vcs_dir.mkdir(exist_ok=True)
        self._patch_dir.mkdir(exist_ok=True)

        self._patches: list[Patch] = self.__read_patches()
        self._create_header_file()

    def __eq__(self, __value: object) -> bool:
        return (
            self.bound_file_path == __value.bound_file_path
            and self.name == __value.name
        )

    def _create_header_file(self):
        header_path: str = os.path.join(self._vcs_dir, f"{self.name}.easy_vcs")
        with open(header_path, "w") as file:
            file.write(os.path.abspath(self.bound_file_path) + "\n")
            file.write(self.name + "\n")

    def __read_patches(self):
        patches = list()
        for patch_path in [f for f in os.listdir(self._patch_dir) if os.path.isfile(f)]:
            try:
                patches.append(Patch.from_file(patch_path))
            except TypeError:
                pass
        return patches

    @classmethod
    def from_file(cls, header_path: Path):
        with open(header_path, "r") as file:
            lines = file.readlines()
            bound_file_path: Path = Path(lines[0][:-1])
            name: str = str(lines[1][:-1])
        return cls(bound_file_path, name)
    
    def delete(self):
        header_path: Path = Path(os.path.join(self._vcs_dir, f"{self.name}.easy_vcs"))

        for path in os.listdir(self._patch_dir):
            path.unlink(True)
            
        self._patch_dir.rmdir()
        header_path.unlink(True)
        self._vcs_dir.rmdir()


if __name__ == "__main__":
    VCS = EasyVCS(Path("Files/test.txt"), "test")
    VCS.delete()
