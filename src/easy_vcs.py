import os
from pathlib import Path
from patch import Version

class EasyVCS:
    def __init__(self, bound_file_path: Path, name = None) -> None:
        self.bound_file_path: Path = bound_file_path
        self.name: str = name or self.bound_file_path.stem
        self.save_dir: Path = bound_file_path.parent.joinpath("easy_vcs").joinpath(self.name)
        self.save_dir.mkdir(parents=True, exist_ok=True)
        self.versions = [Version(self.save_dir.joinpath(p), int(Path(p).stem)) for p in os.listdir(self.save_dir) if Path(p).suffix == ".easy_version"]
        
    
    def save(self):
        version_numbers = [number.get_version() for number in self.versions]
        version_number = max(version_numbers) + 1 if version_numbers != [] else 0
        version = Version(self.bound_file_path, version_number)
        version.to_file(self.save_dir)
        self.versions.append(version)

    def delete(self):
        for version in self.versions:
            version.delete(self.save_dir)
        self.save_dir.rmdir()
    
        

if __name__ == "__main__":
    BOUND_FILE_PATH = Path("Testing/test.txt")
    TEST_VCS = EasyVCS(BOUND_FILE_PATH)
    assert TEST_VCS.bound_file_path == BOUND_FILE_PATH
    assert TEST_VCS.name == BOUND_FILE_PATH.stem
    assert TEST_VCS.save_dir == BOUND_FILE_PATH.parent.joinpath("easy_vcs").joinpath(TEST_VCS.name)

    TEST_VCS.delete()