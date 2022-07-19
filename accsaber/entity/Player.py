# load modules
from dataclasses import dataclass


# definition class
@dataclass(frozen=True)
class Player:

    rank: float
    rankLastWeek: float
    playerId: float
    playerName: str
    avatarUrl: str
    hmd: str
    averageAcc: float
    ap: float
    averageApPerMap: float
    rankedPlays: float
    accChamp: bool


# definition function
def gen(response):

    if response is not None:
        instance = Player(
            rank=response.get('rank'),
            rankLastWeek=response.get('rankLastWeek'),
            playerId=response.get('playerId'),
            playerName=response.get('playerName'),
            avatarUrl=response.get('avatarUrl'),
            hmd=response.get('hmd'),
            averageAcc=response.get('averageAcc'),
            ap=response.get('ap'),
            averageApPerMap=response.get('averageApPerMap'),
            rankedPlays=response.get('rankedPlays'),
            accChamp=response.get('accChamp')
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
