
# load modules
from common import USER_AGENT
from requests_api import request

from ..entity import Player

# const
SERVER = 'https://accsaber.com'


# definition
async def get_players(
):
    """
    GET /leaderboards
    """

    # request
    request_url = f'{SERVER}/leaderboards'
    response_dict = await request.get(request_url, user_agent=USER_AGENT)
    return Player.genList(response_dict)


async def get_player(
    # scoresaber ID
    playerId: float
):
    """
    GET /profile/{playerId}/overall/scores
    """

    # request
    request_url = f'{SERVER}/profile/{playerId}/overall/scores'
    print(request_url)
    response_dict = await request.get(request_url, user_agent=USER_AGENT)
    return Player.gen(response_dict)
