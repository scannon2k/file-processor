#!/usr/bin/env python3

import os
import shutil
import zipfile
import gzip
import argparse
import configparser
import itertools
from pathlib import Path

def setup_parser():
    parser = argparse.ArgumentParser(description="Organize and uncompress files based on file types and name patterns.")
    parser.add_argument("--verbose", "-v", action="store_true", help="Increase output verbosity.")
    return parser.parse_args()

def read_config():
    config = configparser.ConfigParser()
    config.read("config.ini")
    try:
        source_directory = config.get("Paths", "source_directory")
        return Path(source_directory).expanduser()
    except (configparser.NoSectionError, configparser.NoOptionError) as e:
        print(f"Error reading source directory from config.ini: {e}")
        exit(1)

def create_archive_folder(directory, verbose):
    archive_folder = directory / "archive"
    if not archive_folder.exists():
        archive_folder.mkdir()
        if verbose:
            print(f"Created archive folder at: {archive_folder}")
    return archive_folder

def copy_files_to_archive(directory, archive_folder, verbose):
    # Combine .zip and .gz files using itertools.chain
    for file in itertools.chain(directory.glob("*.zip"), directory.glob("*.gz")):
        shutil.copy(file, archive_folder)
        if verbose:
            print(f"Copied {file} to {archive_folder}")

def uncompress_files(directory, verbose):
    # Uncompress .zip files
    for file in directory.glob("*.zip"):
        with zipfile.ZipFile(file, 'r') as zip_ref:
            zip_ref.extractall(directory)
            if verbose:
                print(f"Uncompressed {file} to {directory}")
        file.unlink()  # Remove the compressed file after extraction

    # Uncompress .gz files
    for file in directory.glob("*.gz"):
        output_file = directory / file.stem  # Remove .gz extension
        with gzip.open(file, 'rb') as gz_file:
            with open(output_file, 'wb') as out_file:
                shutil.copyfileobj(gz_file, out_file)
                if verbose:
                    print(f"Uncompressed {file} to {output_file}")
        file.unlink()  # Remove the compressed file after extraction

def move_files(directory, verbose):
    keywords = ["cat", "dog"]  # Add more as needed
    for keyword in keywords:
        target_folder = directory / keyword
        if not target_folder.exists():
            target_folder.mkdir()
            if verbose:
                print(f"Created target folder: {target_folder}")
        
        # Move files based on keywords in the name
        for file in directory.glob(f"*{keyword}*"):
            if file.is_file():
                shutil.move(str(file), str(target_folder))
                if verbose:
                    print(f"Moved {file} to {target_folder}")

def main():
    args = setup_parser()
    directory = read_config()

    if not directory.exists():
        print(f"Directory {directory} does not exist.")
        return

    archive_folder = create_archive_folder(directory, args.verbose)
    copy_files_to_archive(directory, archive_folder, args.verbose)
    uncompress_files(directory, args.verbose)
    move_files(directory, args.verbose)

    if args.verbose:
        print("Completed organizing and uncompressing files.")

# Call main if being executed directly
if __name__ == "__main__":
    main()
