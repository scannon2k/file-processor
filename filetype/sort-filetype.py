#!/usr/bin/env python3
import os
import shutil
import logging
from configparser import ConfigParser

# Set up logging to log.log
logging.basicConfig(filename='log.log', level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Load file path from config.ini
config = ConfigParser()
config.read('config.ini')

try:
    path = config['filepath']['path']
except KeyError:
    logging.error("Config file is missing 'filepath' or 'path' entry.")
    raise

# Ensure the path exists
if not os.path.isdir(path):
    logging.error(f"The specified path '{path}' does not exist or is not a directory.")
    raise FileNotFoundError(f"The specified path '{path}' does not exist or is not a directory.")

try:
    file_list = os.listdir(path)
except OSError as e:
    logging.error(f"Error accessing the directory '{path}': {e}")
    raise

# Sort files by extension
for file in file_list:
    try:
        name, ext = os.path.splitext(file)
        ext = ext[1:]  # remove the dot from the extension

        # Skip directories
        if not ext:
            continue

        # Target directory for this extension
        target_dir = os.path.join(path, ext)

        # Create target directory if it doesn't exist
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        # Move file to target directory
        shutil.move(os.path.join(path, file), os.path.join(target_dir, file))

    except (OSError, shutil.Error) as e:
        logging.error(f"Error moving file '{file}': {e}")
