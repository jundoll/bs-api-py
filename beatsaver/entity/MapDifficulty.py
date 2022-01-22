# load modules
from dataclasses import dataclass
from typing import Union

from ...beatsaver.entity import MapParitySummary


# definition class
@dataclass(frozen=True)
class MapDifficulty:

    bombs: int
    characteristic: str
    chroma: bool
    cinema: bool
    difficulty: str
    events: int
    length: float
    me: bool
    ne: bool
    njs: float
    notes: int
    nps: float
    obstacles: int
    offset: float
    paritySummary: Union[MapParitySummary.MapParitySummary, None]
    seconds: float
    stars: float


# definition function
def gen(response):

    if response is not None:
        instance = MapDifficulty(
            bombs=response.get('bombs'),
            characteristic=response.get('characteristic'),
            chroma=response.get('chroma'),
            cinema=response.get('cinema'),
            difficulty=response.get('difficulty'),
            events=response.get('events'),
            length=response.get('length'),
            me=response.get('me'),
            ne=response.get('ne'),
            njs=response.get('njs'),
            notes=response.get('notes'),
            nps=response.get('notenpss'),
            obstacles=response.get('obstacles'),
            offset=response.get('offset'),
            paritySummary=MapParitySummary.gen(response.get('paritySummary')),
            seconds=response.get('seconds'),
            stars=response.get('stars')
        )
        return instance


def gen_list(response):

    if response is not None:
        if len(response) == 0:
            return []
        else:
            return [gen(v) for v in response]
