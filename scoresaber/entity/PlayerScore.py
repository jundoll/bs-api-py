# load modules
from dataclasses import dataclass
from typing import Union

import LeaderboardInfo, Score


# definition class
@dataclass(frozen=True)
class PlayerScore:

    score: Union[Score.Score, None]
    leaderboard:  Union[LeaderboardInfo.LeaderboardInfo, None]


# definition function
def gen(response):

    if response is not None:
        instance = PlayerScore(
            score=Score.gen(response.get('score')),
            leaderboard=LeaderboardInfo.gen(response.get('leaderboard'))
        )
        return instance


def gen_list(response):

    if response is not None:
        if len(response) == 0:
            return []
        else:
            return [gen(v) for v in response]
