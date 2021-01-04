"""
Tests for access_log
"""

import unittest

import access_log

import pandas as pd
import numpy as np
from pandas.testing import assert_series_equal


class AccessLogTest(unittest.TestCase):

  def test_get_top_10_clients_by_bytes_correctly_groups_and_sums(self):
    sample = pd.DataFrame({
        'client_ip': ['a', 'b', 'a', 'a'],
        'bytes': [1, 2, 3, 4]
    })

    expected = pd.Series([8, 2],
                         name='bytes',
                         dtype=np.int64,
                         index=pd.Index(['a', 'b'], name='client_ip'))

    actual = access_log.get_top_10_clients_by_bytes(sample)

    assert_series_equal(expected, actual)
