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

import os
import requests

from aws_regions.config import Config
from functools import lru_cache

endpoints_url = (
    'https://raw.githubusercontent.com/boto/botocore/'
    'develop/botocore/data/endpoints.json'
)
partition_names = ('aws', 'aws-cn', 'aws-us-gov')
default_config_file = '~/.config/aws_regions.config'


def get_config(config_file: str = ''):
    config_file = os.path.expanduser(config_file or default_config_file)

    try:
        config = Config.load_from_file(config_file)
    except FileNotFoundError:
        config = Config()

    return config


@lru_cache(maxsize=128)
def get_endpoints():
    return requests.get(endpoints_url).json()


def get_partition_data(partition: str):
    endpoints = get_endpoints()

    for partition_data in endpoints['partitions']:
        if partition_data['partition'] == partition:
            return partition_data


def get_regions(partition: str = 'aws', config_file: str = ''):
    partition_data = get_partition_data(partition)
    additional_regions = get_config(config_file).get_custom_regions(partition)
    return list(partition_data['regions'].keys()) + additional_regions


def get_all_regions(config_file: str = ''):
    regions = []

    for name in partition_names:
        regions += get_regions(name, config_file=config_file)

    return regions
