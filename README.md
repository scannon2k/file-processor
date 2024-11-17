# File Type Sorter 

This Python script organizes files in a specified directory by moving them into subdirectories based on file type.

## Setup

1. **Configure Path**:
   - Modify the `config.ini` file in the same directory as the script.
   - Add the following, replacing `/path/to/your/directory` with the target folder path:
     ```ini
     [filepath]
     path = /path/to/your/directory
     ```

2. **Run**:
   ```bash
   python3 file_sorter.py
   ```
   
## Logging

Errors are logged to `log.log` with timestamps.

# Keyword Based Sorter 

This Python script organizes files in a specified directory by moving them into subdirectories based on file name patterns. It also supports copying and uncompressing both `.zip` and `.gz` files, depending on what is present in the source directory. The script is compatible with both Windows and Unix-based systems.

## Features

- Supports uncompressing both `.zip` and `.gz` files.
- Copies `.zip` and `.gz` files to an "archive" folder.
- Uncompresses `.zip` and `.gz` files in the directory.
- Organizes files by moving them into subdirectories based on specific keywords in their names.
- Provides a verbose mode for detailed processing output.

## Requirements

- Python 3.x
- Modules: `os`, `shutil`, `zipfile`, `gzip`, `argparse`, `configparser`, `itertools`, `pathlib`

## Setup

1. **Create Configuration File**:
   - In the script directory, create a `config.ini` file to specify the source directory path.
   - Example `config.ini`:
     ```ini
     [Paths]
     source_directory = /path/to/your/directory
     ```
   - Replace `/path/to/your/directory` with the directory where you want to organize files.
   - On Windows, use backslashes `\\` in the path or a double backslash (`\\\\`) if escaping is required.

2. **Run**:
   - To run the script, use: 
     ```bash
      python3 process_files.py
      ```
      
   - For verbose output, use the -v option:
     ```bash
      python3 process_files.py --verbose
      python3 process_files.py -v
      ```
