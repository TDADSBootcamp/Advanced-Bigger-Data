"""
Lookup billing information for each client based on hour of day
using an unoptimised lookup function

One scan of the (small) billing dataframe per row - 10,365,152 scans
"""

import pandas as pd
import access_log


def timestamp_to_hour(timestamp):
  return int(timestamp.split(':')[1])


def lookup_multiplier(lookup, hour):
  return lookup.loc[hour]['multiplier']

def main(access_log_path):
  with open('billing.csv') as billing_data:
    billing_lookup = pd.read_csv(billing_data, index_col='hour') # we index by the hour

  with open(access_log_path) as log:
    hits = pd.read_csv(log,
                       sep=access_log.SEPARATOR,
                       header=None,
                       names=access_log.COLUMN_NAMES,
                       usecols=['client_ip', 'timestamp', 'bytes'])

    hits['bytes_billed'] = hits['bytes'] * hits['timestamp'] \
      .apply(lambda timestamp: lookup_multiplier(billing_lookup, timestamp_to_hour(timestamp)))

    return access_log.get_top_10_clients_by_bytes(hits,
                                                  bytes_col='bytes_billed')


if __name__ == '__main__':
  print(main(access_log.ACCESS_LOG_PATH))
