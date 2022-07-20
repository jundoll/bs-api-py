# load modules
from dataclasses import dataclass


# definition class
@dataclass(frozen=True)
class PlayerScoreStats:

    averageRankedAccuracy: float
    averageAccuracy: float
    medianRankedAccuracy: float
    medianAccuracy: float
    topAccuracy: float
    topPp: float
    totalPlayCount: int
    rankedPlayCount: int
    replaysWatched: int
    averageRank: float
    averageRankedRank: float
    sSPPlays: int
    sSPlays: int
    sPPlays: int
    sPlays: int
    aPlays: int
    topPlatform: str
    topHMD: int
    dailyImprovements: int


# definition function
def gen(response):

    if response is not None:
        instance = PlayerScoreStats(
            averageRankedAccuracy=response.get('averageRankedAccuracy'),
            averageAccuracy=response.get('averageAccuracy'),
            medianRankedAccuracy=response.get('medianRankedAccuracy'),
            medianAccuracy=response.get('medianAccuracy'),
            topAccuracy=response.get('topAccuracy'),
            topPp=response.get('topPp'),
            totalPlayCount=response.get('totalPlayCount'),
            rankedPlayCount=response.get('rankedPlayCount'),
            replaysWatched=response.get('replaysWatched'),
            averageRank=response.get('averageRank'),
            averageRankedRank=response.get('averageRankedRank'),
            sSPPlays=response.get('sSPPlays'),
            sSPlays=response.get('sSPlays'),
            sPPlays=response.get('sPPlays'),
            sPlays=response.get('sPlays'),
            aPlays=response.get('aPlays'),
            topPlatform=response.get('topPlatform'),
            topHMD=response.get('topHMD'),
            dailyImprovements=response.get('dailyImprovements')
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
