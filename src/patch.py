from pathlib import Path
import bsdiff4
import os

class TypeError(Exception):
    """Raise if the file you're checking is not a valid PatchFile."""

    def __init__(self, message="Invalid Patch file."):
        self.message = message
        super().__init__(self.message)


class Patch:
    def __init__(self, patch_data: bytes, version: int) -> None:
        self.patch_data: bytes = patch_data
        self.version: int = version

    def __eq__(self, __value: object) -> bool:
        return self.patch_data == __value.patch_data and self.version == __value.version

    @classmethod
    def new(cls, old_data: bytes, new_data: bytes, version: int) -> None:
        patch_data = bsdiff4.diff(old_data, new_data)
        return cls(patch_data, version)

    @classmethod
    def from_file(cls, file_path: Path):
        if file_path.suffix != ".easy_patch":
            raise TypeError("File is not a patch file.")
        try:
            version = int(file_path.stem)
        except ValueError:
            raise TypeError("Patch file doesn't contain an integer file stem.")
        if not file_path.exists():
            raise TypeError("No file found at the given path.")
        with open(file_path, "rb") as file:
            patch_data = file.read()
        return cls(patch_data, version)

    def apply_patch(self, old_bytes: bytes) -> bytes:
        return bsdiff4.patch(old_bytes, self.patch_data)

    def to_file(self, output_directory: Path) -> None:
        if not os.path.exists(output_directory):
            os.mkdir(output_directory)
        file_path = os.path.join(output_directory, f"{self.version}.easy_patch")
        with open(file_path, "wb") as file:
            file.write(self.patch_data)


if __name__ == "__main__":
    pass