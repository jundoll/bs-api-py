# load modules
from dataclasses import dataclass


# definition class
@dataclass(frozen=True)
class PlayerStatsHistory:

    id: int
    pp: str
    rank: str
    countryRank: str
    totalScore: str
    averageRankedAccuracy: str
    topAccuracy: str
    topPp: str
    averageAccuracy: str
    medianAccuracy: str
    medianRankedAccuracy: str
    totalPlayCount: str
    rankedPlayCount: str
    replaysWatched: str


# definition function
def gen(response):

    if response is not None:
        instance = PlayerStatsHistory(
            id=response.get('id'),
            pp=response.get('pp'),
            rank=response.get('rank'),
            countryRank=response.get('countryRank'),
            totalScore=response.get('totalScore'),
            averageRankedAccuracy=response.get('averageRankedAccuracy'),
            topAccuracy=response.get('topAccuracy'),
            topPp=response.get('topPp'),
            averageAccuracy=response.get('averageAccuracy'),
            medianAccuracy=response.get('medianAccuracy'),
            medianRankedAccuracy=response.get('medianRankedAccuracy'),
            totalPlayCount=response.get('totalPlayCount'),
            rankedPlayCount=response.get('rankedPlayCount'),
            replaysWatched=response.get('replaysWatched')
        )
        return instance


def genList(response):

    if response is None:
        return None
    else:
        if type(response) is list:
            if len(response) == 0:
                return []
            else:
                return [gen(v) for v in response]
        elif type(response) is dict:
            return [gen(response)]
