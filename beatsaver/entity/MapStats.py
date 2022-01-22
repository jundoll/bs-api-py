# load modules
from dataclasses import dataclass


# definition class
@dataclass(frozen=True)
class MapStats:

    downloads: int
    downvotes: int
    plays: int
    score: float
    scoreOneDP: float
    upvotes: int


# definition function
def gen(response):

    if response is not None:
        instance = MapStats(
            downloads=response.get('downloads'),
            downvotes=response.get('downvotes'),
            plays=response.get('plays'),
            score=response.get('score'),
            scoreOneDP=response.get('scoreOneDP'),
            upvotes=response.get('upvotes')
        )
        return instance


def gen_list(response):

    if response is not None:
        if len(response) == 0:
            return []
        else:
            return [gen(v) for v in response]
