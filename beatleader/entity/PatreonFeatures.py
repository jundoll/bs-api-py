# load modules
from dataclasses import dataclass


# definition class
@dataclass(frozen=True)
class PatreonFeatures:

    bio: str
    message: str
    leftSaberColor: str
    rightSaberColor: str


# definition function
def gen(response):

    if response is not None:
        instance = PatreonFeatures(
            bio=response.get('bio'),
            message=response.get('message'),
            leftSaberColor=response.get('leftSaberColor'),
            rightSaberColor=response.get('rightSaberColor')
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
