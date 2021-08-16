[![Continuous testing & Linting](https://github.com/SUSE-Enceladus/aws-regions/actions/workflows/ci.yml/badge.svg)](https://github.com/SUSE-Enceladus/aws-regions/actions/workflows/ci.yml)

Overview
========

This package provides a very simple API for retrieving the most up-to-date
region list. The region info is pulled from the botocore Github project so
this requires a network connection. The advantage to using botocore directly
is that the region list is not reliant on the botocore version which is
installed. This can be an issue if you are using system packages for example,
which may get updates very infrequently and thus may be missing new regions.


Requirements
============

- requests

Installation
============

```shell
pip install aws-regions
```

Usage
=====

There are two main functions in aws-regions. The first function will provide
a list of regions based on the AWS partition. By default this is this public
AWS partition:

```python
from aws_regions.endpoints import get_regions


# Defaults to "aws" partition
regions = get_regions()

# "aws-cn" partition
cn_region = get_regions(partition='aws-cn')
```

The second function will return a list of all regions from all three
partitions:

```python
from aws_regions.endpoints import get_all_regions

all_regions = get_all_regions()  # From aws, aws-cn and aws-us-gov
```

Issues/Enhancements
===================

Please submit issues and requests to
[Github](https://github.com/SUSE-Enceladus/aws-regions/issues).

Contributing
============

Contributions to **aws-regions** are welcome and encouraged. See
[CONTRIBUTING](https://github.com/SUSE-Enceladus/aws-regions/blob/master/CONTRIBUTING.md)
for info on getting started.

License
=======

Copyright (c) 2021 SUSE LLC.

Distributed under the terms of MIT license, see
[LICENSE](https://github.com/SUSE-Enceladus/aws-regions/blob/master/LICENSE)
for details.
