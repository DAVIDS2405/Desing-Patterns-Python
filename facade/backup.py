import datetime
import shutil
import zipfile
import os


class FileCompressor:
    def compress(self, file_path):
        output_path = file_path + ".zip"
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(file_path, os.path.basename(file_path))
        return output_path


class FileBackup:
    def __init__(self, backup_dir="backup"):
        self.backup_dir = backup_dir
        os.makedirs(backup_dir, exist_ok=True)

    def copy(self, file_path):
        timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        backup_path = os.path.join(self.backup_dir, f"{file_path}_{timestamp}")
        shutil.copy2(file_path, backup_path)
        return backup_path


class FileFacade:
    def __init__(self):
        self.compressor = FileCompressor()
        self.backup = FileBackup()

    def process(self, file_path):
        backup_path = self.backup.copy(file_path)
        print(f"Backup created at {backup_path}")

        compressed_path = self.compressor.compress(backup_path)
        print(f"File compressed to {compressed_path}")


facade = FileFacade()
facade.process("doc.txt")
