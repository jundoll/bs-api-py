# load modules
from dataclasses import dataclass
from typing import Union

from accsaber.fetcher.Player import extract_player, extract_players


# definition class
@dataclass(frozen=True)
class Player:

    playerId: str
    avatarUrl: str
    playerName: str
    rank: float
    ap: float
    hmd: Union[str, None]
    rankedPlays: float
    averageAcc: Union[float, None]
    averageApPerMap: Union[float, None]


# definition function
def gen(response):

    if response is not None:
        instance = extract_player(response)
        return instance


def genList(response, url):

    if response is not None:
        instances = extract_players(response, url)
        return instances
