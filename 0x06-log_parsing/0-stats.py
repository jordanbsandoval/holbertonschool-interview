#!/usr/bin/python3
"""0x06. Log Parsing"""
from sys import stdin


total_size = 0
stats = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
         '404': 0, '405': 0, '500': 0}


def print_stats():
    """A script that reads stdin line by line and computes metrics"""
    print("File size: {}".format(total_size))
    for key, value in sorted(stats.items()):
        if value > 0:
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    line_counter = 0
    try:
        for line in stdin:
            args = line.split()
            line_counter += 1
            if len(args) > 2:
                total_size += int(args[-1])
                if args[-2] in stats:
                    stats.update({str(args[-2]): stats.get(args[-2]) + 1})
            if line_counter == 10:
                print_stats()
                line_counter = 0
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()

