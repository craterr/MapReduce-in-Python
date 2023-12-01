#!/usr/bin/env python3

import json
import sys


def calculate_strike_rate(runs, balls):
    if balls == 0:
        return 0.000  
    return round((runs / balls) * 100, 3)

for line in sys.stdin:
    if '[\n' == line:
        continue
    elif ']\n' == line:
        break
    else:
        ele_json = json.loads(line.split(',\n')[0].strip())
        name = ele_json["name"]
        runs = int(ele_json["runs"])
        balls = int(ele_json["balls"])
        strike_rate = calculate_strike_rate(runs, balls)
        print(f"{name},{strike_rate}")
