"""
Demonstrates loading and calculating over a large tabular dataset without pandas
"""

from operator import itemgetter

import csv

import access_log


def main(access_log_path):
  with open(access_log_path) as log:
    log_parser = csv.reader(log, delimiter=' ')

    clients = {}
    for row in log_parser:
      client_ip = row[access_log.COLUMN_NAMES.index('client_ip')]
      client_bytes = int(row[access_log.COLUMN_NAMES.index('bytes')])

      updated_total_bytes_for_client = clients.setdefault(client_ip,
                                                          0) + client_bytes
      clients[client_ip] = updated_total_bytes_for_client

    top_10 = sorted(clients.items(), key=itemgetter(1), reverse=True)[0:10]

    return top_10


if __name__ == '__main__':
  print(main(access_log.ACCESS_LOG_PATH))
