# load modules
from dataclasses import dataclass


# definition class
@dataclass(frozen=True)
class Badge:

    description: str
    image: str


# definition function
def gen(response):

    if response is not None:
        instance = Badge(
            description=response.get('description'),
            image=response.get('image')
        )
        return instance


def gen_list(response):

    if response is not None:
        if len(response) == 0:
            return []
        else:
            return [gen(v) for v in response]
