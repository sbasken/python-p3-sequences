#!/usr/bin/env python3

def print_fibonacci(length):
    result = []
    for i in range(length):
        if len(result) == 0:
            result.append(0)
        elif len(result) == 1:
            result.append(1)
        elif len(result) >= 2:
            number = result[i-2] + result[i-1]
            result.append(number)
    print(result)
