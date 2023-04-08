
# load modules
from dataclasses import dataclass


# definition class
@dataclass(frozen=True)
class ScoreImprovement:
    id: str


# definition function
def gen(response):
    instance = ScoreImprovement(
        id=response.get('id'),
    )
    return instance


def gen_list(response):
    if response is not None:
        if len(response) == 0:
            return []
        else:
            return [gen(v) for v in response]
