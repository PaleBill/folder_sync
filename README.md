# File Replication Script

This script replicates the contents of one directory (`<path_src>`) to another (`<path_des>`), ensuring that the destination directory mirrors the source. It periodically copies new files, updates existing ones, and removes files or folders from the destination that no longer exist in the source. All operations are logged in a specified log file.

## Usage

You can run the script from the command line by passing the source and destination directories, the path for the log file, and the time interval between runs.

### Command-line Parameters

- `<path_src>`: The source directory that contains the files to be replicated.
- `<path_des>`: The destination directory where the files will be copied.
- `<log_file_path>`: The full path to the log file where operations will be logged.
- `<interval>`: The time interval in seconds for periodically running the replication process.

### Example Command

```bash
python script_name.py <path_src> <path_des> <log_file_path> <interval_in_seconds>
```

### Log Files
## All operations are logged with timestamps:

- Creation of new files and directories.
- Updates to existing files.
- Removal of files or directories from the destination if they are absent in the source.
