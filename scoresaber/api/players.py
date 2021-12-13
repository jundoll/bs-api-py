
# load modules
from lib import api
from scoresaber.entity import Player, PlayerCollection, PlayerScoreCollection
from scoresaber.parameters import SERVER


# definition
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
