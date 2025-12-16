import shutil
from pathlib import Path
import logging

def ensure_directory(path: Path) -> None:

    path.mkdir(parents=True, exist_ok=True)

def avoid_name_conflict(destination: Path) -> Path:

    if not destination.exists():
        return destination
    
    stem = destination.stem
    suffix = destination.suffix
    parent = destination.parent

    counter = 1

    while True:
        new_name = f"{stem} ({counter}){suffix}"

        new_path = parent / new_name

        if not new_path.exists():
            return new_path
        
        counter += 1

def move_file(file_meta: dict, output_base: str) -> dict | None:

    try:
        source = Path(file_meta["path"])

        if not source.exists():
            logging.warning(f"Source file missing: {source}")
            return None
        
        category = file_meta.get("category", "Others")
        target_dir = Path(output_base) / category

        ensure_directory(target_dir)

        destination = avoid_name_conflict(target_dir / source.name)

        shutil.move(str(source), str(destination))

        file_meta["path"] = str(destination)

        logging.info(f"Moved: {source.name} -> {destination}")
        return file_meta
    
    except PermissionError:
        logging.error(f"Permission denied while moving {file_meta["path"]}")
        return None
    
    except Exception as e:
        logging.error(f'Failed to move. Error occurred: {e}')
        return None
    