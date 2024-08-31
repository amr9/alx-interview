#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
import sys


def print_stats(status_dict, file_size):
    """Prints the stats"""
    print("File size: {}".format(file_size))
    for key, value in sorted(status_dict.items()):
        if value != 0:
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    status_dict = {"200": 0, "301": 0, "400": 0, "401": 0,
                   "403": 0, "404": 0, "405": 0, "500": 0}
    file_size = 0
    counter = 0

    try:
        for line in sys.stdin:
            counter += 1
            data = line.split()
            try:
                file_size += int(data[-1])
            except Exception:
                pass
            try:
                if data[-2] in status_dict:
                    status_dict[data[-2]] += 1
            except Exception:
                pass
            if counter == 10:
                print_stats(status_dict, file_size)
                counter = 0
    except KeyboardInterrupt:
        print_stats(status_dict, file_size)
        raise
    print_stats(status_dict, file_size)
