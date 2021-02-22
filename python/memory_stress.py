import time
import argparse

def eat_memory(gb):
    GB = 1024*1024*1024
    hog = "a" * (gb * GB)
    HOURS = 60 * 60
    time.sleep(1 * HOURS)

parser = argparse.ArgumentParser()
parser.add_argument('--gb', type=int, help='how many GB to consume')

args = parser.parse_args()
eat_memory(args.gb)
