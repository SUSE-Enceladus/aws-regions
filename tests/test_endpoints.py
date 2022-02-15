import vcr

from aws_regions.endpoints import get_all_regions


def scrub_headers():
    def before_record_response(response):
        new_headers = {
            'Content-Encoding': response['headers']['Content-Encoding'],
            'Content-Length': response['headers']['Content-Length'],
            'Content-Type': response['headers']['Content-Type']
        }
        response['headers'] = new_headers
        return response
    return before_record_response


@vcr.use_cassette(
    'tests/cassettes/get_all_regions.yml',
    before_record_response=scrub_headers()
)
def test_get_all_regions():
    expected_regions = [
        'af-south-1',
        'ap-east-1',
        'ap-northeast-1', 'ap-northeast-2', 'ap-northeast-3',
        'ap-south-1',
        'ap-southeast-1', 'ap-southeast-2',
        'ca-central-1',
        'eu-central-1',
        'eu-north-1',
        'eu-south-1',
        'eu-west-1', 'eu-west-2', 'eu-west-3',
        'me-south-1',
        'sa-east-1',
        'us-east-1', 'us-east-2',
        'us-west-1', 'us-west-2',
        'zu-west-1',
        'cn-north-1',
        'cn-northwest-1',
        'us-gov-east-1',
        'us-gov-west-1'
    ]

    regions = get_all_regions(config_file='tests/data/test.config')
    assert regions == expected_regions


@vcr.use_cassette(
    'tests/cassettes/get_all_regions.yml',
    before_record_response=scrub_headers()
)
def test_get_all_regions_no_config():
    expected_regions = [
        'af-south-1',
        'ap-east-1',
        'ap-northeast-1', 'ap-northeast-2', 'ap-northeast-3',
        'ap-south-1',
        'ap-southeast-1', 'ap-southeast-2',
        'ca-central-1',
        'eu-central-1',
        'eu-north-1',
        'eu-south-1',
        'eu-west-1', 'eu-west-2', 'eu-west-3',
        'me-south-1',
        'sa-east-1',
        'us-east-1', 'us-east-2',
        'us-west-1', 'us-west-2',
        'cn-north-1',
        'cn-northwest-1',
        'us-gov-east-1',
        'us-gov-west-1'
    ]

    regions = get_all_regions(config_file='tests/data/no.config')
    assert regions == expected_regions
