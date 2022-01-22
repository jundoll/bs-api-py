# load modules
from dataclasses import dataclass
from typing import List, Union

from ...beatsaver.entity import MapDetailMetadata, MapStats, UserDetail, MapVersion


# definition class
@dataclass(frozen=True)
class MapDetail:

    automapper: bool
    createdAt: str
    curator: str
    deletedAt: str
    description: str
    id: str
    lastPublishedAt: str
    metadata: Union[MapDetailMetadata.MapDetailMetadata, None]
    name: str
    qualified: bool
    ranked: bool
    stats: Union[MapStats.MapStats, None]
    tags: str
    updatedAt: str
    uploaded: str
    uploader: Union[UserDetail.UserDetail, None]
    versions: Union[List[MapVersion.MapVersion], List, None]


# definition function
def gen(response):

    if response is not None:
        instance = MapDetail(
            automapper=response.get('automapper'),
            createdAt=response.get('createdAt'),
            curator=response.get('curator'),
            deletedAt=response.get('deletedAt'),
            description=response.get('description'),
            id=response.get('id'),
            lastPublishedAt=response.get('lastPublishedAt'),
            metadata=MapDetailMetadata.gen(response.get('metadata')),
            name=response.get('name'),
            qualified=response.get('qualified'),
            ranked=response.get('ranked'),
            stats=MapStats.gen(response.get('stats')),
            tags=response.get('tags'),
            updatedAt=response.get('updatedAt'),
            uploaded=response.get('scoreStats'),
            uploader=UserDetail.gen(response.get('uploader')),
            versions=MapVersion.gen_list(response.get('versions'))
        )
        return instance


def gen_list(response):

    if response is not None:
        if len(response) == 0:
            return []
        else:
            return [gen(v) for v in response]
