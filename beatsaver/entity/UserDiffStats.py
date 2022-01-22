# load modules
from dataclasses import dataclass


# definition class
@dataclass(frozen=True)
class UserDiffStats:

    easy: int
    expert: int
    expertPlus: int
    hard: int
    normal: int
    total: int


# definition function
def gen(response):

    if response is not None:
        instance = UserDiffStats(
            easy=response.get('easy'),
            expert=response.get('expert'),
            expertPlus=response.get('expertPlus'),
            hard=response.get('hard'),
            normal=response.get('normal'),
            total=response.get('total')
        )
        return instance


def gen_list(response):

    if response is not None:
        if len(response) == 0:
            return []
        else:
            return [gen(v) for v in response]
