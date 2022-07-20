# load modules
from dataclasses import dataclass
from typing import List, Union

from ..entity import (Badge, Clan, PatreonFeatures, PlayerFriends,
                                  PlayerScoreStats, PlayerStatsHistory)


# definition class
@dataclass(frozen=True)
class Player:

    id: str
    name: str
    platform: str
    avatar: str
    country: str
    histories: str
    role: str
    pp: float
    rank: int
    countryRank: int
    banned: bool
    inactive: bool
    externalProfileUrl: str
    lastTwoWeeksTime: float
    allTime: float
    scoreStats: Union[PlayerScoreStats.PlayerScoreStats, None]
    statsHistory: Union[PlayerStatsHistory.PlayerStatsHistory, None]
    clans: Union[List[Clan.Clan], List, None]
    friends: Union[List[PlayerFriends.PlayerFriends], List, None]
    badges: Union[List[Badge.Badge], List, None]
    patreonFeatures: Union[PatreonFeatures.PatreonFeatures, None]

class PlayerSelfReference:

    id: str
    name: str
    platform: str
    avatar: str
    country: str
    histories: str
    role: str
    pp: float
    rank: int
    countryRank: int
    banned: bool
    inactive: bool
    externalProfileUrl: str
    lastTwoWeeksTime: float
    allTime: float
    scoreStats: Union[PlayerScoreStats.PlayerScoreStats, None]
    statsHistory: Union[PlayerStatsHistory.PlayerStatsHistory, None]
    clans: Union[List[Clan.Clan], List, None]
    friends: Union[List[PlayerFriends.PlayerFriends], List, None]
    badges: Union[List[Badge.Badge], List, None]
    patreonFeatures: Union[PatreonFeatures.PatreonFeatures, None]


# definition function
def gen(response):

    if response is not None:
        instance = Player(
            id=response.get('id'),
            name=response.get('name'),
            platform=response.get('platform'),
            avatar=response.get('avatar'),
            country=response.get('country'),
            histories=response.get('histories'),
            role=response.get('role'),
            pp=response.get('pp'),
            rank=response.get('rank'),
            countryRank=response.get('countryRank'),
            banned=response.get('banned'),
            inactive=response.get('inactive'),
            externalProfileUrl=response.get('externalProfileUrl'),
            lastTwoWeeksTime=response.get('lastTwoWeeksTime'),
            allTime=response.get('allTime'),
            scoreStats=PlayerScoreStats.gen(response.get('scoreStats')),
            statsHistory=PlayerStatsHistory.gen(response.get('statsHistory')),
            clans=Clan.genList(response.get('clans')),
            friends=PlayerFriends.genList(response.get('friends')),
            badges=Badge.genList(response.get('badges')),
            patreonFeatures=PatreonFeatures.gen(
                response.get('patreonFeatures'))
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
