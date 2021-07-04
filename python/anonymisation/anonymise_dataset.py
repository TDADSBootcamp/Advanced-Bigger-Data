'''
Reads line from an access log file and writes a new file
with potentially sensitive fields either masked or replaced with randomly generated values

To preserve the distribution of client IP addresses (col 0) but remove the identifiability,
they are replaced with randomly generated IP addresses,
where the same client IP produces the same generated address every time it occurs.

Bot user-agents are not personally identifiable, so are unmodified.
To keep the decompressed file roughly the same length,
other user agents are replaced with strings of mask characters of the same length
'''

import csv
from functools import lru_cache
import random
from typing import List

import access_log

@lru_cache(maxsize=None)
def random_caching_ip(original_ip: str) -> str: # pylint: disable=unused-argument
  '''
  Returns randomly generated IPs, but always returns the same random IP for a given original_ip

  >>> import re
  >>> bool(re.match(r'^(?:[0-9]{1,3}\\.){3}[0-9]{1,3}$', random_caching_ip('4.3.2.1')))
  True

  >>> ip = '1.2.3.4'
  >>> random_caching_ip(ip) == random_caching_ip(ip)
  True
  '''
  return '.'.join([str(random.randrange(0, 255)) for _ in range(4)])

def masked_user_agent_same_length(val: str) -> str:
  return 'x' * len(val)

def mask_value(replacement: str = None) -> str:
  '''
  >>> mask_value()
  'masked'

  >>> mask_value('foo')
  'masked:foo'
  '''
  return f'masked{":" + replacement if replacement else ""}'

def anonymise_column_value(col_name: str, value: str) -> str:
  '''
  >>> import re
  >>> ip = '123.456.789.0'
  >>> ip == anonymise_column_value('client_ip', ip)
  False

  >>> user_agent = 'my_user_agent'
  >>> user_agent == anonymise_column_value('user-agent', user_agent)
  False

  >>> len(user_agent) + len('masked:') == len(anonymise_column_value('user-agent', user_agent))
  True

  >>> anonymise_column_value('user-agent', 'Mozilla/5.0 (compatible; AhrefsBot/6.1; +http://ahrefs.com/robot/)')
  'Mozilla/5.0 (compatible; AhrefsBot/6.1; +http://ahrefs.com/robot/)'

  >>> anonymise_column_value('username', 'me')
  'masked'

  >>> identity = 'me'
  >>> anonymise_column_value('identity', 'me')
  'masked'

  >>> anonymise_column_value('Identity', 'me')
  'masked'

  >>> anonymise_column_value(' identity', 'me')
  'masked'

  >>> anonymise_column_value('ref', 'foo')
  'masked'
  '''

  clean_col_name = col_name.lower().strip()
  if clean_col_name == 'client_ip':
    return mask_value(random_caching_ip(value))
  if clean_col_name == 'user-agent':
    return value if 'bot' in value.lower() else mask_value(masked_user_agent_same_length(value))
  if clean_col_name in {'identity', 'username', 'ref'}:
    return mask_value()
  else:
    return value


def anonymise_row(col_values: List[str]) -> List[str]:
  '''
  >>> col_values = ['3.6.5.4','-','-','[22/Jan/2019:03:56:14','+0330]','GET /filter HTTP/1.1','200','30577','-','Mozilla/5.0 (compatible; AhrefsBot/6.1; +http://ahrefs.com/robot/)','-'] # pylint: disable=line-too-long
  >>> anonymised = anonymise_line(col_values)
  >>> anonymised[0][0:6]
  'masked'

  >>> '3.6.5.4' in anonymised[0]
  False

  >>> anonymised[1:] == ['masked' ,'masked', '[22/Jan/2019:03:56:14', '+0330]', 'GET /filter HTTP/1.1', '200', '30577', 'masked', 'Mozilla/5.0 (compatible; AhrefsBot/6.1; +http://ahrefs.com/robot/)', '-']
  True
  '''

  return [anonymise_column_value(col, value) for col, value in zip(access_log.COLUMN_NAMES, col_values)]

def main():
  with open('uncommitted/access.log', newline='') as original_log, open('uncommitted/access_masked.log', 'w') as masked_log:
    log_reader = csv.reader(original_log, delimiter=' ')
    log_writer = csv.writer(masked_log, delimiter=' ')
    for row in log_reader:
      log_writer.writerow(anonymise_row(row))

if __name__ == '__main__':
  main()
