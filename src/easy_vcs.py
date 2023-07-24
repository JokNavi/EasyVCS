from pathlib import Path

class EasyVCS:
    def __init__(self, bound_file_path: Path, name = None) -> None:
        self.bound_file_path = bound_file_path
        self.save_path = bound_file_path.parent.joinpath("easy_vcs")
        self.name = name or self.bound_file_path.stem


if __name__ == "__main__":
    VERSION_0 = EasyVCS("./Testing/target_file.txt")
    print()