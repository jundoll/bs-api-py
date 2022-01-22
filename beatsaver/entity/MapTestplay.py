# load modules
from dataclasses import dataclass
from typing import Union

from ...beatsaver.entity import UserDetail


# definition class
@dataclass(frozen=True)
class MapTestplay:

    createdAt: str
    feedback: str
    feedbackAt: str
    user: Union[UserDetail.UserDetail, None]
    video: str


# definition function
def gen(response):

    if response is not None:
        instance = MapTestplay(
            createdAt=response.get('createdAt'),
            feedback=response.get('feedback'),
            feedbackAt=response.get('feedbackAt'),
            user=UserDetail.gen(response.get('user')),
            video=response.get('video')
        )
        return instance


def gen_list(response):

    if response is not None:
        if len(response) == 0:
            return []
        else:
            return [gen(v) for v in response]
