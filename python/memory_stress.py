"""
Consumes a fixed amount of memory for stress testing
"""

import time
import argparse

GB = 1024 * 1024 * 1024
HOURS = 60 * 60

def eat_memory(gb):
  hog = 'a' * (gb * GB) #pylint: disable=unused-variable
  time.sleep(1 * HOURS)


parser = argparse.ArgumentParser()
parser.add_argument('--gb', type=int, help='how many GB to consume')

args = parser.parse_args()
eat_memory(args.gb)
