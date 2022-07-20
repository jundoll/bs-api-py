# load modules
from dataclasses import dataclass


# definition class
@dataclass(frozen=True)
class Badge:

    id: int
    description: str
    image: str


# definition function
def gen(response):

    if response is not None:
        instance = Badge(
            id=response.get('id'),
            description=response.get('description'),
            image=response.get('image')
        )
        return instance


def genList(response):

    if response is None:
        return None
    else:
        if type(response) is list:
            if len(response) == 0:
                return []
            else:
                return [gen(v) for v in response]
        elif type(response) is dict:
            return [gen(response)]
