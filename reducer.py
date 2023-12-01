#!/usr/bin/env python3

import sys


player_strike_rates = {}


for line in sys.stdin:
    try:
        name, strike_rate = line.strip().split(',')
        strike_rate = float(strike_rate)

        
        if name in player_strike_rates:
            player_strike_rates[name].append(strike_rate)
        else:
            player_strike_rates[name] = [strike_rate]

    except ValueError:
        
        pass


for name, strike_rates in player_strike_rates.items():
    if len(strike_rates) > 0:
        aggregate_strike_rate = sum(strike_rates)/len(strike_rates)

        
        #print(f'{{"name": "{name}", "strike_rate": {aggregate_strike_rate:.3f}}}')
        print("{"+"\"name\": \"{}\", \"strike_rate\": {}".format(name,round(aggregate_strike_rate,3))+"}")


