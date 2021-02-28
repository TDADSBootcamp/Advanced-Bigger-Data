"""
    Parsing and processing the access logs
    from https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/3QBYB5
"""

import os

COLUMN_NAMES = [
    'client_ip', 'identity', 'username', 'timestamp', 'timezone', 'request',
    'status', 'bytes', 'ref', 'user-agent', 'unknown'
]

SEPARATOR = ' '

ACCESS_LOG_PATH = os.environ.get('ACCESS_LOG_PATH') or 'uncommitted/access.log'
COMPRESSED_ACCESS_LOG_PATH = os.environ.get('COMPRESSED_ACCESS_LOG_PATH') or 'uncommitted/access.log.zip'


def get_top_10_clients_by_bytes(access_log_df):
  by_ip_address = access_log_df.groupby('client_ip')

  client_total_bytes = by_ip_address['bytes'].sum()

  top_10_clients_by_bytes = client_total_bytes.sort_values(
      ascending=False).head(10)

  return top_10_clients_by_bytes
