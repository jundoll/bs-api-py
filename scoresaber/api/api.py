
# change base directory
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append( str(current_dir) + '/../../' )

# load modules
from lib import api
from ..entity import (Difficulty, LeaderboardInfo,
                               LeaderboardInfoCollection, Player,
                               PlayerCollection, PlayerScoreCollection,
                               ScoreCollection)

# const
SERVER = 'https://scoresaber.com'


# definition
def get_leaderboards(
    #
    search: str = '',
    # Filter by verified (⚠️️deprecation notice)
    verified: bool = False,
    # Filter by ranked
    ranked: bool = False,
    # Filter by qualified
    qualified: bool = False,
    # Filter by loved
    loved: bool = False,
    # Filter by minimum star value
    minStar: float = -1,
    # Filter by maxiumum star value
    maxStar: float = -1,
    # Which category to sort by (0 = trending, date ranked = 1, scores set = 2, star difficulty = 3, author = 4)
    category: int = -1,
    # Which direction to sort (0 = descending, 1 = ascending)
    sort: int = -1,
    # Only return one leaderboard of each id
    unique: bool = False,
    #
    page: int = 0,
    # (default true)
    withMetadata: bool = False
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
    if withMetadata:
        query_list.append(f'withMetadata=true')
    if len(query_list) > 0:
        query = f'?{"&".join(query_list)}'
    else:
        query = ''

    # request
    request_url = f'{SERVER}/api/leaderboards{query}'
    response_dict = api.get(request_url)
    return LeaderboardInfoCollection.gen_list(response_dict)


def get_leaderboard_info_by_id(
    # ScoreSaber leaderboardId
    leaderboardId: float
):

    # request
    request_url = f'{SERVER}/api/leaderboard/by-id/{leaderboardId}/info'
    response_dict = api.get(request_url)
    return LeaderboardInfo.gen(response_dict)


def get_leaderboard_info_by_hash(
    # Map hash
    hash: str,
    # (1 = Easy, 3 = Normal, 5 = Hard, 7 = Expert, 9 = Expert+)
    difficulty: int = 1,
    # (e.g SoloStandard)
    gameMode: str = ''
):

    # prepare query
    query_list = []
    if (difficulty > 0) and (difficulty <= 9):
        query_list.append(f'difficulty={difficulty}')
    if gameMode:
        query_list.append(f'gameMode={gameMode}')
    if len(query_list) > 0:
        query = f'?{"&".join(query_list)}'
    else:
        query = ''

    # request
    request_url = f'{SERVER}/api/leaderboard/by-hash/{hash}/info{query}'
    response_dict = api.get(request_url)
    return LeaderboardInfo.gen(response_dict)


def get_leaderboard_scores_by_id(
    # ScoreSaber leaderboardId
    leaderboardId: float,
    # Filter by ISO 3166-1 alpha-2 code (comma delimitered)
    contries: str = '',
    #
    search: str = '',
    #
    page: int = 0,
    # (default true)
    withMetadata: bool = False
):

    # prepare query
    query_list = []
    if contries:
        query_list.append(f'contries={contries}')
    if search:
        query_list.append(f'search={search}')
    if page > 0:
        query_list.append(f'page={page}')
    if withMetadata:
        query_list.append(f'withMetadata=true')
    if len(query_list) > 0:
        query = f'?{"&".join(query_list)}'
    else:
        query = ''

    # request
    request_url = f'{SERVER}/api/leaderboard/by-id/{leaderboardId}/scores{query}'
    response_dict = api.get(request_url)
    return ScoreCollection.gen(response_dict)


def get_leaderboard_scores_by_hash(
    # Map hash
    hash: str,
    # (1 = Easy, 3 = Normal, 5 = Hard, 7 = Expert, 9 = Expert+)
    difficulty: int = 1,
    # Filter by ISO 3166-1 alpha-2 code (comma delimitered)
    contries: str = '',
    #
    search: str = '',
    #
    page: int = 0,
    # (e.g SoloStandard)
    gameMode: str = '',
    # (default true)
    withMetadata: bool = False
):

    # prepare query
    query_list = []
    if (difficulty > 0) and (difficulty <= 9):
        query_list.append(f'difficulty={difficulty}')
    if contries:
        query_list.append(f'contries={contries}')
    if search:
        query_list.append(f'search={search}')
    if page > 0:
        query_list.append(f'page={page}')
    if gameMode:
        query_list.append(f'gameMode={gameMode}')
    if withMetadata:
        query_list.append(f'withMetadata=true')
    if len(query_list) > 0:
        query = f'?{"&".join(query_list)}'
    else:
        query = ''

    # request
    request_url = f'{SERVER}/api/leaderboard/by-hash/{hash}/scores{query}'
    response_dict = api.get(request_url)
    return ScoreCollection.gen(response_dict)


def get_leaderboard_difficulties_by_hash(
    # Map hash
    hash: str
):

    # request
    request_url = f'{SERVER}/api/leaderboard/get-difficulties/{hash}'
    response_dict = api.get(request_url)
    return Difficulty.gen_list(response_dict)


def get_players(
    #
    search: str = '',
    #
    page: int = 0,
    # Filter by ISO 3166-1 alpha-2 code (comma delimitered)
    countries: str = '',
    # (default true)
    withMetadata: bool = False
):
    """
    GET /api/players
    """

    # prepare query
    query_list = []
    if search:
        query_list.append(f'search={search}')
    if countries:
        query_list.append(f'countries={countries}')
    if page > 0:
        query_list.append(f'page={page}')
    if withMetadata:
        query_list.append(f'withMetadata=true')
    if len(query_list) > 0:
        query = f'?{"&".join(query_list)}'
    else:
        query = ''

    # request
    request_url = f'{SERVER}/api/players{query}'
    response_dict = api.get(request_url)
    return PlayerCollection.gen(response_dict)


def get_players_count(
    #
    search: str = '',
    # Filter by ISO 3166-1 alpha-2 code (comma delimitered)
    countries: str = ''
):

    # prepare query
    query_list = []
    if search:
        query_list.append(f'search={search}')
    if countries:
        query_list.append(f'countries={countries}')
    if len(query_list) > 0:
        query = f'?{"&".join(query_list)}'
    else:
        query = ''

    # request
    request_url = f'{SERVER}/api/players/count{query}'
    count_value = api.get(request_url)
    return count_value


def get_player_basic(
    #
    playerId: float
):

    # request
    request_url = f'{SERVER}/api/player/{playerId}/basic'
    response_dict = api.get(request_url)
    return Player.gen(response_dict)


def get_player_full(
    #
    playerId: float
):

    # request
    request_url = f'{SERVER}/api/player/{playerId}/full'
    response_dict = api.get(request_url)
    return Player.gen(response_dict)


def get_player_scores(
    #
    playerId: float,
    # The amount of scores to return
    limit: int = 0,
    # Available values : top, recent
    sort: str = '',
    # Page
    page: int = 0,
    # (default true)
    withMetadata: bool = False
):

    # prepare query
    query_list = []
    if limit > 0:
        query_list.append(f'limit={limit}')
    if (sort == 'top') or (sort == 'recent'):
        query_list.append(f'sort={sort}')
    if page > 0:
        query_list.append(f'page={page}')
    if withMetadata:
        query_list.append(f'withMetadata=true')
    if len(query_list) > 0:
        query = f'?{"&".join(query_list)}'
    else:
        query = ''

    # request
    request_url = f'{SERVER}/api/player/{playerId}/scores{query}'
    response_dict = api.get(request_url)
    return PlayerScoreCollection.gen(response_dict)
