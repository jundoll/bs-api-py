# load modules
from dataclasses import dataclass

from ..entity import Player


# definition class
@dataclass(frozen=True)
class Clan:

    id: int
    name: str
    color: str
    icon: str
    tag: str
    leaderID: str
    description: str
    bio: str
    playersCount: int
    pp: float
    averageRank: float
    averageAccuracy: float
    players: object  #: Union[List[Player.Player], List, None]
    requests: None
    banned: None


# definition function
def gen(response):

    if response is not None:
        instance = Clan(
            id=response.get('id'),
            name=response.get('name'),
            color=response.get('color'),
            icon=response.get('icon'),
            tag=response.get('tag'),
            leaderID=response.get('leaderID'),
            description=response.get('description'),
            bio=response.get('bio'),
            playersCount=response.get('playersCount'),
            pp=response.get('pp'),
            averageRank=response.get('averageRank'),
            averageAccuracy=response.get('averageAccuracy'),
            players=Player.genList(response.get('players')),
            requests=None,
            banned=None
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
