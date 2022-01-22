# load modules
from dataclasses import dataclass
from typing import Union

from ...beatsaver.entity import UserStats


# definition class
@dataclass(frozen=True)
class UserDetail:

    avatar: str
    curator: bool
    email: str
    hash: str
    id: int
    name: str
    stats: Union[UserStats.UserStats, None]
    testplay: bool
    type: str
    uniqueSet: bool
    uploadLimit: int


# definition function
def gen(response):

    if response is not None:
        instance = UserDetail(
            avatar=response.get('avatar'),
            curator=response.get('curator'),
            email=response.get('email'),
            hash=response.get('hash'),
            id=response.get('id'),
            name=response.get('name'),
            stats=UserStats.gen(response.get('stats')),
            testplay=response.get('testplay'),
            type=response.get('type'),
            uniqueSet=response.get('uniqueSet'),
            uploadLimit=response.get('uploadLimit')
        )
        return instance


def gen_list(response):

    if response is not None:
        if len(response) == 0:
            return []
        else:
            return [gen(v) for v in response]
