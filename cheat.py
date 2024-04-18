import json
from pathlib import Path
import logging
from datetime import datetime
import sys
import os
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Check if running under WSL
if 'microsoft' in os.uname().release:
    def get_wsl_windows_home():
        try:
            # Try fetching the USERPROFILE environment variable first
            user_profile = os.environ['USERPROFILE']
            # Normalize the Windows path to a WSL path
            path_components = user_profile.split('\\')
            windows_home = Path('/mnt', path_components[0][0].lower()) / Path(*path_components[1:])
        except KeyError:
            # Fallback to a conventional WSL path if USERPROFILE is not available
            # This assumes that the WSL username matches the Windows username and that Windows is installed on C:
            wsl_user = os.environ['USER']
            windows_home = Path('/mnt/c/Users', wsl_user)
        return windows_home
    # It's WSL, adjust the path for Windows files accordingly
    windows_home = get_wsl_windows_home()
    SAVE_FILE_DIR = windows_home / 'AppData' / 'LocalLow' / 'Torpor Games' / 'Suzerain'
elif sys.platform.startswith('win32'):
    # Regular Windows
    SAVE_FILE_DIR = Path.home() / 'AppData' / 'LocalLow' / 'Torpor Games' / 'Suzerain'
else:
    # TODO: Other OS's
    SAVE_FILE_DIR = Path.home() / '.local' / 'share' / 'Torpor Games' / 'Suzerain'

try:
    with open('keys_to_modify.json', 'r') as file:
        KEYS_TO_MODIFY = json.load(file)
except FileNotFoundError:
    logging.error("keys_to_modify.json file not found")

def update_variables(variables_str, keys_to_modify):
    for key, value in keys_to_modify.items():
        logging.info(f"Updating variable: {key} to {value}")
        search_str = f"[\"{key}\"]="
        index_start = variables_str.find(search_str) + len(search_str)
        index_end = index_start
        while variables_str[index_end] in "0123456789":
            index_end += 1
        variables_str = variables_str[:index_start] + str(value) + variables_str[index_end:]
    return variables_str


def update_save_file(file_path, keys_to_modify):
    logging.info(f"Updating save file: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        save_data = json.load(file)
    logging.info("Save file read successfully.")
    
    if 'variables' in save_data:
        save_data['variables'] = update_variables(save_data['variables'], keys_to_modify)
        logging.info("Variables updated.")

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(save_data, file, indent=4, ensure_ascii=False)
    logging.info("Save file has been updated.")




def find_latest_active_save_file(SAVE_FILE_DIR):
    logging.info("Searching for the latest 'Active_' prefixed save file.")
    json_files = list(SAVE_FILE_DIR.glob("Active_*.json"))
    if not json_files:
        logging.warning("No 'Active_' prefixed JSON files found.")
        return None
    latest_file = max(json_files, key=lambda x: datetime.strptime(x.stem, 'Active_%d-%m-%Y_%H-%M-%S'), default=None)
    logging.info(f"The latest 'Active_' prefixed save file found: {latest_file}")
    return latest_file

def main():

    latest_save_file = find_latest_active_save_file(SAVE_FILE_DIR)

    if latest_save_file:
        logging.info(f"Latest 'Active_' save file to update: {latest_save_file.name}")
        update_save_file(latest_save_file, KEYS_TO_MODIFY)

    else:
        logging.error("No 'Active_' save file found to update.")

if __name__ == "__main__":
    main()
