# load modules
from dataclasses import dataclass
from typing import List, Union

import Badge, ScoreStats


# definition class
@dataclass(frozen=True)
class Player:

    id: str
    name: str
    profilePicture: str
    country: str
    pp: float
    rank: float
    countryRank: float
    role: str
    badges: Union[List[Badge.Badge], List, None]
    histories: str
    scoreStats: Union[ScoreStats.ScoreStats, None]
    permissions: float
    banned: bool
    inactive: bool


# definition function
def gen(response):

    if response is not None:
        instance = Player(
            id=response.get('id'),
            name=response.get('name'),
            profilePicture=response.get('profilePicture'),
            country=response.get('country'),
            pp=response.get('pp'),
            rank=response.get('rank'),
            countryRank=response.get('countryRank'),
            role=response.get('role'),
            badges=Badge.gen_list(response.get('badges')),
            histories=response.get('histories'),
            scoreStats=ScoreStats.gen(response.get('scoreStats')),
            permissions=response.get('permissions'),
            banned=response.get('banned'),
            inactive=response.get('inactive')
        )
        return instance


def gen_list(response):

    if response is not None:
        if len(response) == 0:
            return []
        else:
            return [gen(v) for v in response]
