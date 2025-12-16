# File Organizer & Report Generator

**A professional Python automation tool to organize files and generate summary reports.**

---

## 🏆 Project Overview

This project automates the organization of files from a source directory (like Downloads) into category-based folders such as Documents, Images, Videos, Code, and Others. It also generates a comprehensive CSV report summarizing all files with metadata like size, timestamps, and category.

The tool is designed to be **modular, safe, and production-ready**, making it a strong addition to your Python portfolio.

**Key highlights:**

* Modular Python design (scanner, classifier, organizer, reporter)
* Safe handling of files (prevents overwrites, skips inaccessible files)
* Config-driven classification (easy to add new file types)
* Generates structured CSV reports for analysis
* Windows and cross-platform friendly

---

## 🗂 Features

* ✅ **Directory Scanning:** Automatically detects all files in the given source directory.
* ✅ **File Classification:** Categorizes files based on extensions defined in `config.json`.
* ✅ **Safe File Organization:** Moves files into separate folders in `organized_files/` and handles naming conflicts.
* ✅ **Report Generation:** Creates CSV reports with per-file metadata and category summaries.
* ✅ **Logging:** Detailed logs for all operations, errors, and skipped files.
* ✅ **Config-Driven:** Easily extendable file type rules through `config.json`.

---

## 📁 Project Structure

```
File Organizer/
│
├── main.py                  # Entry point
├── scanner.py               # Scans directories and extracts metadata
├── classifier.py            # Classifies files into categories
├── organizer.py             # Moves files safely into folders
├── report_generator.py      # Generates CSV reports
├── config.json              # File type rules
├── organized_files/         # Output folder for organized files
├── reports/                 # Folder for generated CSV reports
└── README.md
```

---

## ⚙️ How It Works

1. **Scan Directory:** `scanner.py` collects file metadata (name, extension, size, created/modified timestamps).
2. **Classify Files:** `classifier.py` assigns a category to each file using `config.json`.
3. **Organize Files:** `organizer.py` safely moves files into `organized_files/<Category>/`. Conflicts are resolved automatically.
4. **Generate Report:** `report_generator.py` generates a timestamped CSV report summarizing files per category and size.

---

## 🚀 Installation & Usage

1. Clone this repository:

```bash
git clone <your-repo-url>
cd File Organizer
```

2. Set the `SOURCE_DIR` in `main.py` to the folder you want to organize.
3. Run the project:

```bash
python main.py
```

4. Check `organized_files/` for your sorted files and `reports/` for the CSV report.

---

## 🛡 Safety Notes

* Files are moved to a **separate output folder** to prevent accidental overwrites in the original directory.
* Files that are in use, locked, or inaccessible are **skipped safely**, with warnings logged.
* Naming conflicts are resolved by appending `(1)`, `(2)`, etc., to avoid overwriting files.

---

## 🛠 Tech Stack

* Python 3.x
* Standard libraries: `pathlib`, `shutil`, `csv`, `logging`, `datetime`
* Config-driven design using `JSON`

---

## 📊 Sample Report

| Name       | Category  | Size (KB) | Path                                 | Created At | Modified At |
| ---------- | --------- | --------- | ------------------------------------ | ---------- | ----------- |
| resume.pdf | Documents | 245.6     | organized_files/Documents/resume.pdf | 2025-12-10 | 2025-12-11  |
| photo.png  | Images    | 1024.3    | organized_files/Images/photo.png     | 2025-12-09 | 2025-12-09  |

---

## 👨‍💻 About This Project

This project was developed as a Python portfolio project showcasing modular design, file system automation, and reporting.
To achieve professional design and efficiency, I also leveraged **AI-assisted guidance** to structure modules, ensure error handling, and implement best practices — while all coding, testing, and decision-making was performed manually by me.

> This approach allowed me to focus on **software design, modularity, and safety**, ensuring a clean, maintainable, and recruiter-ready project.

---

## 💡 Future Improvements

* Add **Excel (.xlsx) report generation** for advanced formatting
* Add **recursive scanning** for subfolders
* Implement **CLI with `argparse`** for dynamic input paths and options
* Add **GUI** for easier usage

---

## 📝 Author

**Jahanzaib** – Aspiring Python Developer | AI & Automation Enthusiast
