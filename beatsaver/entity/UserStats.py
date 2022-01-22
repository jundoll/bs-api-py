# load modules
from dataclasses import dataclass
from typing import Union

from ...beatsaver.entity import UserDiffStats


# definition class
@dataclass(frozen=True)
class UserStats:

    avgBpm: float
    avgDuration: float
    avgScore: float
    diffStats: Union[UserDiffStats.UserDiffStats, None]
    firstUpload: str
    lastUpload: str
    rankedMaps: int
    totalDownvotes: int
    totalMaps: int
    totalUpvotes: int


# definition function
def gen(response):

    if response is not None:
        instance = UserStats(
            avgBpm=response.get('avgBpm'),
            avgDuration=response.get('avgDuration'),
            avgScore=response.get('avgScore'),
            diffStats=UserDiffStats.gen(response.get('diffStats')),
            firstUpload=response.get('firstUpload'),
            lastUpload=response.get('lastUpload'),
            rankedMaps=response.get('rankedMaps'),
            totalDownvotes=response.get('totalDownvotes'),
            totalMaps=response.get('totalMaps'),
            totalUpvotes=response.get('totalUpvotes')
        )
        return instance


def gen_list(response):

    if response is not None:
        if len(response) == 0:
            return []
        else:
            return [gen(v) for v in response]
