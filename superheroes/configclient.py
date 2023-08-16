import os
from typing import Dict

from spring_config import ClientConfigurationBuilder
from spring_config.client import SpringConfigClient


def __flatten_map__(d, flatten=None, chain=None):
    if flatten is None:
        flatten = {}
    for k, v in d.items():
        key = f'{chain}.{k}' if chain else k
        if isinstance(v, dict):
            __flatten_map__(d=v, flatten=flatten, chain=key)
        else:
            flatten[key] = v
    return flatten


def __resolve_mapping__(c: Dict[str, object]):
    for k, v in c.copy().items():
        if isinstance(v, str):
            start_index = v.find('${', 0)
            while start_index > 0:
                end_index = v.find('}')
                part = v[start_index + 2:end_index]
                resolve = c[part]
                v = v.replace('${' + part + '}', resolve)
                start_index = v.find('${')
            c[k] = v
    return c


__config = (ClientConfigurationBuilder()
            .app_name(os.environ['SPRING_APPLICATION_NAME'])
            .address(os.environ['SPRING_CONFIG_URL'])
            .branch(os.environ['SPRING_CONFIG_LABEL'].replace('/', '(_)'))
            .profile(os.environ['SPRING_PROFILES_ACTIVE'])
            .authentication((os.environ['SPRING_CONFIG_USERNAME'], os.environ['SPRING_CONFIG_PASSWORD']))
            .build())

__c = SpringConfigClient(__config)
configs = __c.get_config()
configs = __flatten_map__(configs)
configs = __resolve_mapping__(configs)
