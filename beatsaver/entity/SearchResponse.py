# load modules
from dataclasses import dataclass
from typing import List, Union

from ...beatsaver.entity import MapDetail


# definition class
@dataclass(frozen=True)
class SearchResponse:

    docs: Union[List[MapDetail.MapDetail], List, None]
    redirect: str


# definition function
def gen(response):

    if response is not None:
        instance = SearchResponse(
            docs=MapDetail.gen_list(response.get('docs')),
            redirect=response.get('redirect')
        )
        return instance


def gen_list(response):

    if response is not None:
        if len(response) == 0:
            return []
        else:
            return [gen(v) for v in response]
