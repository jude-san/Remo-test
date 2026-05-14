
# Monitoring Script

## How to Run the Script

This script monitors a specified directory for new files and logs any new files detected since the last run.

### Usage

Run the script from the command line:

```
python monitoring.py --directory /path/to/your/directory
```

- The `--directory` (or `-d`) argument is optional. If not provided, the script will monitor the current directory (`.`) by default.
- Example:
	- Monitor the current directory:
		```
		python monitoring.py
		```
	- Monitor a specific directory:
		```
		python monitoring.py --directory /home/user/Documents
		```
	- example:
		```
		python3 monitoring.py -d ~/Downloads
		```

### Output
- `log.txt`
- `state.json` file to track previously seen files and their modification times, this resembles something like a state mechanism.

## Assumptions
- The script assumes the specified directory exists and is accessible.
- Only regular files (not subdirectories) in the top level of the specified directory are monitored.
- The script should be run with Python 3.
- The script does not recursively scan subdirectories.
- The script expects to have write permissions in the directory where it is run (to create/update `log.txt` and `state.json`).