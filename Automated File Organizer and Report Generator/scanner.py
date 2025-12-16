from pathlib import Path
from datetime import datetime
import logging

def get_metadata(file_path: Path) -> dict:

    try:
        stats = file_path.stat()

        return {
            'name': file_path.name,
            'path': str(file_path),
            'extension': file_path.suffix.lower(),
            'size_kb': round(stats.st_size / 1024, 2),
            'created at': datetime.fromtimestamp(stats.st_birthtime),
            'modified_at': datetime.fromtimestamp(stats.st_mtime),
            'category': None
        }
    
    except PermissionError:
        logging.warning(f"Permission denied: {file_path}")
        return None

    except FileNotFoundError:
        logging.warning(f"File disappeared during scan: {file_path}")
        return None

    except Exception as e:
        logging.error(f"Unexpected error for {file_path}: {e}")
        return None
    
def scan_directory(dir_path: Path) -> list:

    files_metadata = []
    base_path = Path(dir_path)

    if not base_path.exists():
        logging.error("Directory does not exists")
        return files_metadata
    
    if not base_path.is_dir():
        logging.error('provided path is not a directory')
        return files_metadata
    
    for item in base_path.iterdir():
        if item.is_file():
            metadata = get_metadata(item)
            if metadata:
                files_metadata.append(metadata)

    logging.info(f"Scanned {len(files_metadata)} file from given directory path")
    return files_metadata
