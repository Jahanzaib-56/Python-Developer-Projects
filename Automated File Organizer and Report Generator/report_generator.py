import csv
from pathlib import Path
from collections import defaultdict
import logging


def generate_summary(files: list) -> dict:
    """
    Generate summary statistics from file metadata.
    """
    summary = {
        "total_files": len(files),
        "files_per_category": defaultdict(int),
        "size_per_category_kb": defaultdict(float)
    }

    for f in files:
        category = f.get("category", "Others")
        size = f.get("size_kb", 0)

        summary["files_per_category"][category] += 1
        summary["size_per_category_kb"][category] += size

    return summary


def generate_csv_report(files: list, report_path: str) -> None:
    """
    Generate CSV report for organized files.

    Parameters:
        files (list): List of file metadata dictionaries
        report_path (str): Path to output CSV file
    """
    if not files:
        logging.warning("No files to write in report")
        return

    report_file = Path(report_path)
    report_file.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "name",
        "category",
        "size_kb",
        "path",
        "created_at",
        "modified_at"
    ]

    try:
        with open(report_file, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for f in files:
                writer.writerow({k: f.get(k) for k in fieldnames})

        summary = generate_summary(files)

        logging.info(f"Report generated at: {report_file}")
        logging.info(f"Total files: {summary['total_files']}")

        for category, count in summary["files_per_category"].items():
            logging.info(
                f"{category}: {count} files, "
                f"{round(summary['size_per_category_kb'][category], 2)} KB"
            )

    except Exception as e:
        logging.error(f"Failed to generate report: {e}")
