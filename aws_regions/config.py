import dataclasses
import yaml

from dataclasses import dataclass, field


@dataclass
class Config:
    regions_aws: list = field(default_factory=list)
    regions_aws_cn: list = field(default_factory=list)
    regions_aws_us_gov: list = field(default_factory=list)

    @classmethod
    def load_from_file(cls, filename):
        with open(filename, 'r') as fh:
            yaml_data = yaml.safe_load(fh)

        attrs = {}
        fields = {}

        for f in dataclasses.fields(cls):
            fields[f.name] = f.type

        for section in yaml_data.keys():
            for k, v in yaml_data[section].items():
                attr = f"{section}_{k}"
                attr_type = fields.get(attr, None)
                if attr_type:
                    attrs[attr] = attr_type(v)

        return cls(**attrs)

    def get_custom_regions(self, partition):
        return getattr(self, f'regions_{partition.replace("-", "_")}')
