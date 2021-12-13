
# load modules
import json
from lib import api
from scoresaber.entity import Player
from scoresaber.entity import PlayerScore
from scoresaber.entity import LeaderboardInfo
from scoresaber.entity import LeaderboardInfoCollection
from scoresaber.parameters import SERVER



# definition
async def get_player_basic(
    playerId: float
):

    # request
    requestUrl = f'{SERVER}/api/player/{playerId}/basic'
    response = await api.get(requestUrl)
    responseJson = json.load(response)
    return Player.gen(responseJson)


async def getPlayerFull(
    playerId: float
):

    # request
    requestUrl = f'{SERVER}/api/player/{playerId}/full'
    response = await api.get(requestUrl)
    responseJson = json.load(response)
    return Player.gen(responseJson)


async def getPlayerScores(
    playerId: float,
    limit: int = -1,
    sort: str = 'top',
    page: int = -1
):

    # prepare query
    query_list = []
    if limit >= 0:
        query_list.append(f'limit={limit}')
    if (sort == 'top') or (sort == 'recent'):
        query_list.append(f'sort={sort}')
    if page > 0:
        query_list.append(f'page={page}')
    if len(query_list) > 0:
        query = f'?{"&".join(query_list)}'
    else:
        query = ''

    # request
    requestUrl = f'{SERVER}/api/player/{playerId}/scores{query}'
    response = await api.get(requestUrl)
    responseJson = json.load(response)
    return PlayerScore.genList(responseJson)


async def getLeaderboardInfoById(
    leaderboardId: float
):

    # request
    requestUrl = f'{SERVER}/api/leaderboard/by-id/{leaderboardId}/info'
    response = await api.get(requestUrl)
    responseJson = json.load(response)
    return LeaderboardInfo.gen(responseJson)


async def getLeaderboardInfoCollection(
    search: str = '',
    verified: bool = False,
    ranked: bool = False,
    qualified: bool = False,
    loved: bool = False,
    minStar: float = -1,
    maxStar: float = -1,
    category: int = -1,
    sort: int = -1,
    unique: bool = False,
    page: int = -1
):

    # prepare query
    query_list = []
    if search:
        query_list.append(f'search={search}')
    if verified:
        query_list.append('verified=true')
    if ranked:
        query_list.append('ranked=true')
    if qualified:
        query_list.append('qualified=true')
    if loved:
        query_list.append('loved=true')
    if minStar >= 0:
        query_list.append(f'minStar={minStar}')
    if maxStar >= 0:
        query_list.append(f'maxStar={maxStar}')
    if (category >= 0) & (category <= 4):
        query_list.append(f'category={category}')
    if (sort >= 0) & (sort <= 1):
        query_list.append(f'sort={sort}')
    if unique:
        query_list.append('unique=true')
    if page > 0:
        query_list.append(f'page={page}')
    if len(query_list) > 0:
        query = f'?{"&".join(query_list)}'
    else:
        query = ''

    # request
    requestUrl = f'{SERVER}/api/leaderboards{query}'
    response = await api.get(requestUrl)
    responseJson = json.load(response)
    return LeaderboardInfoCollection.genList(responseJson)
