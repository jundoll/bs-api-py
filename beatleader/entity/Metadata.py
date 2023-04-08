
# load modules
from dataclasses import dataclass


# definition class
@dataclass(frozen=True)
class Metadata:
    itemsPerPage: int
    page: int
    total: int


# definition function
def gen(response):
    instance = Metadata(
        itemsPerPage=response.get('itemsPerPage'),
        page=response.get('page'),
        total=response.get('total')
    )
    return instance


def gen_list(response):
    if response is not None:
        if len(response) == 0:
            return []
        else:
            return [gen(v) for v in response]
