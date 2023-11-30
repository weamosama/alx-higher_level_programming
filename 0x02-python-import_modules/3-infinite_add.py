#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    args = argv[1:]  # Exclude the script name from the arguments
    result = 0

    for arg in args:
        result += int(arg)

    print(result)
