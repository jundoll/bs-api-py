# load modules
from dataclasses import dataclass


# definition class
@dataclass(frozen=True)
class Difficulty:

    leaderboardId: float
    difficulty: float
    gameMode: str
    difficultyRaw: str


# definition function
def gen(response):

    if response is not None:
        instance = Difficulty(
            leaderboardId=response.get('leaderboardId'),
            difficulty=response.get('difficulty'),
            gameMode=response.get('gameMode'),
            difficultyRaw=response.get('difficultyRaw')
        )
        return instance


def gen_list(response):

    if response is not None:
        if len(response) == 0:
            return []
        else:
            return [gen(v) for v in response]
