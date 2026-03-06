import os
from aws_regions.config import Config


def test_defaults():
    config = Config()
    assert config.regions_aws == []
    assert config.regions_aws_cn == []
    assert config.regions_aws_us_gov == []
    assert config.regions_aws_eusc == []
    assert config.ignored_regions_aws == []
    assert config.ignored_regions_aws_cn == []
    assert config.ignored_regions_aws_us_gov == []
    assert config.ignored_regions_aws_eusc == []


def test_load_from_file():
    config_file = os.path.join(
        os.path.dirname(__file__),
        'data',
        'test.config'
    )
    config = Config.load_from_file(config_file)
    assert config.regions_aws == ['zu-west-1']
    assert config.ignored_regions_aws == [
        'me-central-1',
        'me-south-1'
    ]


def test_get_custom_regions():
    config = Config(
        regions_aws=['custom-1'],
        regions_aws_cn=['custom-2']
    )
    assert config.get_custom_regions('aws') == ['custom-1']
    assert config.get_custom_regions('aws-cn') == ['custom-2']
    assert config.get_custom_regions('aws-us-gov') == []


def test_get_custom_ignored_regions():
    config = Config(
        ignored_regions_aws=['ignored-1'],
        ignored_regions_aws_cn=['ignored-2']
    )
    assert config.get_custom_ignored_regions('aws') == ['ignored-1']
    assert config.get_custom_ignored_regions('aws-cn') == ['ignored-2']
    assert config.get_custom_ignored_regions('aws-us-gov') == []
