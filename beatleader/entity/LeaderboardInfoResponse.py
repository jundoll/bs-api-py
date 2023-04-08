
# load modules
from dataclasses import dataclass
from typing import Union

from . import (DifficultyDescription, RankQualification, RankUpdate,
               ScoreResponseWithAcc, Song)


# definition class
@dataclass(frozen=True)
class LeaderboardInfoResponse:
    id: str
    song: Union[Song.Song, None]
    difficulty: Union[DifficultyDescription.DifficultyDescription, None]
    plays: int
    positiveVotes: int
    starVotes: int
    negativeVotes: int
    voteStars: float
    myScore: Union[ScoreResponseWithAcc.ScoreResponseWithAcc, None]
    qualitfication: Union[RankQualification.RankQualification, None]
    reweight: Union[RankUpdate.RankUpdate, None]


# definition function
def gen(response):
    instance = LeaderboardInfoResponse(
        id=response.get('id'),
        song=Song.gen(response.get('song')),
        difficulty=DifficultyDescription.gen(response.get('difficulty')),
        plays=response.get('plays'),
        positiveVotes=response.get('positiveVotes'),
        starVotes=response.get('starVotes'),
        negativeVotes=response.get('negativeVotes'),
        voteStars=response.get('voteStars'),
        myScore=None,  # ScoreResponseWithAcc.gen(response.get('myScore')),
        qualitfication=None,  # RankQualification.gen(response.get('qualitfication')),
        reweight=None  # RankUpdate.gen(response.get('reweight'))
    )
    return instance


def gen_list(response):
    if response is not None:
        if len(response) == 0:
            return []
        else:
            return [gen(v) for v in response]
