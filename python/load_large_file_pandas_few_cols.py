"""
Demonstrates loading explicit columns from a large tabular dataset into a Pandas dataframe
"""

import pandas as pd
import access_log

def main(access_log_path):
  with open(access_log_path) as log:
    hits = pd.read_csv(log,
                      sep=access_log.SEPARATOR,
                      header=None,
                      names=access_log.COLUMN_NAMES,
                      usecols=['client_ip', 'bytes'])

    return access_log.get_top_10_clients_by_bytes(hits)


if __name__ == '__main__':
  print(main('/home/paul/Downloads/access.log'))
