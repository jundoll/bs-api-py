
# load modules
from dataclasses import dataclass
from typing import List, Union

from . import DifficultyDescription


# definition class
@dataclass(frozen=True)
class Song:
    id: str
    hash: str
    name: str
    subName: str
    author: str
    mapper: str
    mapperId: int
    coverImage: int
    downloadUrl: str
    bpm: float
    duration: float
    tags: str
    uploadTime: int
    difficulties: Union[List[DifficultyDescription.DifficultyDescription], List, None]


# definition function
def gen(response):
    instance = Song(
        id=response.get('id'),
        hash=response.get('hash'),
        name=response.get('name'),
        subName=response.get('subName'),
        author=response.get('author'),
        mapper=response.get('mapper'),
        mapperId=response.get('mapperId'),
        coverImage=response.get('coverImage'),
        downloadUrl=response.get('downloadUrl'),
        bpm=response.get('bpm'),
        duration=response.get('duration'),
        tags=response.get('tags'),
        uploadTime=response.get('uploadTime'),
        difficulties=DifficultyDescription.gen_list(
            response.get('difficulties'))
    )
    return instance


def gen_list(response):
    if response is not None:
        if len(response) == 0:
            return []
        else:
            return [gen(v) for v in response]
