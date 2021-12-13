# load modules
from dataclasses import dataclass
from typing import Union


# definition class
@dataclass(frozen=True)
class Metadata:

    total: Union[float, None]
    page: Union[float, None]
    itemsPerPage: Union[float, None]


# definition function
def gen(response):

    if response is not None:
        instance = Metadata(
            total=response.get('total'),
            page=response.get('page'),
            itemsPerPage=response.get('itemsPerPage')
        )
        return instance


def gen_list(response):

    if response is not None:
        if len(response) == 0:
            return []
        else:
            return [gen(v) for v in response]
