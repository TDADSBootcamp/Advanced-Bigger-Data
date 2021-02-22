"""
Demonstrates loading a large tabular dataset with dask
distributing the compute over separate processes
"""

import dask.dataframe as dd

import access_log

import memory_profiler


@memory_profiler.profile
def main(access_log_path):
  hits = dd.read_csv(access_log_path,
                     sep=access_log.SEPARATOR,
                     header=None,
                     names=access_log.COLUMN_NAMES)

  hits = hits.compute(
      scheduler='processes')  # default is 'threads' - subject to GIL

  by_ip_address = hits.groupby('client_ip')

  client_total_bytes = by_ip_address['bytes'].sum()

  top_10_clients_by_bytes = client_total_bytes.nlargest(10)

  return top_10_clients_by_bytes.head(10)


if __name__ == '__main__':
  print(main(access_log.ACCESS_LOG_PATH))
