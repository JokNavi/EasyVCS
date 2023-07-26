from pathlib import Path
import bsdiff4


class TypeError(Exception):
    """Raise if the file you're checking is not a valid PatchFile."""

    def __init__(self, message="Invalid Patch file."):
        self.message = message
        super().__init__(self.message)


class Patch:
    def __init__(self, patch_data: bytes, version: int) -> None:
        self.patch_data: bytes = patch_data
        self.version: int = version

    @classmethod
    def new(cls, old_data: bytes, new_data: bytes, version: int) -> None:
        patch_data = bsdiff4.diff(old_data, new_data)
        return cls(patch_data, version)


    @classmethod
    def from_file(cls: object, path: Path):
        if not path.suffix == ".easy_patch":
            raise TypeError("File is not a patch file.")
        try:
            version = int(path.stem)
        except ValueError:
            raise TypeError("Patch file doesn't contain a integer type file stem.")
        if not path.exists():
            raise TypeError("No file found at Path.")
        with open(path, "wb") as f:
            patch_data = f.read()
        return cls(patch_data, version)

    def apply_patch(self, old_bytes: bytes) -> bytes:
        pass

    def revert_patch(self, new_bytes: bytes) -> bytes:
        pass

    def to_file(self, dir: Path) -> None:
        pass


if __name__ == "__main__":
    # old_data = b"old data"
    # new_data = b"new data"

    # delta = bsdiff4.diff(old_data, new_data)

    # # Save the delta to a file
    # with open("delta.patch", "wb") as f:
    #     f.write(delta)

    # old_data = b"old data"

    # # Load the delta from a file
    # with open("delta.patch", "rb") as f:
    #     delta = f.read()

    # new_data = bsdiff4.patch(old_data, delta)

    # print(new_data)
    pass
