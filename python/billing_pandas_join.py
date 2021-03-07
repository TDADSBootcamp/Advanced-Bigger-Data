"""
Lookup billing information for each client based on hour of day
using a reference dataframe indexed by hour

Far more efficient to look up values - runtime on the order of 25s
"""

import pandas as pd
import access_log


def timestamp_to_hour(timestamp):
  return int(timestamp.split(':')[1])


def main(access_log_path):
  with open('billing.csv') as billing_data:
    billing_lookup = pd.read_csv(billing_data, index_col='hour')

  with open(access_log_path) as log:
    hits = pd.read_csv(log,
                       sep=access_log.SEPARATOR,
                       header=None,
                       names=access_log.COLUMN_NAMES,
                       usecols=['client_ip', 'timestamp', 'bytes'])

    hits['hour'] = hits['timestamp'].map(timestamp_to_hour)
    hits_and_billing = hits.join(billing_lookup, on='hour')
    hits_and_billing['bytes_billed'] = hits_and_billing[
        'bytes'] * hits_and_billing['multiplier']

    return access_log.get_top_10_clients_by_bytes(hits_and_billing,
                                                  bytes_col='bytes_billed')


if __name__ == '__main__':
  print(main(access_log.ACCESS_LOG_PATH))
