"""
Demonstrates loading a large tabular dataset into a Pandas dataframe
"""

import pandas as pd
import access_log

import memory_profiler


@memory_profiler.profile
def main(access_log_path):
  with open(access_log_path) as log:
    hits = pd.read_csv(log,
                       sep=access_log.SEPARATOR,
                       header=None,
                       names=access_log.COLUMN_NAMES)

    return access_log.get_top_10_clients_by_bytes(hits)


if __name__ == '__main__':
  print(main(access_log.ACCESS_LOG_PATH))
