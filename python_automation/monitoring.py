import os
import time
import json

STATE_FILE = "state.json"
LOG_FILE = "log.txt"

def monitor_directory(target_dir):
    if not os.path.isdir(target_dir):
        print(f"Directory {target_dir} does not exist.")
        return

    # Load previous state to compare against
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r') as f:
            previous_state = json.load(f)
    else:
        previous_state = {}

    current_state = {}
    new_files = []

    # Scan the target directory
    for filename in os.listdir(target_dir):
        filepath = os.path.join(target_dir, filename)
        if os.path.isfile(filepath):
            # Get file statistics
            stats = os.stat(filepath)
            size_kb = stats.st_size / 1024
            timestamp = stats.st_mtime
            current_state[filename] = timestamp

            # Identify if it is a new file
            if filename not in previous_state:
                readable_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))
                new_files.append(f"{filename} | {size_kb:.2f} KB | {readable_time}")

    # Output findings to console and log.txt
    if new_files:
        with open(LOG_FILE, 'a') as f:
            for file_info in new_files:
                f.write(f"NEW FILE: {file_info}\n")
                print(f"NEW FILE: {file_info}")
    else:
        print("No new files detected.")

    # Save the current state for the next run
    with open(STATE_FILE, 'w') as f:
        json.dump(current_state, f)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Monitor a directory for new files.")
    parser.add_argument(
        "-d", "--directory",
        type=str,
        default=".",
        help="Directory to monitor (default: current directory)"
    )
    args = parser.parse_args()
    monitor_directory(args.directory)