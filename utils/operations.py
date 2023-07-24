import os
import pathlib
import shutil

from utils.custom_types import Path

class FileOperations:
    def __init__(self, path: Path):
        self.path = path

    def create_folder(self) -> None:
        if self.path.is_dir(): self.path.mkdir(parents=True, exist_ok=True)
    
    def delete_folder(self) -> None:
        if self.path.is_dir(): shutil.rmtree(self.path)
    
    def create_file(self) -> None:
        if self.path.is_file(): self.path.touch()
    
    def delete_file(self) -> None:
        if self.path.is_file(): self.path.unlink()

# Path: utils/__init__.py