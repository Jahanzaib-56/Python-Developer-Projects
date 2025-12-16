import logging
from datetime import datetime
from pathlib import Path

from scanner import scan_directory
from classifier import load_rules, file_classifier
from organizer import move_file
from report_generator import generate_csv_report


# ---------------- CONFIGURATION ---------------- #

SOURCE_DIR = r"F:\files"
PROJECT_ROOT = Path(__file__).parent

OUTPUT_DIR = PROJECT_ROOT / "organized_files"
REPORTS_DIR = PROJECT_ROOT / "reports"
CONFIG_PATH = PROJECT_ROOT / "config.json"


# ---------------- LOGGING SETUP ---------------- #

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.StreamHandler()
        ]
    )


# ---------------- MAIN PIPELINE ---------------- #

def main():
    setup_logger()
    start_time = datetime.now()

    logging.info("Starting File Organizer")

    # 1️⃣ Scan directory
    files = scan_directory(SOURCE_DIR)
    logging.info(f"Scanned {len(files)} files")

    if not files:
        logging.warning("No files found. Exiting.")
        return

    # 2️⃣ Load classification rules
    rules = load_rules(str(CONFIG_PATH))
    if not rules:
        logging.error("Failed to load classification rules. Exiting.")
        return

    # 3️⃣ Classify files
    classified_files = [file_classifier(f, rules) for f in files]

    # 4️⃣ Organize files
    organized_files = []
    for f in classified_files:
        result = move_file(f, str(OUTPUT_DIR))
        if result:
            organized_files.append(result)

    logging.info(f"Successfully organized {len(organized_files)} files")

    # 5️⃣ Generate report
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_path = REPORTS_DIR / f"file_report_{timestamp}.csv"

    generate_csv_report(organized_files, str(report_path))

    # 6️⃣ Done
    duration = datetime.now() - start_time
    logging.info(f"Completed in {duration}")


# ---------------- ENTRY POINT ---------------- #

if __name__ == "__main__":
    main()
