# load modules
from dataclasses import dataclass


# definition class
@dataclass(frozen=True)
class PlayerScore:

    rank: float
    ap: float
    weightedAp: float
    score: float
    accuracy: float
    songName: str
    songAuthorName: str
    levelAuthorName: str
    complexity: float
    songHash: str
    difficulty: str
    leaderboardId: str
    beatsaverKey: str
    timeSet: str
    categoryDisplayName: str


# definition function
def gen(response):

    if response is not None:
        instance = PlayerScore(
            rank=response.get('rank'),
            ap=response.get('ap'),
            weightedAp=response.get('weightedAp'),
            score=response.get('score'),
            accuracy=response.get('accuracy'),
            songName=response.get('songName'),
            songAuthorName=response.get('songAuthorName'),
            levelAuthorName=response.get('levelAuthorName'),
            complexity=response.get('complexity'),
            songHash=response.get('songHash'),
            difficulty=response.get('difficulty'),
            leaderboardId=response.get('leaderboardId'),
            beatsaverKey=response.get('beatsaverKey'),
            timeSet=response.get('timeSet'),
            categoryDisplayName=response.get('categoryDisplayName')
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
