# load modules
from dataclasses import dataclass


# definition class
@dataclass(frozen=True)
class ScoreStats:

    totalScore: float
    totalRankedScore: float
    averageRankedAccuracy: float
    totalPlayCount: float
    rankedPlayCount: float
    replaysWatched: float


# definition function
def gen(response):

    if response is not None:
        instance = ScoreStats(
            totalScore=response.get('totalScore'),
            totalRankedScore=response.get('totalRankedScore'),
            averageRankedAccuracy=response.get('averageRankedAccuracy'),
            totalPlayCount=response.get('totalPlayCount'),
            rankedPlayCount=response.get('rankedPlayCount'),
            replaysWatched=response.get('replaysWatched')
        )
        return instance


def gen_list(response):

    if response is not None:
        if len(response) == 0:
            return []
        else:
            return [gen(v) for v in response]
