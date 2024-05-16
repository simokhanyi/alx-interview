#!/usr/bin/python3
import sys
import signal

# Initialize variables
total_file_size = 0
status_code_counts = {
    200: 0, 301: 0, 400: 0, 401: 0,
    403: 0, 404: 0, 405: 0, 500: 0
}
line_count = 0


def print_stats():
    """Print the statistics collected so far."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


def signal_handler(sig, frame):
    """Handle keyboard interrupt signal (CTRL + C)."""
    print_stats()
    sys.exit(0)


# Set up the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        # Split and validate the line format
        parts = line.split()
        if len(parts) < 9:
            continue
        if (parts[5] != '"GET' or parts[6] != '/projects/260' or
                parts[7] != 'HTTP/1.1"'):
            continue

        # Extract status code and file size
        try:
            status_code = int(parts[8])
            file_size = int(parts[9])
        except (ValueError, IndexError):
            continue

        # Update total file size and status code count
        total_file_size += file_size
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        line_count += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Handle the case when the script is interrupted
    print_stats()
    sys.exit(0)
