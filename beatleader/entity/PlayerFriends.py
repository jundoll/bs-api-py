# load modules
from dataclasses import dataclass

from ..entity import Player


# definition class
@dataclass(frozen=True)
class PlayerFriends:

    id: str
    friends: object  #: Union[List[Player.Player], List, None]


# definition function
def gen(response):

    if response is not None:
        instance = PlayerFriends(
            id=response.get('id'),
            friends=Player.genList(response.get('friends'))
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
