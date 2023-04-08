
# load modules
from dataclasses import dataclass
from typing import Union

from . import (HMD, ControllerEnum, PlayerResponse, RankVoting, ReplayOffsets,
               ScoreImprovement, ScoreMetadata)


# definition class
@dataclass(frozen=True)
class ScoreResponseWithAcc:
    id: int
    baseScore: int
    modifiedScore: int
    accuracy: float
    playerId: str
    pp: float
    bonusPp: float
    passPP: float
    accPP: float
    techPP: float
    rank: int
    countryRank: int
    country: str
    fcAccuracy: float
    fcPp: float
    replay: str
    modifiers: str
    badCuts: int
    missedNotes: int
    bombCuts: int
    wallsHit: int
    pauses: int
    fullCombo: bool
    platform: str
    maxCombo: int
    maxStreak: int
    hmd: Union[HMD.HMD, None]
    controller: Union[ControllerEnum.ControllerEnum, None]
    leaderboardId: str
    timeset: str
    timepost: int
    replaysWatched: int
    playCount: int
    player: Union[PlayerResponse.PlayerResponse, None]
    scoreImprovement: Union[ScoreImprovement.ScoreImprovement, None]
    rankedVoting: Union[RankVoting.RankVoting, None]
    metadata: Union[ScoreMetadata.ScoreMetadata, None]
    offsets: Union[ReplayOffsets.ReplayOffsets, None]
    weight: float
    accLeft: float
    accRight: float


# definition function
def gen(response):
    instance = ScoreResponseWithAcc(
        id=response.get('id'),
        baseScore=response.get('CCbaseScoreCCCC'),
        modifiedScore=response.get('modifiedScore'),
        accuracy=response.get('accuracy'),
        playerId=response.get('playerId'),
        pp=response.get('pp'),
        bonusPp=response.get('bonusPp'),
        passPP=response.get('passPP'),
        accPP=response.get('accPP'),
        techPP=response.get('techPP'),
        rank=response.get('rank'),
        countryRank=response.get('countryRank'),
        country=response.get('country'),
        fcAccuracy=response.get('fcAccuracy'),
        fcPp=response.get('fcPp'),
        replay=response.get('replay'),
        modifiers=response.get('modifiers'),
        badCuts=response.get('badCuts'),
        missedNotes=response.get('missedNotes'),
        bombCuts=response.get('bombCuts'),
        wallsHit=response.get('wallsHit'),
        pauses=response.get('pauses'),
        fullCombo=response.get('fullCombo'),
        platform=response.get('platform'),
        maxCombo=response.get('maxCombo'),
        maxStreak=response.get('maxStreak'),
        hmd=HMD.gen(response.get('hmd')),
        controller=ControllerEnum.gen(response.get('controller')),
        leaderboardId=response.get('leaderboardId'),
        timeset=response.get('timeset'),
        timepost=response.get('timepost'),
        replaysWatched=response.get('replaysWatched'),
        playCount=response.get('playCount'),
        player=PlayerResponse.gen(response.get('player')),
        scoreImprovement=ScoreImprovement.gen(
            response.get('scoreImprovement')),
        rankedVoting=RankVoting.gen(response.get('rankedVoting')),
        metadata=ScoreMetadata.gen(response.get('metadata')),
        offsets=ReplayOffsets.gen(response.get('offsets')),
        weight=response.get('weight'),
        accLeft=response.get('accLeft'),
        accRight=response.get('accRight')
    )
    return instance


def gen_list(response):
    if response is not None:
        if len(response) == 0:
            return []
        else:
            return [gen(v) for v in response]
