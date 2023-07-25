from pathlib import Path


class Version:

    def __init__(self, bound_file_path: Path, version: int) -> None:
        with open(bound_file_path, "rb") as file:
            content = file.read()
        self._content = content
        self._version = version
    
    def get_content(self) -> bytes:
        return self._content
    
    def get_version(self) -> int:
        return self._version
    
    def to_file(self, save_dir: Path) -> None:
        with open(self._save_path(save_dir), "wb") as file:
            file.write(self.get_content())

    def _save_path(self, save_dir: Path) -> Path:
        return save_dir.joinpath(f"{self._version}.easy_version")

    def delete(self, save_dir: Path) -> None:
        self._save_path(save_dir).unlink(True)
   

if __name__ == "__main__":
    BOUND_FILE_PATH = Path("Testing/test.txt")
    SAVE_DIR = BOUND_FILE_PATH.parent.joinpath("easy_vcs")

    VERSION_0 = Version(BOUND_FILE_PATH, 0)
    assert VERSION_0.get_version() == 0
    assert VERSION_0.get_content() == b"Version 1 content"

    VERSION_0.to_file(SAVE_DIR)
    assert Path("./Testing/easy_vcs/").exists()

    VERSION_0.delete(SAVE_DIR)
