# load modules
from dataclasses import dataclass
from typing import List, Union

from scoresaber.entity import LeaderboardInfo, Metadata


# definition class
@dataclass(frozen=True)
class LeaderboardInfoCollection:

    leaderboards: Union[List[LeaderboardInfo.LeaderboardInfo], List, None]
    metadata:  Union[Metadata.Metadata, None]


# definition function
def gen(response: dict):

    if response is not None:
        instance = LeaderboardInfoCollection(
            leaderboards=LeaderboardInfo.gen_list(
                response.get('leaderboards')),
            metadata=Metadata.gen(response.get('metadata'))
        )
        return instance


def gen_list(response):

    if response is not None:
        if len(response) == 0:
            return []
        else:
            return [gen(v) for v in response]
