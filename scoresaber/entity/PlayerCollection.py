# load modules
from dataclasses import dataclass
from typing import List, Union

from scoresaber.entity import Metadata, Player


# definition class
@dataclass(frozen=True)
class PlayerCollection:

    players: Union[List[Player.Player], List, None]
    metadata: Union[Metadata.Metadata, None]


# definition function
def gen(response):

    if response is not None:
        instance = PlayerCollection(
            players=Player.gen_list(response.get('players')),
            metadata=Metadata.gen(response.get('metadata'))
        )
        return instance


def gen_list(response):

    if response is not None:
        if len(response) == 0:
            return []
        else:
            return [gen(v) for v in response]
