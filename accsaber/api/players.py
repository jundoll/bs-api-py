
# load modules
from requests_api import request

from ..entity import Player, PlayerScore

# init
SERVER = 'https://accsaber.com'


# definition
async def get_players(
):
    """
    GET /api/players
    """

    # request
    requestUrl = f'{SERVER}/api/players'
    response_dict = await request.get(requestUrl)
    return Player.genList(response_dict)


async def get_player(
    #
    playerId: float
):
    """
    GET /api/players/{playerId}
    """

    # request
    requestUrl = f'{SERVER}/api/players/{playerId}'
    response_dict = await request.get(requestUrl)
    return Player.gen(response_dict)


async def get_player_scores(
    #
    playerId: float
):
    """
    GET /api/player/{playerId}/scores
    """

    # request
    requestUrl = f'{SERVER}/api/player/{playerId}/scores'
    response_dict = await request.get(requestUrl)
    return PlayerScore.genList(response_dict)
