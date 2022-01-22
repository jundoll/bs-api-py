# load modules
from dataclasses import dataclass
from typing import List, Union

from ...beatsaver.entity import MapDifficulty, MapTestplay


# definition class
@dataclass(frozen=True)
class MapVersion:

    coverURL: str
    createdAt: str
    diffs: Union[List[MapDifficulty.MapDifficulty], List, None]
    downloadURL: str
    feedback: str
    hash: str
    key: str
    previewURL: str
    sageScore: str
    scheduledAt: str
    state: str
    testplayAt: str
    testplays: Union[List[MapTestplay.MapTestplay], List, None]


# definition function
def gen(response):

    if response is not None:
        instance = MapVersion(
            coverURL=response.get('coverURL'),
            createdAt=response.get('createdAt'),
            diffs=MapDifficulty.gen_list(response.get('diffs')),
            downloadURL=response.get('downloadURL'),
            feedback=response.get('feedback'),
            hash=response.get('hash'),
            key=response.get('key'),
            previewURL=response.get('previewURL'),
            sageScore=response.get('sageScore'),
            scheduledAt=response.get('scheduledAt'),
            state=response.get('state'),
            testplayAt=response.get('testplayAt'),
            testplays=MapTestplay.gen_list(response.get('testplays'))
        )
        return instance


def gen_list(response):

    if response is not None:
        if len(response) == 0:
            return []
        else:
            return [gen(v) for v in response]
