#!/usr/bin/python3
'''interview of elements in an list'''
import re
import signal
import sys


def print_info(info, size):
    codes = list(info.keys())
    codes.sort()
    print("File size: {}".format(size))
    for code in codes:
        print("{}: {}".format(code, info[code]))


def signal_handler(sig, frame):
    pass


def main():
    valid_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    regex = {
        "ip":
            r"((?:(?:25[0-5]|2[0-4]\d|1?\d?\d)\.){3}"
            "(?:25[0-5]|2[0-4]\d|1?\d?\d)|\w+)",

        "date": r"(20\d{2}-[01]?\d-(?:3[01]|[0-2]\d))",

        "time": "([0-5]\d:[0-5]\d:[0-5]\d\.\d+)",

        "code": "(\w+)",

        "size": "(\d+)",

        "path": "/projects/260"
    }

    pattern = \
        '^{ip} ?- ?\[{date} {time}\] "GET {path} HTTP/1.1" {code} {size}$'
    pattern = pattern.format(**regex)

    line_counter = 0
    code_counter = {}
    sizes = 0
    signal.signal(signal.SIGINT, signal_handler)
    for line in sys.stdin:
        out = re.match(pattern, line)
        if out:
            line_counter += 1
            sizes += int(out.group(5))
            code = out.group(4)
            if code in map(str, valid_codes):
                if code not in code_counter.keys():
                    code_counter[code] = 1
                else:
                    code_counter[code] += 1
            if line_counter % 10 == 0:
                print_info(code_counter, sizes)
    if line_counter == 0 or line_counter % 10 != 0:
        print_info(code_counter, sizes)


if __name__ == "__main__":
    main()
