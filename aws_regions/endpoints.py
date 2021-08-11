# Copyright (c) 2021 SUSE LLC
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import requests

from functools import lru_cache

endpoints_url = (
    'https://raw.githubusercontent.com/boto/botocore/'
    'develop/botocore/data/endpoints.json'
)
partition_names = ('aws', 'aws-cn', 'aws-us-gov')


@lru_cache
def get_endpoints():
    return requests.get(endpoints_url).json()


def get_partition_data(partition: str):
    endpoints = get_endpoints()

    for partition_data in endpoints['partitions']:
        if partition_data['partition'] == partition:
            return partition_data


def get_regions(partition: str = 'aws'):
    partition_data = get_partition_data(partition)
    return list(partition_data['regions'].keys())


def get_all_regions():
    regions = []

    for name in partition_names:
        regions += get_regions(name)

    return regions
