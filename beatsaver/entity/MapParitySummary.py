# load modules
from dataclasses import dataclass


# definition class
@dataclass(frozen=True)
class MapParitySummary:

    errors: int
    resets: int
    warns: int


# definition function
def gen(response):

    if response is not None:
        instance = MapParitySummary(
            errors=response.get('errors'),
            resets=response.get('resets'),
            warns=response.get('warns')
        )
        return instance


def gen_list(response):

    if response is not None:
        if len(response) == 0:
            return []
        else:
            return [gen(v) for v in response]
