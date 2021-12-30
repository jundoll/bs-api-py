# load modules
from dataclasses import dataclass
from typing import List, Union

from . import Metadata, PlayerScore


# definition class
@dataclass(frozen=True)
class PlayerScoreCollection:

    playerScores: Union[List[PlayerScore.PlayerScore], List, None]
    metadata:  Union[Metadata.Metadata, None]


# definition function
def gen(response):

    if response is not None:
        instance = PlayerScoreCollection(
            playerScores=PlayerScore.gen_list(response.get('playerScores')),
            metadata=Metadata.gen(response.get('metadata'))
        )
        return instance


def gen_list(response):

    if response is not None:
        if len(response) == 0:
            return []
        else:
            return [gen(v) for v in response]
