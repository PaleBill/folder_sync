import sys
import os
import shutil
from datetime import datetime
import time

def log(string):
    """
    Logs the provided message to both the console and a log file with a timestamp.

    Args:
        string (str): The message to be logged.

    This function prints the log message to the console and writes it to a specified log file.
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = f"[{timestamp}] - {string}"

    print(log_message)

    with open(LOG_FILE_PATH, 'a') as log_file:
        log_file.write(log_message + '\n')


def copy(path_src, path_des):
    """
    Copies a file from the source path to the destination path.

    Args:
        path_src (str): The full path of the source file to be copied.
        path_des (str): The full path of the destination file.

    This function logs the file replication and handles any exceptions during the copying process.
    """
    try:
        log(f"File replicated: {path_src} -> {path_des}")
        shutil.copy(path_src, path_des)
    except Exception as e:
        log(e)


def remove_files_and_folders(path_src, path_des):
    """
    Removes files and directories in the destination that do not exist in the source.

    Args:
        path_src (str): The path to the source directory.
        path_des (str): The path to the destination directory.

    This function scans through the destination directory, compares it to the source directory,
    and removes files and folders from the destination if they don't exist in the source.
    """
    for folderName, subfolders, filenames in os.walk(path_des, topdown=False):
        relative_path = os.path.relpath(folderName, path_des)
        corresponding_src_folder = os.path.join(path_src, relative_path)

        # Remove files in the destination that don't exist in the source
        for filename in filenames:
            dest_file = os.path.join(folderName, filename)
            src_file = os.path.join(corresponding_src_folder, filename)
            if not os.path.exists(src_file):
                os.remove(dest_file)
                log(f"Removed file: {dest_file}")

        # Remove folders in the destination that don't exist in the source
        if not os.path.exists(corresponding_src_folder):
            shutil.rmtree(folderName)
            log(f"Removed folder: {folderName}")


def copy_files_and_folders(path_src, path_des):
    """
    Recursively copies files from the source directory to the destination directory,
    ensuring that the directory structure is maintained.

    Args:
        path_src (str): The path to the source directory.
        path_des (str): The path to the destination directory.

    This function walks through the source directory, creates corresponding directories in the
    destination, and copies files. It logs the creation of new folders and files.
    """
    for folderName, subfolders, filenames in os.walk(path_src):
        relative_path = os.path.relpath(folderName, path_src)
        target_folder = os.path.join(path_des, relative_path)

        # Create the folder in the destination if it doesn't exist
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
            log(f"Created folder: {target_folder}")

        # Copy each file to the corresponding destination folder
        for filename in filenames:
            src_file = os.path.join(folderName, filename)
            dest_file = os.path.join(target_folder, filename)
            
            if not os.path.exists(dest_file):
                log(f"Creating new file: {dest_file}")
            
            copy(src_file, dest_file)


if __name__ == "__main__":
    """
    Main function that takes command-line arguments and sets the interval for periodic execution.

    Usage:
        python script_name.py <path_src> <path_des> <log_file_path> <interval>

    Args:
        <path_src> (str): The path to the source directory.
        <path_des> (str): The path to the destination directory.
        <log_file_path> (str): The full path to the log file where logs will be written.
        <interval> (int): The time interval (in seconds) at which the script should run.
    """
    if len(sys.argv) != 5:
        print("Usage: python script_name.py <path_src> <path_des> <log_file_path> <interval>")
        sys.exit(1)

    # Parse the command-line arguments
    path_src = sys.argv[1]  
    path_des = sys.argv[2]  
    LOG_FILE_PATH = sys.argv[3]
    interval = int(sys.argv[4])  

    # Run the script periodically with the specified interval
    while True:
        copy_files_and_folders(path_src, path_des)
        remove_files_and_folders(path_src, path_des)
        time.sleep(interval)
