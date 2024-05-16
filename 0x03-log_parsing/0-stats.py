#!/usr/bin/python3
"""
Log parsing script.
"""

import sys
import re
import signal


def output(log):
    """
    Helper function to display stats.
    """
    print("File size: {}".format(log["file_size"]))
    for code in sorted(log["code_frequency"]):
        if log["code_frequency"][code] > 0:
            print("{}: {}".format(code, log["code_frequency"][code]))


def signal_handler(sig, frame):
    """
    Handle keyboard interrupt signal (CTRL + C).
    """
    output(log)
    sys.exit(0)


if __name__ == "__main__":
    # Set up the signal handler for CTRL + C
    signal.signal(signal.SIGINT, signal_handler)

    regex = re.compile(
        r'(\d{1,3}\.){3}\d{1,3} - \[\d{4}-\d{2}-\d{2} '
        r'\d{2}:\d{2}:\d{2}\.\d+\] "GET /projects/260 HTTP/1\.1" '
        r'(\d{3}) (\d+)'
    )

    line_count = 0
    log = {
        "file_size": 0,
        "code_frequency": {
            "200": 0, "301": 0, "400": 0, "401": 0,
            "403": 0, "404": 0, "405": 0, "500": 0
        }
    }

    try:
        for line in sys.stdin:
            line = line.strip()
            match = regex.fullmatch(line)
            if match:
                line_count += 1
                code = match.group(2)
                file_size = int(match.group(3))

                # Update file size
                log["file_size"] += file_size

                # Update status code count
                if code in log["code_frequency"]:
                    log["code_frequency"][code] += 1

                if line_count % 10 == 0:
                    output(log)
    except KeyboardInterrupt:
        pass
    finally:
        output(log)
