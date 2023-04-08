
# load modules
from dataclasses import dataclass
from typing import List, Union

from . import LeaderboardInfoResponse, Metadata


# definition class
@dataclass(frozen=True)
class LeaderboardInfoResponseResponseWithMetadata:
    metadata: Union[Metadata.Metadata, None]
    data: Union[List[LeaderboardInfoResponse.LeaderboardInfoResponse], List, None]


# definition function
def gen(response):
    instance = LeaderboardInfoResponseResponseWithMetadata(
        metadata=Metadata.gen(response.get('scoreStats')),
        data=LeaderboardInfoResponse.gen_list(
            response.get('badges'))
    )
    return instance


def gen_list(response):
    if response is not None:
        if len(response) == 0:
            return []
        else:
            return [gen(v) for v in response]
