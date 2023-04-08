
# load modules
from dataclasses import dataclass
from typing import Union

from . import DifficultyStatus, ModifiersMap, ModifiersRating, Requirements


# definition class
@dataclass(frozen=True)
class DifficultyDescription:
    id: int
    value: int
    mode: int
    difficultyName: str
    modeName: str
    status: Union[DifficultyStatus.DifficultyStatus, None]
    modifierValues: Union[ModifiersMap.ModifiersMap, None]
    modifiersRating: Union[ModifiersRating.ModifiersRating, None]
    nominatedTime: int
    qualifiedTime: int
    rankedTime: int
    stars: float
    predictedAcc: float
    passRating: float
    accRating: float
    techRating: float
    type: int
    njs: float
    nps: float
    notes: int
    bombs: int
    walls: int
    maxScore: int
    duration: float
    requirements: Union[Requirements.Requirements, None]


# definition function
def gen(response):
    instance = DifficultyDescription(
        id=response.get('id'),
        value=response.get('value'),
        mode=response.get('mode'),
        difficultyName=response.get('difficultyName'),
        modeName=response.get('modeName'),
        status=None,  # DifficultyStatus.gen(response.get('status')),
        modifierValues=None,  # ModifiersMap.gen(response.get('modifierValues')),
        modifiersRating=None,  # ModifiersRating.gen(response.get('modifiersRating')),
        nominatedTime=response.get('nominatedTime'),
        qualifiedTime=response.get('qualifiedTime'),
        rankedTime=response.get('rankedTime'),
        stars=response.get('stars'),
        predictedAcc=response.get('predictedAcc'),
        passRating=response.get('passRating'),
        accRating=response.get('accRating'),
        techRating=response.get('techRating'),
        type=response.get('type'),
        njs=response.get('njs'),
        nps=response.get('nps'),
        notes=response.get('notes'),
        bombs=response.get('bombs'),
        walls=response.get('walls'),
        maxScore=response.get('maxScore'),
        duration=response.get('duration'),
        requirements=None  # Requirements.gen(response.get('requirements'))
    )
    return instance


def gen_list(response):
    if response is not None:
        if len(response) == 0:
            return []
        else:
            return [gen(v) for v in response]
