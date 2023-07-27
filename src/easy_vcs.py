import os
from pathlib import Path

class EasyVCS:

    def __init__(self, bound_file_path: Path, name: str) -> None:
        if not os.path.exists(bound_file_path):
            return FileNotFoundError()
        self.bound_file_path = bound_file_path
        self.name = name

    def __eq__(self, __value: object) -> bool:
        return self.bound_file_path == __value.bound_file_path and self.name == __value.name
    
    def _create_header_file(self):
        header_dir: Path = Path(os.path.join(self.bound_file_path.parent, f"{self.name}"))
        header_dir.mkdir(exist_ok=True)
        header_path: str = os.path.join(header_dir, f"{self.name}.easy_vcs")
        with open(header_path, "w") as file:
            file.write(os.path.abspath(self.bound_file_path) + "\n")
            file.write(self.name + "\n")

    @classmethod
    def new(cls, bound_file_path: Path, name: str):
        easy_vcs = EasyVCS(bound_file_path, name)
        easy_vcs._create_header_file()
        return easy_vcs

    @classmethod
    def from_file(cls, header_path: Path):
        with open(header_path, "r") as file:
            lines = file.readlines()
            bound_file_path: Path = Path(lines[0])
            name: str = str(lines[1])
        return cls(bound_file_path, name)  


if __name__ == "__main__":
    EasyVCS(Path("Files/test.txt"), "test")
        
    