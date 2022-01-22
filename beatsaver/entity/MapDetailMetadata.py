# load modules
from dataclasses import dataclass


# definition class
@dataclass(frozen=True)
class MapDetailMetadata:

    bpm: float
    duration: int
    levelAuthorName: str
    songAuthorName: str
    songName: str
    songSubName: str


# definition function
def gen(response):

    if response is not None:
        instance = MapDetailMetadata(
            bpm=response.get('bpm'),
            duration=response.get('duration'),
            levelAuthorName=response.get('levelAuthorName'),
            songAuthorName=response.get('songAuthorName'),
            songName=response.get('songName'),
            songSubName=response.get('songSubName')
        )
        return instance


def gen_list(response):

    if response is not None:
        if len(response) == 0:
            return []
        else:
            return [gen(v) for v in response]
