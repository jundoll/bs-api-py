# load modules
from dataclasses import dataclass
from typing import List, Union

import Metadata, Score


# definition class
@dataclass(frozen=True)
class ScoreCollection:

    scores: Union[List[Score.Score], List, None]
    metadata:  Union[Metadata.Metadata, None]


# definition function
def gen(response):

    if response is not None:
        instance = ScoreCollection(
            scores=Score.gen_list(response.get('scores')),
            metadata=Metadata.gen(response.get('metadata'))
        )
        return instance


def gen_list(response):

    if response is not None:
        if len(response) == 0:
            return []
        else:
            return [gen(v) for v in response]
